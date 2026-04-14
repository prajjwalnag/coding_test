"use client";

import { useState } from "react";
import Link from "next/link";
// TODO FOR CANDIDATE: 
// import { useDropzone } from 'react-dropzone';
// import Papa from 'papaparse';
// import { BarChart, LineChart ... } from 'recharts';
// import { flexRender, getCoreRowModel ... } from '@tanstack/react-table';

export default function DashboardChallenge() {
  const [data, setData] = useState<any[]>([]);

  return (
    <div className="min-h-screen bg-slate-50 text-slate-900 p-8">
      <div className="max-w-6xl mx-auto">
        <Link href="/" className="text-slate-500 hover:text-slate-800 mb-8 inline-block">&larr; Back to Hub</Link>
        
        <h1 className="text-3xl font-bold mb-2">CSV Analytics Dashboard</h1>
        <p className="text-slate-600 mb-8">
          Upload a dirty CSV file to instantly visualize lead data and trends.
        </p>

        {/* DRAG AND DROP ZONE */}
        <div className="border-2 border-dashed border-slate-300 rounded-xl p-12 text-center bg-white mb-8">
          {/* ----- YOUR CODE HERE ----- */}
          <p className="text-slate-500">
            TODO: Implement <code>react-dropzone</code> here. 
            When a file drops, parse it with <code>PapaParse</code> and update <code>setData()</code>.
            Remember to filter out logically broken rows (dirty data)!
          </p>
          {/* -------------------------- */}
        </div>

        {data.length > 0 ? (
          <div className="space-y-8">
            {/* CHARTS */}
            <div className="grid grid-cols-1 md:grid-cols-2 gap-8">
              <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 h-80 flex items-center justify-center">
                 {/* ----- YOUR CODE HERE ----- */}
                 <p className="text-slate-400">TODO: Render Recharts Bar Chart here</p>
              </div>
              <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 h-80 flex items-center justify-center">
                 {/* ----- YOUR CODE HERE ----- */}
                 <p className="text-slate-400">TODO: Render Recharts Line Chart here</p>
              </div>
            </div>

            {/* DATA TABLE */}
            <div className="bg-white p-6 rounded-xl shadow-sm border border-slate-200 overflow-x-auto h-96 flex items-center justify-center">
               {/* ----- YOUR CODE HERE ----- */}
               <p className="text-slate-400">TODO: Render sortable TanStack Table here</p>
            </div>
          </div>
        ) : (
          <div className="text-center py-20 text-slate-400 border border-slate-200 rounded-xl bg-white shadow-sm">
            <p>Waiting for valid CSV data...</p>
          </div>
        )}
      </div>
    </div>
  );
}
