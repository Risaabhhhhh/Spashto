const esbuild = require('esbuild');

// Build service worker and extractor
esbuild.build({
  entryPoints: ['src/background/service-worker.ts', 'src/content-scripts/extractor.ts'],
  bundle: true,
  outdir: 'dist',
  format: 'iife',
  minify: true,
}).catch(() => process.exit(1));

// Build sidepanel React app
esbuild.build({
  entryPoints: ['src/sidepanel/index.tsx'],
  bundle: true,
  outdir: 'dist/sidepanel',
  format: 'iife',
  minify: true,
}).catch(() => process.exit(1));
