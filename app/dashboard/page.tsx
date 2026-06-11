import Sidebar from "@/components/sidebar";

export default function DashboardPage() {
  return (
    <div className="flex">
      <Sidebar />

      <main className="flex-1 p-8">
        <h1 className="text-3xl font-bold mb-6">
          Dashboard
        </h1>

        <div className="grid grid-cols-3 gap-4">
          <div className="border rounded-lg p-6">
            Total Audits
          </div>

          <div className="border rounded-lg p-6">
            Risk Score
          </div>

          <div className="border rounded-lg p-6">
            Violations
          </div>
        </div>
      </main>
    </div>
  );
}