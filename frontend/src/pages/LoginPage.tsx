/**
 * Purpose:
 *   Organization login page for token-based access to protected features.
 * Inputs:
 *   Email/password credentials.
 * Outputs:
 *   Stores token in parent app via callback on success.
 * Dependencies:
 *   Auth endpoint helper.
 * TODO Checklist:
 *   - [ ] Add remember-me option and secure token handling strategy.
 *   - [ ] Add password visibility toggle and accessibility improvements.
 */

import type * as React from "react";
import { useState } from "react";

import { postLogin } from "../api/endpoints";

interface LoginPageProps {
  onLoginSuccess: (token: string) => void;
}

export default function LoginPage({ onLoginSuccess }: LoginPageProps) {
  const [email, setEmail] = useState("analyst@example.edu");
  const [password, setPassword] = useState("changeme123!");
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError("");
    setLoading(true);
    try {
      const result = await postLogin({ email: email.trim(), password });
      onLoginSuccess(result.access_token);
    } catch (err) {
      setError(err instanceof Error ? err.message : "Login failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <section style={styles.page}>
      <h2 style={styles.heading}>Organization Login</h2>
      <p style={styles.info}>
        Demo password in this skeleton: <code>changeme123!</code>
      </p>
      <form onSubmit={handleSubmit} style={styles.form}>
        <label style={styles.label}>
          Email
          <input
            style={styles.input}
            type="email"
            value={email}
            onChange={(event) => setEmail(event.target.value)}
          />
        </label>
        <label style={styles.label}>
          Password
          <input
            style={styles.input}
            type="password"
            value={password}
            onChange={(event) => setPassword(event.target.value)}
          />
        </label>
        <button disabled={loading} type="submit" style={styles.button}>
          {loading ? "Signing In..." : "Login"}
        </button>
        {error ? <p style={styles.error}>{error}</p> : null}
      </form>
    </section>
  );
}

const styles: Record<string, React.CSSProperties> = {
  page: {
    display: "grid",
    gap: "10px",
  },
  heading: {
    margin: 0,
  },
  info: {
    margin: 0,
    color: "#365674",
  },
  form: {
    border: "1px solid #d4dfec",
    borderRadius: "12px",
    padding: "14px",
    display: "grid",
    gap: "10px",
    background: "#ffffff",
    maxWidth: "420px",
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
  },
};




