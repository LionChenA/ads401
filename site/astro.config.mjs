// @ts-check
import { defineConfig } from 'astro/config';
import { unified } from '@astrojs/markdown-remark';
import rehypeSlug from 'rehype-slug';

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
