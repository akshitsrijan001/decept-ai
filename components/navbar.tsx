import { ShieldCheck } from "lucide-react";

export default function Navbar() {
  return (
    <nav className="h-16 bg-slate-900 border-b border-slate-800 flex items-center justify-between px-8">

      <div className="flex items-center gap-3">
        <ShieldCheck className="text-cyan-400" size={28} />
        <h1 className="text-cyan-400 text-2xl font-bold">
          DeceptAI
        </h1>
      </div>

      <div className="text-slate-400 text-sm">
        AI Dark Pattern Auditor
      </div>

    </nav>
  );
}