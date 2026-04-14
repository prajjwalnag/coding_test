"use client"

import Link from "next/link";
// import { motion } from "framer-motion";
// import { useTheme } from "next-themes";

export default function BrokenLandingChallenge() {
  
  // TODO: Fix this messy hardcoded navigation using a JSON map
  return (
    <div className="bg-white min-h-screen relative text-black">
      
      {/* 
        MESSY NAVIGATION BAR
        Candidate Instructions: Refactor this entirely. Extract into a mapped array.
        Add Dark/Light Mode toggle here.
      */}
      <nav className="p-4 border-b absolute w-full top-0 left-0 bg-white/50 z-50">
        <div className="max-w-7xl mx-auto flex justify-between">
          <div className="font-bold text-xl">SaaSify.</div>
          <div className="flex gap-4">
            <a href="#" className="text-gray-500 hover:text-black">Features</a>
            <a href="#" className="text-gray-500 hover:text-black">Pricing</a>
            <a href="#" className="text-gray-500 hover:text-black">Testimonials</a>
            <a href="#" className="text-gray-500 hover:text-black">Blog</a>
            <a href="#" className="text-gray-500 hover:text-black pl-8 font-semibold">Login</a>
          </div>
        </div>
      </nav>

      {/* 
        BROKEN HERO SECTION 
        Candidate Instructions: 
        1. Notice how the text overlaps the image on smaller screens. 
        2. Fix the flexbox/grid so it stacks perfectly on mobile but aligns side-by-side on 1920px. 
        3. Add Framer Motion entrance animations.
      */}
      <div className="pt-32 pb-20 max-w-7xl mx-auto px-4 h-[600px] flex items-center">
        <div className="w-[800px] absolute z-10 left-20 border bg-white/80 p-8 shadow-2xl">
          <h1 className="text-6xl font-extrabold mb-4">Automate your entire workflow.</h1>
          <p className="text-xl mb-8">Stop doing manual work. Build pipelines that run your business while you sleep.</p>
          <button className="bg-blue-600 text-white px-8 py-4 rounded-md">Start for free</button>
        </div>
        
        {/* Unresponsive overlapping image block */}
        <div className="absolute right-0 w-[600px] h-[400px] bg-gradient-to-tr from-purple-500 to-pink-500 rounded-l-3xl shadow-xl z-0">
          <div className="p-8 text-white text-9xl flex items-center justify-center h-full opacity-50 font-black">
            UI
          </div>
        </div>
      </div>

      {/* 
        BROKEN FEATURE GRID
        Candidate Instructions: Fix layout so cards don't squish horizontally.
      */}
      <div className="bg-gray-100 p-20 flex gap-4 w-[200vw] overflow-x-hidden">
        <div className="bg-white p-8 shadow-sm w-[400px]">
          <h3 className="font-bold text-2xl">Feature 1</h3>
          <p>This box looks terrible on mobile right now.</p>
        </div>
        <div className="bg-white p-8 shadow-sm w-[400px]">
          <h3 className="font-bold text-2xl">Feature 2</h3>
          <p>Flex constraints are completely broken.</p>
        </div>
        <div className="bg-white p-8 shadow-sm w-[400px]">
          <h3 className="font-bold text-2xl">Feature 3</h3>
          <p>Needs responsive grid implementation.</p>
        </div>
      </div>

    </div>
  );
}
