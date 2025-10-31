import { defineConfig } from 'vite';
import react from '@vitejs/plugin-react';
import { resolve } from 'path';

export default defineConfig({
  plugins: [react()],
  define: {
    'process.env.NODE_ENV': JSON.stringify('production'),
    'process.env.REACT_APP_SC_ATTR': JSON.stringify(undefined),
    'process.env.SC_ATTR': JSON.stringify(undefined),
    'process.env.REACT_APP_SC_DISABLE_SPEEDY': JSON.stringify(undefined),
    'process.env.SC_DISABLE_SPEEDY': JSON.stringify(undefined)
  },
  build: {
    lib: {
      entry: resolve(__dirname, 'src/index.ts'),
      name: 'SplitLeaseComponents',
      fileName: 'split-lease-components',
      formats: ['umd'],
    },
    rollupOptions: {
      external: ['react', 'react-dom'],
      output: {
        globals: {
          react: 'React',
          'react-dom': 'ReactDOM',
        },
      },
    },
  },
});


