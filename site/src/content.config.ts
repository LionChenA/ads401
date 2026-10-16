import { defineCollection, z } from 'astro:content';
import { glob } from 'astro/loaders';

const report = defineCollection({
  loader: glob({ pattern: '**/*.md', base: './src/content' }),
  schema: z.object({
    title: z.string(),
  }),
});

export const collections = { report };
