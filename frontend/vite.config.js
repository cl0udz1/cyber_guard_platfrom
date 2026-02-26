/**
 * Purpose:
 *   Vite configuration for React + TypeScript frontend.
 * Inputs:
 *   Build/dev server options.
 * Outputs:
 *   Dev server and bundling behavior.
 * Dependencies:
 *   `vite`, `@vitejs/plugin-react`.
 * TODO Checklist:
 *   - [ ] Add proxy rules if backend CORS strategy changes.
 *   - [ ] Add build optimization settings when project matures.
 */
import { defineConfig } from "vite";
import react from "@vitejs/plugin-react";
export default defineConfig({
    plugins: [react()],
    server: {
        port: 5173,
        host: "0.0.0.0",
    },
});
