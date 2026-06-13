"use client";

import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase";
import Navbar from "@/components/navbar";
import Sidebar from "@/components/sidebar"
import {
  Shield,
  AlertTriangle,
  CheckCircle,
  BarChart3
} from "lucide-react";

import {
  PieChart,
  Pie,
  Cell,
  Tooltip,
  ResponsiveContainer
} from "recharts";

interface Audit {
  id: number;
  image_url: string;
  deception_score: number;
  risk_level: string;
  created_at: string;
}

export default function DashboardPage() {
  const [audits, setAudits] = useState<Audit[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchAudits();
  }, []);

  const fetchAudits = async () => {
    const { data, error } = await supabase
      .from("audits")
      .select("*")
      .order("created_at", { ascending: false });

    if (error) {
      console.error(error);
      return;
    }

    setAudits(data || []);
    setLoading(false);
  };
const chartData = [
  {
    name: "High",
    value: audits.filter(
      (a) => a.risk_level === "High"
    ).length,
  },
  {
    name: "Medium",
    value: audits.filter(
      (a) => a.risk_level === "Medium"
    ).length,
  },
  {
    name: "Low",
    value: audits.filter(
      (a) => a.risk_level === "Low"
    ).length,
  },
];

const COLORS = [
  "#ef4444",
  "#eab308",
  "#22c55e",
];
 if (loading) {
  return (
    <div className="min-h-screen bg-slate-950 flex flex-col items-center justify-center">

      <div className="animate-spin rounded-full h-24 w-24 border-4 border-slate-700 border-t-cyan-400" />

      <h2 className="text-white text-2xl font-bold mt-6">
        Loading Audit Data...
      </h2>

      <p className="text-slate-400 mt-2">
        Analyzing records
      </p>

    </div>
  );
}

  return (
  <>
    <Navbar />

    <div className="flex bg-slate-950 text-white">

      <Sidebar />

      <main className="flex-1 p-8">

      <h1 className="text-5xl font-bold text-center mb-10">
        DeceptAI Audit Dashboard
      </h1>

      {/* Stats Cards */}
      <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6 mb-10">

        <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6 shadow-lg">
          <h3 className="text-slate-400 text-sm uppercase tracking-wide">
            Total Audits
          </h3>
          <p className="text-4xl font-bold mt-2">
            {audits.length}
          </p>
        </div>

        <div className="bg-slate-900 border border-red-900 rounded-2xl p-6 shadow-lg">
          <h3 className="text-red-400 text-sm uppercase tracking-wide">
            High Risk
          </h3>
          <p className="text-4xl font-bold text-red-500 mt-2">
            {audits.filter((a) => a.risk_level === "High").length}
          </p>
        </div>

        <div className="bg-slate-900 border border-yellow-900 rounded-2xl p-6 shadow-lg">
          <h3 className="text-yellow-400 text-sm uppercase tracking-wide">
            Medium Risk
          </h3>
          <p className="text-4xl font-bold text-yellow-500 mt-2">
            {audits.filter((a) => a.risk_level === "Medium").length}
          </p>
        </div>

        <div className="bg-slate-900 border border-green-900 rounded-2xl p-6 shadow-lg">
          <h3 className="text-green-400 text-sm uppercase tracking-wide">
            Low Risk
          </h3>
          <p className="text-4xl font-bold text-green-500 mt-2">
            {audits.filter((a) => a.risk_level === "Low").length}
          </p>
        </div>

      </div>
      <div className="bg-slate-900 rounded-2xl p-6 border border-slate-800 mb-10">

  <div className="flex items-center gap-3 mb-6">
    <BarChart3 className="text-cyan-400" />
    <h2 className="text-xl font-bold">
      Risk Distribution
    </h2>
  </div>

  <div className="h-72">

    <ResponsiveContainer width="100%" height="100%">

      <PieChart>

        <Pie
          data={chartData}
          dataKey="value"
          nameKey="name"
          outerRadius={100}
          label
        >
          {chartData.map((entry, index) => (
            <Cell
              key={index}
              fill={COLORS[index]}
            />
          ))}
        </Pie>

        <Tooltip />

      </PieChart>

    </ResponsiveContainer>

  </div>

</div>

      {/* Audit Cards */}
      {audits.length === 0 && (
  <div className="bg-slate-900 rounded-2xl p-16 text-center border border-slate-800">

    <Shield
      size={70}
      className="mx-auto text-cyan-400 mb-4"
    />

    <h2 className="text-2xl font-bold mb-2">
      No Audits Found
    </h2>

    <p className="text-slate-400">
      Upload evidence to start auditing.
    </p>

  </div>
)}
      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">

        {audits.map((audit) => (

          <div
            key={audit.id}
            className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-lg hover:shadow-2xl hover:-translate-y-1 transition duration-300"
          >

            <img
              src={audit.image_url}
              alt="Evidence"
              className="w-full h-64 object-contain bg-slate-800 p-4"
            />

            <div className="p-5">

              <div className="flex items-center justify-between mb-4">

                <p className="text-xl font-bold">
                  Score: {audit.deception_score}
                </p>

                <span
                  className={
                    audit.risk_level === "High"
                      ? "px-3 py-1 rounded-full bg-red-500/20 text-red-400 font-semibold"
                      : audit.risk_level === "Medium"
                      ? "px-3 py-1 rounded-full bg-yellow-500/20 text-yellow-400 font-semibold"
                      : "px-3 py-1 rounded-full bg-green-500/20 text-green-400 font-semibold"
                  }
                >
                  {audit.risk_level}
                </span>

              </div>

              <p className="text-sm text-slate-400">
                Audit ID: #{audit.id}
              </p>

              <p className="text-sm text-slate-500 mt-2">
                {new Date(audit.created_at).toLocaleString()}
              </p>
                                </div>
          </div>

        ))}

      </div>

         </main>

      </div>

      </>
);
}