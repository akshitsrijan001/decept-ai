"use client";

import { usePathname } from "next/navigation";
import {
  LayoutDashboard,
  Upload,
  AlertTriangle
} from "lucide-react";

export default function Sidebar() {
  const pathname = usePathname();

  const links = [
    {
      name: "Dashboard",
      href: "/dashboard",
      icon: LayoutDashboard
    },
    {
      name: "Upload",
      href: "/upload",
      icon: Upload
    },
    {
      name: "Violations",
      href: "/violations",
      icon: AlertTriangle
    }
  ];

  return (
    <aside className="w-64 bg-slate-900 border-r border-slate-800 min-h-screen p-6">

      <div className="space-y-2">

        {links.map((link) => {
          const Icon = link.icon;

          return (
            <a
              key={link.href}
              href={link.href}
              className={`flex items-center gap-3 px-4 py-3 rounded-xl transition
                ${
                  pathname === link.href
                    ? "bg-cyan-500 text-black font-semibold"
                    : "text-slate-300 hover:bg-slate-800"
                }`}
            >
              <Icon size={18} />
              {link.name}
            </a>
          );
        })}

      </div>
    </aside>
  );
}