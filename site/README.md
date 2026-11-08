# ADS401 Group A site

The Astro site builds three routes under the configured `/ads401` base path:

- `/` — project entry and presentation menu.
- `/pre2/` — archived report, with its route in `src/pages/pre2/` and content in `src/content/report.md`.
- `/pre3/` — interactive presentation, with its route and source in `src/pages/pre3/`.

The Pre3 source omits the interview evidence slide containing participant-linked observations. Astro configuration checks for participant IDs before building; review source changes and the resulting output for privacy before deployment. Do not copy participant data into `public/`. Its navigation links use the configured `/ads401` base path and must be updated if that base changes.

From this directory, run `npm ci` to install dependencies, `npm run build` to build the static site into `dist/`, and `npm run preview` to preview the build. Node 22.22 or newer is required. Build outputs and dependencies are not committed.

See [Astro routing documentation](https://docs.astro.build/en/guides/routing/) for how source files map to routes.

## Original Astro command reference

Run these commands from the `site/` directory:

| Command | Action |
| :--- | :--- |
| `npm install` | Install dependencies. |
| `npm run dev` | Start the local development server at `localhost:4321`. |
| `npm run build` | Build the production site to `./dist/`. |
| `npm run preview` | Preview the build locally. |
| `npm run astro ...` | Run Astro CLI commands such as `astro add` or `astro check`. |
| `npm run astro -- --help` | Show Astro CLI help. |

The original starter README also provided this command for creating a new minimal Astro project:

```sh
npm create astro@latest -- --template minimal
```
