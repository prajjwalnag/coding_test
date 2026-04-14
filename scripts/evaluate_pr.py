#!/usr/bin/env python3
"""
Automated PR Evaluation for the Full-Stack Coding Assessment.

Scoring matches SCORING_RUBRIC.md (100 pts total):
  Backend  — 30 pts  (weather 15, enrollment 15)
  Frontend — 40 pts  (dashboard 20, landing 20)
  Selenium — 30 pts  (cookie 10, headless 20)

Live backend API tests and a frontend build are run as informational
diagnostics (not counted in the 100-pt score).

Produces:
  - evaluation_results.json   (machine-readable scores)
  - evaluation_comment.md     (pre-formatted Markdown for the PR comment)
"""

import ast
import json
import re
import subprocess
import sys
import time
import pathlib
import urllib.error
import urllib.parse
import urllib.request

ROOT = pathlib.Path(__file__).parent.parent
BACKEND_PORT = 8765
RESULTS_FILE = ROOT / "evaluation_results.json"
COMMENT_FILE = ROOT / "evaluation_comment.md"


# ─── helpers ──────────────────────────────────────────────────────────────────

def read(path: pathlib.Path) -> str:
    try:
        return path.read_text(encoding="utf-8", errors="replace")
    except Exception:
        return ""


def strip_py_comments(src: str) -> str:
    """Remove Python # comments and triple-quoted docstrings."""
    src = re.sub(r'""".*?"""', "", src, flags=re.DOTALL)
    src = re.sub(r"'''.*?'''", "", src, flags=re.DOTALL)
    src = re.sub(r"#[^\n]*", "", src)
    return src


def strip_ts_comments(src: str) -> str:
    """Remove TypeScript // and /* */ comments."""
    src = re.sub(r"/\*.*?\*/", "", src, flags=re.DOTALL)
    src = re.sub(r"//[^\n]*", "", src)
    return src


def http_get(url: str, timeout: int = 8):
    """Return (status_code, body_bytes). Never raises."""
    try:
        with urllib.request.urlopen(url, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as exc:
        return exc.code, b""
    except Exception:
        return 0, b""


def http_post_form(url: str, fields: dict, timeout: int = 8):
    """POST application/x-www-form-urlencoded. Never raises."""
    data = urllib.parse.urlencode(fields, doseq=True).encode()
    req = urllib.request.Request(
        url,
        data=data,
        method="POST",
        headers={"Content-Type": "application/x-www-form-urlencoded"},
    )
    try:
        with urllib.request.urlopen(req, timeout=timeout) as r:
            return r.status, r.read()
    except urllib.error.HTTPError as exc:
        try:
            body = exc.read()
        except Exception:
            body = b""
        return exc.code, body
    except Exception:
        return 0, b""


def award(name: str, pts: int, passed: bool, detail: str = "") -> dict:
    return {"name": name, "earned": pts if passed else 0, "max": pts,
            "passed": passed, "detail": detail}


def info_check(name: str, passed: bool, detail: str = "") -> dict:
    """Informational check — does not contribute to the 100-pt score."""
    return {"name": name, "earned": 0, "max": 0, "passed": passed, "detail": detail}


# ─── Backend static analysis (30 pts) ─────────────────────────────────────────

def analyse_backend() -> list:
    src_raw = read(ROOT / "backend" / "main.py")
    src = strip_py_comments(src_raw)

    try:
        tree = ast.parse(src_raw)
    except SyntaxError as exc:
        return [award("Python syntax is valid", 0, False, str(exc))]

    checks = []

    # ── Weather (15 pts) ────────────────────────────────────────────────────

    # [5] Query construction: OWM URL + appid in actual code (not docstring)
    has_owm = bool(re.search(r"openweathermap|appid", src))
    checks.append(award(
        "Weather [5pts]: constructs OWM URL with city param and appid",
        5, has_owm,
        "Searched outside comments/docstrings for 'openweathermap' or 'appid'",
    ))

    # [5] Async implementation: httpx.AsyncClient call + async def function
    uses_async_client = bool(re.search(r"httpx\.AsyncClient", src))
    async_weather = any(
        isinstance(n, ast.AsyncFunctionDef) and "weather" in n.name.lower()
        for n in ast.walk(tree)
    )
    checks.append(award(
        "Weather [5pts]: uses httpx.AsyncClient inside an async def",
        5, uses_async_client and async_weather,
        f"httpx.AsyncClient={uses_async_client}, async def={async_weather}",
    ))

    # [5] Error handling: try/except inside the weather function body
    weather_fn = next(
        (n for n in ast.walk(tree)
         if isinstance(n, ast.AsyncFunctionDef) and "weather" in n.name.lower()),
        None,
    )
    try_in_weather = bool(
        weather_fn and any(isinstance(n, ast.Try) for n in ast.walk(weather_fn))
    )
    checks.append(award(
        "Weather [5pts]: try/except block handles errors gracefully",
        5, try_in_weather,
    ))

    # ── Enrollment (15 pts) ─────────────────────────────────────────────────

    # [5] Form extraction: actual Form(...) call detected via AST
    uses_form_call = any(
        isinstance(n, ast.Call)
        and (
            (isinstance(n.func, ast.Name) and n.func.id == "Form")
            or (isinstance(n.func, ast.Attribute) and n.func.attr == "Form")
        )
        for n in ast.walk(tree)
    )
    checks.append(award(
        "Enrollment [5pts]: function params use Form(...)",
        5, uses_form_call,
    ))

    # [5] Data types: List[str]/list[str], date, bool in enrollment function args
    enroll_fn = next(
        (n for n in ast.walk(tree)
         if isinstance(n, (ast.AsyncFunctionDef, ast.FunctionDef))
         and "enroll" in n.name.lower()),
        None,
    )
    has_list_str = has_date = has_bool = False
    if enroll_fn:
        for arg in enroll_fn.args.args:
            ann = ast.unparse(arg.annotation) if arg.annotation else ""
            if re.search(r"List\[str\]|list\[str\]", ann):
                has_list_str = True
            if re.search(r"\bdate\b", ann):
                has_date = True
            if ann.strip() == "bool":
                has_bool = True
    checks.append(award(
        "Enrollment [5pts]: correct param types (List[str], date, bool)",
        5, has_list_str and has_date and has_bool,
        f"List[str]={has_list_str}, date={has_date}, bool={has_bool}",
    ))

    # [5] Not left as a stub — 501 placeholder must be gone
    still_stub = bool(re.search(r"enrollment not implemented", src, re.I))
    checks.append(award(
        "Enrollment [5pts]: implementation replaces the stub",
        5, not still_stub,
    ))

    return checks


# ─── Backend live API tests (informational) ────────────────────────────────────

def run_live_tests() -> list:
    checks = []
    proc = None
    try:
        proc = subprocess.Popen(
            [sys.executable, "-m", "uvicorn", "main:app",
             "--host", "127.0.0.1", "--port", str(BACKEND_PORT)],
            cwd=ROOT / "backend",
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
        )

        base = f"http://127.0.0.1:{BACKEND_PORT}"
        ready = False
        for _ in range(15):
            time.sleep(1)
            code, _ = http_get(f"{base}/docs", timeout=2)
            if code == 200:
                ready = True
                break

        if not ready:
            checks.append(info_check("Live: server starts", False,
                                     "uvicorn did not become ready within 15 s"))
            return checks

        checks.append(info_check("Live: server starts", True))

        code, _ = http_get(f"{base}/api/weather?city=London")
        checks.append(info_check(
            "Live: GET /api/weather?city=London", code != 501, f"HTTP {code}"
        ))

        code, _ = http_get(f"{base}/api/weather?city=XXXINVALIDCITY999")
        checks.append(info_check(
            "Live: invalid city returns clean 4xx (not 500/501)",
            400 <= code < 500, f"HTTP {code}",
        ))

        fields = {
            "parent_name": "Jane Doe", "child_name": "Baby Doe",
            "date_of_birth": "2020-06-15",
            "enrolled_programs": ["math", "science"],
            "agreed_to_terms": "true",
        }
        code, body = http_post_form(f"{base}/api/enrollment", fields)
        checks.append(info_check("Live: POST /api/enrollment returns 200",
                                 code == 200, f"HTTP {code}"))
        if code == 200:
            try:
                resp = json.loads(body)
            except Exception:
                resp = {}
            required = {"parent_name", "child_name", "date_of_birth",
                        "enrolled_programs", "agreed_to_terms"}
            checks.append(info_check(
                "Live: enrollment response has all required fields",
                required.issubset(resp.keys()),
                f"Keys: {sorted(resp.keys())}",
            ))
    finally:
        if proc:
            proc.terminate()
            try:
                proc.wait(timeout=5)
            except subprocess.TimeoutExpired:
                proc.kill()
    return checks


# ─── Frontend checks (40 pts + informational build) ───────────────────────────

def check_frontend() -> list:
    checks = []

    # ── Build (informational) ────────────────────────────────────────────────
    try:
        build = subprocess.run(
            ["npm", "run", "build"], cwd=ROOT / "frontend",
            capture_output=True, text=True, timeout=120,
        )
        build_ok = build.returncode == 0
        detail = "" if build_ok else build.stderr[-400:].strip()
    except Exception as exc:
        build_ok, detail = False, str(exc)
    checks.append(info_check("Build: npm run build succeeds", build_ok, detail))

    # ── Dashboard (20 pts) ──────────────────────────────────────────────────
    src = strip_ts_comments(
        read(ROOT / "frontend" / "src" / "app" / "dashboard" / "page.tsx")
    )

    uses_dropzone = bool(re.search(r"useDropzone|from\s+['\"]react-dropzone['\"]", src))
    checks.append(award("Dashboard [5pts]: implements react-dropzone (useDropzone)", 5, uses_dropzone))

    uses_papa = bool(re.search(r"Papa\.parse|from\s+['\"]papaparse['\"]", src, re.I))
    checks.append(award("Dashboard [5pts]: uses PapaParse for CSV parsing", 5, uses_papa))

    has_filter = bool(re.search(r"\.filter\s*\(", src))
    checks.append(award("Dashboard [5pts]: filters dirty rows with .filter()", 5, has_filter))

    uses_recharts = bool(re.search(r"from\s+['\"]recharts['\"]|BarChart|LineChart|AreaChart|ComposedChart", src))
    uses_tanstack = bool(re.search(r"from\s+['\"]@tanstack|useReactTable|flexRender|getCoreRowModel", src))
    checks.append(award(
        "Dashboard [5pts]: uses Recharts charts and TanStack Table", 5,
        uses_recharts and uses_tanstack,
        f"recharts={uses_recharts}, tanstack={uses_tanstack}",
    ))

    # ── Landing (20 pts) ────────────────────────────────────────────────────
    landing = strip_ts_comments(
        read(ROOT / "frontend" / "src" / "app" / "landing" / "page.tsx")
    )
    layout = strip_ts_comments(
        read(ROOT / "frontend" / "src" / "app" / "layout.tsx")
    )

    has_responsive = bool(re.search(r"(?:md|lg|sm):[a-z]|grid-cols-\d|flex-col", landing))
    no_hardcoded = not bool(re.search(r'w-\[800px\]|w-\[600px\]|w-\[200vw\]', landing))
    checks.append(award(
        "Landing [5pts]: responsive layout (no broken hardcoded widths)", 5,
        has_responsive and no_hardcoded,
        f"responsive_classes={has_responsive}, no_hardcoded_widths={no_hardcoded}",
    ))

    uses_map = bool(re.search(r"\.map\s*\(", landing))
    checks.append(award("Landing [5pts]: navbar uses .map() over a constant array", 5, uses_map))

    uses_themes = bool(re.search(
        r"ThemeProvider|from\s+['\"]next-themes['\"]|useTheme", layout + landing
    ))
    checks.append(award("Landing [5pts]: next-themes dark mode wired into layout", 5, uses_themes))

    uses_framer = bool(re.search(r"from\s+['\"]framer-motion['\"]|motion\.[a-z]", landing))
    checks.append(award("Landing [5pts]: framer-motion entrance animations", 5, uses_framer))

    return checks


# ─── Selenium checks (30 pts) ─────────────────────────────────────────────────

def check_selenium() -> list:
    src = strip_py_comments(read(ROOT / "e2e-tests" / "facebook_automation.py"))
    checks = []

    uses_robust = bool(re.search(r"By\.ID|By\.XPATH|By\.NAME", src))
    checks.append(award(
        "Selenium [5pts]: uses robust selectors (By.ID / By.XPATH / By.NAME)", 5, uses_robust
    ))

    has_c_user = bool(re.search(r"c_user", src))
    has_xs = bool(re.search(r"""['"]xs['"]""", src))
    checks.append(award(
        "Selenium [5pts]: isolates c_user and xs cookies", 5,
        has_c_user and has_xs,
        f"c_user={has_c_user}, xs={has_xs}",
    ))

    injects = bool(re.search(r"add_cookie", src))
    checks.append(award(
        "Selenium [5pts]: uses driver.add_cookie() for session injection", 5, injects
    ))

    has_scroll = bool(re.search(
        r"window\.scrollTo|ActionChains|PAGE_DOWN|Keys\.PAGE_DOWN|execute_script.*scroll",
        src, re.I,
    ))
    has_wait = bool(re.search(r"WebDriverWait|expected_conditions|EC\.", src))
    scroll_pts = (5 if has_scroll else 0) + (5 if has_wait else 0)
    checks.append({
        "name": "Selenium [10pts]: scroll + WebDriverWait for lazy-loading",
        "earned": scroll_pts, "max": 10, "passed": scroll_pts == 10,
        "detail": f"scroll_mechanism={has_scroll}, WebDriverWait={has_wait}",
    })

    extracts_text = bool(re.search(r"\.text\b", src))
    checks.append(award(
        "Selenium [5pts]: extracts post text via .text attribute", 5, extracts_text
    ))

    return checks


# ─── Report builder ────────────────────────────────────────────────────────────

def _pct(earned: int, max_pts: int) -> int:
    """Return integer percentage, 0 if max_pts is 0."""
    return int(earned / max_pts * 100) if max_pts else 0


def _e(passed: bool) -> str:
    return "✅" if passed else "❌"


def _table(checks: list) -> str:
    rows = []
    for c in checks:
        score = f"{c['earned']}/{c['max']}" if c["max"] > 0 else "—"
        detail = f" — _{c['detail']}_" if c.get("detail") else ""
        rows.append(f"| {_e(c['passed'])} | {c['name']} | {score}{detail} |")
    return "\n".join(rows)


def build_report(backend, live, frontend, selenium) -> tuple[dict, str]:
    def total(checks):
        e = sum(c["earned"] for c in checks if c["max"] > 0)
        m = sum(c["max"]    for c in checks if c["max"] > 0)
        return e, m

    be_e, be_m = total(backend)
    fe_e, fe_m = total(frontend)
    se_e, se_m = total(selenium)
    grand_e = be_e + fe_e + se_e
    grand_m = be_m + fe_m + se_m  # == 100

    results = {
        "backend":   {"earned": be_e, "max": be_m, "checks": backend},
        "frontend":  {"earned": fe_e, "max": fe_m, "checks": frontend},
        "selenium":  {"earned": se_e, "max": se_m, "checks": selenium},
        "live_tests": live,
        "total_earned": grand_e,
        "total_max": grand_m,
    }

    pct   = _pct(grand_e, grand_m)
    bar   = "█" * int(pct / 5) + "░" * (20 - int(pct / 5))
    fe_scored = [c for c in frontend if c["max"] > 0]
    fe_info   = [c for c in frontend if c["max"] == 0]
    live_rows = _table(live) if live else "_No live test data._"

    md = f"""## 🤖 Automated Evaluation Report

> Auto-generated on every PR push. Scores are based on static code analysis and live API tests.
> A human reviewer will assess code quality, UI fidelity, and overall cleanliness.

---

### 📊 Overall Score: **{grand_e} / {grand_m}**

`[{bar}]` {pct}%

---

### 🐍 Backend — FastAPI &nbsp; `{be_e}/{be_m} pts`

| | Check | Score |
|--|-------|-------|
{_table(backend)}

<details>
<summary>🔬 Live API test results (informational — not scored)</summary>

| | Check | Result |
|--|-------|--------|
{live_rows}

</details>

---

### ⚛️ Frontend — Next.js &nbsp; `{fe_e}/{fe_m} pts`

| | Check | Score |
|--|-------|-------|
{_table(fe_scored)}

<details>
<summary>🔨 Build result (informational — not scored)</summary>

| | Check | Result |
|--|-------|--------|
{_table(fe_info)}

</details>

---

### 🤖 Selenium Automation &nbsp; `{se_e}/{se_m} pts`

> ℹ️ Evaluated by static code analysis only — live Facebook automation cannot run in CI.

| | Check | Score |
|--|-------|-------|
{_table(selenium)}

---

<details>
<summary>📋 Full rubric reference</summary>

See [SCORING_RUBRIC.md](./SCORING_RUBRIC.md) for the complete point breakdown used by human reviewers.

</details>
"""
    return results, md


# ─── Main ──────────────────────────────────────────────────────────────────────

def main():
    print("▶ Backend static analysis…")
    backend = analyse_backend()

    print("▶ Backend live tests…")
    live = run_live_tests()

    print("▶ Frontend checks…")
    frontend = check_frontend()

    print("▶ Selenium static analysis…")
    selenium = check_selenium()

    results, comment = build_report(backend, live, frontend, selenium)

    RESULTS_FILE.write_text(json.dumps(results, indent=2))
    COMMENT_FILE.write_text(comment)

    e, m = results["total_earned"], results["total_max"]
    print(f"\n✅ Evaluation complete: {e}/{m} ({_pct(e, m)}%)")
    print(f"   Results → {RESULTS_FILE}")
    print(f"   Comment → {COMMENT_FILE}")


if __name__ == "__main__":
    main()
