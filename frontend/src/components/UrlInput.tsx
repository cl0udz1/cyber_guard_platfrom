/**
 * Purpose:
 *   Reusable URL scan input form for guest scanning.
 * Inputs:
 *   User-entered URL string.
 * Outputs:
 *   Calls `onSubmit(url)` when valid.
 * Dependencies:
 *   React hooks + client-side validators.
 * TODO Checklist:
 *   - [ ] Add URL defang/preview behavior for safety.
 *   - [ ] Add keyboard shortcuts and accessibility refinements.
 */

import type * as React from "react";
import { useState } from "react";

import { isValidUrlInput } from "../utils/validators";

interface UrlInputProps {
  loading?: boolean;
  onSubmit: (url: string) => Promise<void> | void;
}

export default function UrlInput({ loading = false, onSubmit }: UrlInputProps) {
  const [url, setUrl] = useState("");
  const [error, setError] = useState("");

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!isValidUrlInput(url)) {
      setError("Please enter a valid URL or domain.");
      return;
    }
    setError("");
    await onSubmit(url.trim());
  }

  return (
    <form onSubmit={handleSubmit} style={styles.form}>
      <label style={styles.label}>
        Suspicious URL
        <input
          style={styles.input}
          type="text"
          placeholder="https://example.com"
          value={url}
          onChange={(event) => setUrl(event.target.value)}
        />
      </label>
      <button disabled={loading} type="submit" style={styles.button}>
        {loading ? "Scanning..." : "Scan URL"}
      </button>
      {error ? <p style={styles.error}>{error}</p> : null}
    </form>
  );
}

const styles: Record<string, React.CSSProperties> = {
  form: {
    display: "grid",
    gap: "10px",
    border: "1px solid #d4dfec",
    borderRadius: "12px",
    padding: "14px",
    background: "#ffffff",
  },
  label: {
    display: "grid",
    gap: "6px",
    fontWeight: 600,
  },
  input: {
    border: "1px solid #afc2d5",
    borderRadius: "8px",
    padding: "10px",
    fontSize: "14px",
  },
  button: {
    width: "fit-content",
    border: "1px solid #0f4a86",
    borderRadius: "8px",
    background: "#1d5b9c",
    color: "#ffffff",
    padding: "8px 12px",
    cursor: "pointer",
  },
  error: {
    margin: 0,
    color: "#b12828",
    fontSize: "14px",
  },
};




