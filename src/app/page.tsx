export default function Home() {
  return (
    <div className="min-h-screen flex items-center justify-center p-8">
      <main className="max-w-4xl w-full space-y-8">
        <div className="text-center space-y-4">
          <h1 className="text-6xl font-bold tracking-tight">
            Next.js Geist Font Starter
          </h1>
          <p className="text-xl text-muted-foreground font-mono">
            A beautiful starter template with Geist font family
          </p>
        </div>

        <div className="grid gap-6 md:grid-cols-2 lg:grid-cols-3">
          <div className="p-6 rounded-lg border bg-card text-card-foreground shadow-sm hover:shadow-md transition-shadow">
            <h2 className="text-2xl font-semibold mb-2">Geist Sans</h2>
            <p className="text-muted-foreground">
              A modern sans-serif font designed for optimal readability and clarity.
            </p>
          </div>

          <div className="p-6 rounded-lg border bg-card text-card-foreground shadow-sm hover:shadow-md transition-shadow">
            <h2 className="text-2xl font-semibold mb-2 font-mono">Geist Mono</h2>
            <p className="text-muted-foreground font-mono">
              A monospace font perfect for code and technical content.
            </p>
          </div>

          <div className="p-6 rounded-lg border bg-card text-card-foreground shadow-sm hover:shadow-md transition-shadow">
            <h2 className="text-2xl font-semibold mb-2">Next.js 16</h2>
            <p className="text-muted-foreground">
              Built with the latest Next.js features and best practices.
            </p>
          </div>
        </div>

        <div className="text-center space-y-4 pt-8">
          <div className="flex gap-4 justify-center flex-wrap">
            <a
              href="https://nextjs.org/docs"
              target="_blank"
              rel="noopener noreferrer"
              className="px-6 py-3 rounded-lg bg-primary text-primary-foreground hover:bg-primary/90 transition-colors font-medium"
            >
              Next.js Docs
            </a>
            <a
              href="https://vercel.com/font"
              target="_blank"
              rel="noopener noreferrer"
              className="px-6 py-3 rounded-lg border border-border hover:bg-accent transition-colors font-medium"
            >
              Learn about Geist
            </a>
          </div>
        </div>
      </main>
    </div>
  );
}
