/**
 * Purpose:
 *   React entry point that mounts the app into the Vite HTML root node.
 * Inputs:
 *   Browser DOM element `#root`.
 * Outputs:
 *   Rendered SPA UI.
 * Dependencies:
 *   React, ReactDOM, `App.tsx`.
 * TODO Checklist:
 *   - [ ] Add global CSS theme tokens.
 *   - [ ] Add strict error boundary around main app.
 */

import React from "react";
import ReactDOM from "react-dom/client";
import App from "./App";

ReactDOM.createRoot(document.getElementById("root") as HTMLElement).render(
  <React.StrictMode>
    <App />
  </React.StrictMode>
);


