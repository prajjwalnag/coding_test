import Link from "next/link";

export default function Home() {
  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 flex items-center justify-center p-8">
      <div className="max-w-2xl w-full">
        <h1 className="text-5xl font-extrabold text-transparent bg-clip-text bg-gradient-to-r from-indigo-400 to-cyan-400 mb-6 text-center">
          Frontend Challenge Hub
        </h1>
        <p className="text-slate-400 text-center mb-12 text-lg">
          Select a task below to begin the assessment.
        </p>

        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <Link href="/dashboard" className="group relative block bg-slate-900 border border-slate-800 hover:border-indigo-500/50 p-8 rounded-2xl transition-all hover:shadow-[0_0_30px_-5px_rgba(99,102,241,0.3)]">
            <div className="absolute top-0 right-0 w-32 h-32 bg-indigo-500/10 blur-3xl rounded-full group-hover:bg-indigo-500/20 transition-all"></div>
            <h2 className="text-2xl font-bold text-slate-200 mb-3 group-hover:text-indigo-400 transition-colors">Task 1: CSV Dashboard</h2>
            <p className="text-slate-500 text-sm leading-relaxed">
              Parse dirty CSV data in the browser and beautifully visualize it using Recharts, PapaParse, and TanStack Table.
            </p>
          </Link>

          <Link href="/landing" className="group relative block bg-slate-900 border border-slate-800 hover:border-cyan-500/50 p-8 rounded-2xl transition-all hover:shadow-[0_0_30px_-5px_rgba(34,211,238,0.3)]">
            <div className="absolute top-0 right-0 w-32 h-32 bg-cyan-500/10 blur-3xl rounded-full group-hover:bg-cyan-500/20 transition-all"></div>
            <h2 className="text-2xl font-bold text-slate-200 mb-3 group-hover:text-cyan-400 transition-colors">Task 2: Pixel Perfect Fix</h2>
            <p className="text-slate-500 text-sm leading-relaxed">
              Take a heavily broken SaaS landing page layout and meticulously fix the CSS, adding Dark Mode and Framer Motion.
            </p>
          </Link>
        </div>
      </div>
    </div>
  );
}
