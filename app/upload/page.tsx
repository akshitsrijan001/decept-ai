import UploadZone from "@/components/UploadZone";
import Navbar from "@/components/navbar";
import Sidebar from "@/components/sidebar";
import { UploadCloud, ShieldCheck } from "lucide-react";

export default function UploadPage() {
  return (
    <>
      <Navbar />

      <div className="flex bg-slate-950 text-white min-h-screen">

        <Sidebar />

        <main className="flex-1 p-8">

          <div className="max-w-5xl mx-auto">

            <div className="text-center mb-10">

              <div className="flex justify-center mb-4">
                <ShieldCheck
                  size={60}
                  className="text-cyan-400"
                />
              </div>

              <h1 className="text-5xl font-bold mb-4">
                Upload Evidence
              </h1>

              <p className="text-slate-400 text-lg">
                Submit screenshots, webpages, or UI captures for
                dark pattern analysis.
              </p>

            </div>

            <div className="bg-slate-900 border border-slate-800 rounded-3xl shadow-xl p-10">

              <div className="flex items-center gap-3 mb-6">

                <UploadCloud
                  size={28}
                  className="text-cyan-400"
                />

                <h2 className="text-2xl font-semibold">
                  Evidence Upload
                </h2>

              </div>

              <p className="text-slate-400 mb-8">
                Supported formats: PNG, JPG, JPEG
              </p>

              <UploadZone />

            </div>

            <div className="grid md:grid-cols-3 gap-6 mt-10">

              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

                <h3 className="font-bold text-cyan-400 mb-2">
                  OCR Analysis
                </h3>

                <p className="text-slate-400 text-sm">
                  Extracts visible text from screenshots and UI flows.
                </p>

              </div>

              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

                <h3 className="font-bold text-cyan-400 mb-2">
                  Pattern Detection
                </h3>

                <p className="text-slate-400 text-sm">
                  Identifies urgency, scarcity, forced action and
                  deceptive UX techniques.
                </p>

              </div>

              <div className="bg-slate-900 border border-slate-800 rounded-2xl p-6">

                <h3 className="font-bold text-cyan-400 mb-2">
                  Risk Scoring
                </h3>

                <p className="text-slate-400 text-sm">
                  Generates audit scores and stores evidence
                  automatically.
                </p>

              </div>

            </div>

          </div>

        </main>

      </div>
    </>
  );
}