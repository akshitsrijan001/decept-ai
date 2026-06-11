export default function Sidebar() {
  return (
    <aside className="w-64 border-r min-h-screen p-6">
      <h2 className="font-bold text-lg mb-6">
        DeceptAI
      </h2>

      <div className="flex flex-col gap-4">
        <a href="/dashboard">Dashboard</a>
        <a href="/upload">Upload</a>
      </div>
    </aside>
  );
}