"use client";

import { useEffect, useState } from "react";
import TaskForm from "@/components/TaskForm";

interface Task {
  id: number;
  title: string;
  description: string;
  status: string;
  created_at: string;
}

export default function Home() {
  const [tasks, setTasks] = useState<Task[]>([]);
  const [error, setError] = useState("");

  const fetchTasks = async () => {
    try {
      // Trying to fetch from the local FastAPI backend
      const res = await fetch("http://localhost:8000/api/tasks");
      if (!res.ok) throw new Error("Failed to fetch tasks. Is the backend running?");
      const data = await res.json();
      setTasks(data);
      setError("");
    } catch (err) {
      console.error(err);
      setError("Unable to connect to the backend API.");
    }
  };

  useEffect(() => {
    fetchTasks();
  }, []);

  return (
    <div className="min-h-screen bg-slate-950 text-slate-100 p-8 font-sans selection:bg-emerald-500/30">
      <div className="max-w-4xl mx-auto">
        <header className="mb-12 text-center">
          <h1 className="text-4xl md:text-5xl font-extrabold tracking-tight mb-4 bg-gradient-to-r from-emerald-400 to-cyan-400 text-transparent bg-clip-text">
            Task Board Challenge
          </h1>
          <p className="text-slate-400">
            A full-stack coding challenge assessing Next.js, FastAPI, and Selenium skills.
          </p>
        </header>

        <TaskForm onTaskAdded={fetchTasks} />

        {error && (
          <div className="bg-red-500/10 border border-red-500/50 text-red-400 p-4 rounded-xl mb-8">
            <p className="font-semibold">⚠️ Connection Error</p>
            <p className="text-sm">{error}</p>
          </div>
        )}

        <div className="bg-slate-900 border border-slate-700/50 rounded-2xl shadow-xl overflow-hidden backdrop-blur-md">
          <table className="w-full text-left border-collapse">
            <thead>
              <tr className="bg-slate-800/80 text-slate-300 text-sm uppercase tracking-wider">
                <th className="p-4 border-b border-slate-700/50 font-medium">ID</th>
                <th className="p-4 border-b border-slate-700/50 font-medium">Title</th>
                <th className="p-4 border-b border-slate-700/50 font-medium">Status</th>
                <th className="p-4 border-b border-slate-700/50 font-medium">Created At</th>
              </tr>
            </thead>
            <tbody className="divide-y divide-slate-800/50">
              {tasks.length === 0 ? (
                <tr>
                  <td colSpan={4} className="p-8 text-center text-slate-500 italic">
                    No tasks found. Try adding one!
                  </td>
                </tr>
              ) : (
                tasks.map((t) => (
                  <tr key={t.id} className="hover:bg-slate-800/30 transition-colors group">
                    <td className="p-4 text-slate-400 font-mono text-sm">#{t.id}</td>
                    <td className="p-4">
                      <p className="font-medium text-slate-200 group-hover:text-emerald-400 transition-colors">{t.title}</p>
                      <p className="text-sm text-slate-500 mt-1">{t.description}</p>
                    </td>
                    <td className="p-4">
                      <span className="inline-flex items-center px-2.5 py-0.5 rounded-full text-xs font-medium bg-cyan-400/10 text-cyan-400 border border-cyan-400/20">
                        {t.status}
                      </span>
                    </td>
                    <td className="p-4 text-sm text-slate-400 font-mono">
                      {new Date(t.created_at).toLocaleString()}
                    </td>
                  </tr>
                ))
              )}
            </tbody>
          </table>
        </div>
      </div>
    </div>
  );
}
