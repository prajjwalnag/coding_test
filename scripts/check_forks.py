#!/usr/bin/env python3
"""
Check Forked Repos Utility

Lists all forks of this coding test repository and reports each fork's
activity status — including the number of commits ahead, latest commit
date, and whether a pull request has been opened back to the upstream repo.

Usage:
    # Requires GITHUB_TOKEN environment variable
    python scripts/check_forks.py

    # Or specify owner/repo explicitly
    python scripts/check_forks.py --owner prajjwalnag --repo coding_test
"""

import argparse
import json
import os
import sys
import urllib.request
import urllib.error
from datetime import datetime, timezone


def gh_api(endpoint, token=None):
    """Make an authenticated GET request to the GitHub REST API."""
    url = f"https://api.github.com{endpoint}"
    headers = {
        "Accept": "application/vnd.github+json",
        "X-GitHub-Api-Version": "2022-11-28",
    }
    if token:
        headers["Authorization"] = f"Bearer {token}"

    req = urllib.request.Request(url, headers=headers)
    try:
        with urllib.request.urlopen(req) as resp:
            return json.loads(resp.read().decode())
    except urllib.error.HTTPError as exc:
        print(f"GitHub API error {exc.code} for {url}: {exc.reason}", file=sys.stderr)
        return None


def list_forks(owner, repo, token=None):
    """Return a list of fork objects, handling pagination."""
    forks = []
    page = 1
    while True:
        data = gh_api(
            f"/repos/{owner}/{repo}/forks?sort=newest&per_page=100&page={page}",
            token,
        )
        if not data:
            break
        forks.extend(data)
        if len(data) < 100:
            break
        page += 1
    return forks


def list_open_prs(owner, repo, token=None):
    """Return open pull requests targeting the upstream repo, handling pagination."""
    prs = []
    page = 1
    while True:
        data = gh_api(
            f"/repos/{owner}/{repo}/pulls?state=open&per_page=100&page={page}",
            token,
        )
        if not data:
            break
        prs.extend(data)
        if len(data) < 100:
            break
        page += 1
    return prs


def compare_commits(owner, repo, base, head, token=None):
    """Return the comparison object between base and head refs."""
    return gh_api(
        f"/repos/{owner}/{repo}/compare/{base}...{head}",
        token,
    )


def check_forks(owner, repo, token=None):
    """Check all forks and print a summary report."""
    print(f"\n{'='*70}")
    print(f"  Fork Report for {owner}/{repo}")
    print(f"{'='*70}\n")

    forks = list_forks(owner, repo, token)
    if not forks:
        print("No forks found.")
        return

    # Gather open PRs to cross-reference against forks
    open_prs = list_open_prs(owner, repo, token)
    pr_authors = {pr["head"]["repo"]["full_name"] for pr in open_prs if pr.get("head", {}).get("repo")}

    # Pre-fetch comparison data for all forks (single pass to avoid duplicate API calls)
    comparisons = {}
    for fork in forks:
        fork_owner = fork["owner"]["login"]
        comparisons[fork_owner] = compare_commits(
            owner, repo, f"{owner}:main", f"{fork_owner}:main", token
        )

    print(f"Total forks: {len(forks)}\n")
    print(f"{'#':<4} {'Fork Owner':<25} {'Created':<12} {'Last Push':<12} {'Ahead':<8} {'PR?':<5}")
    print(f"{'-'*4} {'-'*25} {'-'*12} {'-'*12} {'-'*8} {'-'*5}")

    for idx, fork in enumerate(forks, start=1):
        fork_owner = fork["owner"]["login"]
        full_name = fork["full_name"]
        created = fork.get("created_at", "")[:10]
        pushed = fork.get("pushed_at", "")[:10]
        has_pr = "Yes" if full_name in pr_authors else "No"

        comparison = comparisons.get(fork_owner)
        ahead = str(comparison["ahead_by"]) if comparison and "ahead_by" in comparison else "N/A"

        print(f"{idx:<4} {fork_owner:<25} {created:<12} {pushed:<12} {ahead:<8} {has_pr:<5}")

    print(f"\n{'='*70}")
    print(f"  Report generated at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}")
    print(f"{'='*70}\n")

    # Build structured JSON summary for CI consumption
    summary = []
    for fork in forks:
        fork_owner = fork["owner"]["login"]
        full_name = fork["full_name"]
        comparison = comparisons.get(fork_owner)
        ahead_by = comparison.get("ahead_by", 0) if comparison else 0

        summary.append({
            "owner": fork_owner,
            "full_name": full_name,
            "created_at": fork.get("created_at", ""),
            "pushed_at": fork.get("pushed_at", ""),
            "ahead_by": ahead_by,
            "has_open_pr": full_name in pr_authors,
            "html_url": fork.get("html_url", ""),
        })

    # Write JSON summary if GITHUB_STEP_SUMMARY is available (Actions environment)
    summary_path = os.environ.get("GITHUB_STEP_SUMMARY")
    if summary_path:
        with open(summary_path, "a") as f:
            f.write("## 🍴 Fork Check Report\n\n")
            f.write(f"**Total forks:** {len(forks)}\n\n")
            f.write("| # | Fork Owner | Created | Last Push | Ahead | PR? |\n")
            f.write("|---|-----------|---------|-----------|-------|-----|\n")
            for i, item in enumerate(summary, 1):
                pr_badge = "✅" if item["has_open_pr"] else "❌"
                f.write(
                    f"| {i} | [{item['owner']}]({item['html_url']}) "
                    f"| {item['created_at'][:10]} "
                    f"| {item['pushed_at'][:10]} "
                    f"| {item['ahead_by']} "
                    f"| {pr_badge} |\n"
                )
            f.write(
                f"\n*Generated at {datetime.now(timezone.utc).strftime('%Y-%m-%d %H:%M:%S UTC')}*\n"
            )

    # Write JSON to file for downstream consumption
    output_path = os.environ.get("FORK_REPORT_PATH", "fork_report.json")
    with open(output_path, "w") as f:
        json.dump(summary, f, indent=2)
    print(f"JSON report written to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Check forked repositories for a coding test")
    parser.add_argument("--owner", default=os.environ.get("GITHUB_REPOSITORY_OWNER", "prajjwalnag"))
    parser.add_argument("--repo", default=os.environ.get("GITHUB_REPOSITORY_NAME", "coding_test"))
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        print("Warning: GITHUB_TOKEN not set. API rate limits will be restrictive.", file=sys.stderr)

    check_forks(args.owner, args.repo, token)


if __name__ == "__main__":
    main()
