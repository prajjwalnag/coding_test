"use client";

import { useState } from "react";

export default function TaskForm({ onTaskAdded }: { onTaskAdded: () => void }) {
  const [title, setTitle] = useState("");
  const [description, setDescription] = useState("");
  const [loading, setLoading] = useState(false);

  const handleSubmit = async (e: React.FormEvent) => {
    e.preventDefault();
    setLoading(true);

    try {
      // TODO FOR CANDIDATE:
      // 1. Send a POST request to `http://localhost:8000/api/tasks` 
      //    with the `title` and `description` in the JSON body.
      // 2. If successful, call the `onTaskAdded()` callback to refresh the grid, 
      //    and clear the input fields.
      // 3. Handle any errors (e.g., using alert() or a toast library if added).
      
      // ----- YOUR CODE HERE -----
      console.warn("Submit not implemented yet!");
      alert("onSubmit not implemented. You must write the fetch call!");
      // --------------------------
      
    } catch (error) {
      console.error(error);
      alert("Failed to submit task.");
    } finally {
      setLoading(false);
    }
  };

  return (
    <form onSubmit={handleSubmit} className="bg-slate-900 border border-slate-700/50 p-6 rounded-2xl shadow-xl backdrop-blur-md mb-8">
      <h2 className="text-xl font-semibold mb-4 text-emerald-400">Add New Task</h2>
      <div className="space-y-4">
        <div>
          <label className="block text-sm font-medium text-slate-300 mb-1" htmlFor="title">
            Task Title
          </label>
          <input
            id="title"
            type="text"
            value={title}
            onChange={(e) => setTitle(e.target.value)}
            className="w-full bg-slate-800/50 border border-slate-600 rounded-lg px-4 py-2 text-slate-100 focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-all"
            placeholder="e.g., Setup Database"
            required
          />
        </div>
        <div>
          <label className="block text-sm font-medium text-slate-300 mb-1" htmlFor="description">
            Description
          </label>
          <textarea
            id="description"
            value={description}
            onChange={(e) => setDescription(e.target.value)}
            className="w-full bg-slate-800/50 border border-slate-600 rounded-lg px-4 py-2 text-slate-100 focus:outline-none focus:ring-2 focus:ring-emerald-500 transition-all"
            rows={3}
            placeholder="Detailed description of the task..."
            required
          />
        </div>
        <button
          type="submit"
          disabled={loading}
          className="w-full bg-emerald-500 hover:bg-emerald-600 text-slate-950 font-bold px-6 py-3 rounded-xl shadow-lg shadow-emerald-500/20 active:scale-[0.98] transition-all disabled:opacity-50"
        >
          {loading ? "Adding..." : "Add Task"}
        </button>
      </div>
    </form>
  );
}
