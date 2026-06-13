"use client";

import { useEffect, useState } from "react";
import { supabase } from "@/lib/supabase";
import Navbar from "@/components/navbar";
import Sidebar from "@/components/sidebar";
import { AlertTriangle } from "lucide-react";

interface Audit {
  id: number;
  image_url: string;
  deception_score: number;
  risk_level: string;
  created_at: string;
}

export default function ViolationsPage() {
  const [violations, setViolations] = useState<Audit[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchViolations();
  }, []);

  const fetchViolations = async () => {
    const { data, error } = await supabase
      .from("audits")
      .select("*")
      .in("risk_level", ["Medium", "High"])
      .order("created_at", { ascending: false });

    if (error) {
      console.error(error);
      return;
    }

    setViolations(data || []);
    setLoading(false);
  };

  if (loading) {
    return (
      <div className="min-h-screen bg-slate-950 flex items-center justify-center">
        <div className="animate-spin rounded-full h-16 w-16 border-b-2 border-cyan-400"></div>
      </div>
    );
  }

  return (
    <>
      <Navbar />

      <div className="flex bg-slate-950 text-white min-h-screen">

        <Sidebar />

        <main className="flex-1 p-8">

          <div className="flex items-center gap-3 mb-8">
            <AlertTriangle className="text-red-400" size={32} />

            <div>
              <h1 className="text-4xl font-bold">
                Violations
              </h1>

              <p className="text-slate-400">
                Medium and High risk audit findings
              </p>
            </div>
          </div>

          {violations.length === 0 ? (
            <div className="bg-slate-900 border border-slate-800 rounded-2xl p-12 text-center">

              <AlertTriangle
                size={60}
                className="mx-auto text-green-400 mb-4"
              />

              <h2 className="text-2xl font-bold mb-2">
                No Violations Found
              </h2>

              <p className="text-slate-400">
                No medium or high risk audits detected.
              </p>

            </div>
          ) : (
            <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-8">

              {violations.map((audit) => (
                <div
                  key={audit.id}
                  className="bg-slate-900 border border-slate-800 rounded-2xl overflow-hidden shadow-lg"
                >

                  <img
                    src={audit.image_url}
                    alt="Evidence"
                    className="w-full h-64 object-contain bg-slate-800 p-4"
                  />

                  <div className="p-5">

                    <div className="flex items-center justify-between mb-4">

                      <p className="font-bold">
                        Score: {audit.deception_score}
                      </p>

                      <span
                        className={
                          audit.risk_level === "High"
                            ? "px-3 py-1 rounded-full bg-red-500/20 text-red-400"
                            : "px-3 py-1 rounded-full bg-yellow-500/20 text-yellow-400"
                        }
                      >
                        {audit.risk_level}
                      </span>

                    </div>

                    <p className="text-slate-400 text-sm">
                      Audit #{audit.id}
                    </p>

                    <p className="text-slate-500 text-sm mt-2">
                      {new Date(
                        audit.created_at
                      ).toLocaleString()}
                    </p>

                  </div>

                </div>
              ))}

            </div>
          )}

        </main>

      </div>
    </>
  );
}