// @ts-check
import { defineConfig } from 'astro/config';
import { unified } from '@astrojs/markdown-remark';
import rehypeSlug from 'rehype-slug';
import { readFileSync } from 'node:fs';

const pre3 = readFileSync(new URL('./src/pages/pre3/index.html', import.meta.url), 'utf8');
if (/\bP\d{3,}\b/.test(pre3)) {
  throw new Error('Pre3 privacy check failed: participant ID found');
}

// https://astro.build/config
export default defineConfig({
  output: 'static',
  site: 'https://lionchena.github.io',
  base: '/ads401',
  build: {
    inlineStylesheets: 'always',
  },
  markdown: {
    processor: unified({
      rehypePlugins: [rehypeSlug],
    }),
  },
});
