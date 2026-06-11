export default function Navbar() {
  return (
    <nav className="flex items-center justify-between border-b px-6 py-4">
      <h1 className="text-xl font-bold">
        DeceptAI
      </h1>

      <div className="flex gap-6">
        <a href="/">Home</a>
        <a href="/dashboard">Dashboard</a>
        <a href="/upload">Upload</a>
      </div>
    </nav>
  );
}