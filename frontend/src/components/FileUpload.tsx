/**
 * Purpose:
 *   Reusable file upload form for hash-based scan lookup.
 * Inputs:
 *   One selected file.
 * Outputs:
 *   Calls `onSubmit(file)` when user submits.
 * Dependencies:
 *   React hooks.
 * TODO Checklist:
 *   - [ ] Add drag-and-drop support.
 *   - [ ] Add client-side max size warnings before upload.
 */

import type * as React from "react";
import { useState } from "react";

interface FileUploadProps {
  loading?: boolean;
  onSubmit: (file: File) => Promise<void> | void;
}

export default function FileUpload({ loading = false, onSubmit }: FileUploadProps) {
  const [file, setFile] = useState<File | null>(null);
  const [error, setError] = useState("");

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    if (!file) {
      setError("Please choose a file before scanning.");
      return;
    }
    setError("");
    await onSubmit(file);
  }

  return (
    <form onSubmit={handleSubmit} style={styles.form}>
      <label style={styles.label}>
        Suspicious File
        <input
          type="file"
          onChange={(event) => setFile(event.target.files?.[0] ?? null)}
          style={styles.input}
        />
      </label>
      <button disabled={loading} type="submit" style={styles.button}>
        {loading ? "Scanning..." : "Scan File"}
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
    background: "#ffffff",
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




