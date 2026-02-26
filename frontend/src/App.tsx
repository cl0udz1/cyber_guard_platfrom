/**
 * Purpose:
 *   Top-level frontend shell with simple tab navigation across MVP pages.
 * Inputs:
 *   Local UI state (active page, access token).
 * Outputs:
 *   Rendered page component for guest scan, login, IoC submit, or dashboard.
 * Dependencies:
 *   React hooks and page components.
 * TODO Checklist:
 *   - [ ] Replace tab state with React Router for deep-linking.
 *   - [ ] Add global notification/toast system.
 *   - [ ] Add persistent auth refresh strategy.
 */

import type * as React from "react";
import { useMemo, useState } from "react";

import DashboardPage from "./pages/DashboardPage";
import GuestScanPage from "./pages/GuestScanPage";
import LoginPage from "./pages/LoginPage";
import SubmitIocPage from "./pages/SubmitIocPage";

type ViewKey = "guest" | "login" | "submit_ioc" | "dashboard";

const navItems: Array<{ key: ViewKey; label: string }> = [
  { key: "guest", label: "Guest Scan" },
  { key: "login", label: "Login" },
  { key: "submit_ioc", label: "Submit IoC" },
  { key: "dashboard", label: "Dashboard" },
];

export default function App() {
  const [activeView, setActiveView] = useState<ViewKey>("guest");
  const [token, setToken] = useState<string>(() => localStorage.getItem("cg_token") ?? "");

  const isLoggedIn = useMemo(() => token.trim().length > 0, [token]);

  function handleLoginSuccess(accessToken: string) {
    setToken(accessToken);
    localStorage.setItem("cg_token", accessToken);
    setActiveView("dashboard");
  }

  function handleLogout() {
    setToken("");
    localStorage.removeItem("cg_token");
    setActiveView("guest");
  }

  return (
    <div style={styles.page}>
      <header style={styles.header}>
        <h1 style={styles.title}>cyber_guard_platform</h1>
        <p style={styles.subtitle}>
          Student MVP skeleton: guest scan + anonymous IoC sharing (Disconnect by Design)
        </p>
        <nav style={styles.nav}>
          {navItems.map((item) => (
            <button
              key={item.key}
              onClick={() => setActiveView(item.key)}
              style={{
                ...styles.navButton,
                ...(activeView === item.key ? styles.navButtonActive : {}),
              }}
            >
              {item.label}
            </button>
          ))}
          {isLoggedIn ? (
            <button onClick={handleLogout} style={styles.logoutButton}>
              Logout
            </button>
          ) : null}
        </nav>
      </header>

      <main style={styles.main}>
        {activeView === "guest" ? <GuestScanPage /> : null}
        {activeView === "login" ? <LoginPage onLoginSuccess={handleLoginSuccess} /> : null}
        {activeView === "submit_ioc" ? <SubmitIocPage token={token} /> : null}
        {activeView === "dashboard" ? <DashboardPage token={token} /> : null}
      </main>
    </div>
  );
}

const styles: Record<string, React.CSSProperties> = {
  page: {
    minHeight: "100vh",
    background:
      "radial-gradient(circle at top right, rgba(208, 240, 255, 0.7), rgba(250, 253, 255, 1))",
    color: "#102030",
    fontFamily: "'Segoe UI', Tahoma, Geneva, Verdana, sans-serif",
    padding: "24px",
  },
  header: {
    maxWidth: "1000px",
    margin: "0 auto 20px auto",
    border: "1px solid #c8d7e6",
    borderRadius: "16px",
    padding: "16px 20px",
    backgroundColor: "#ffffff",
    boxShadow: "0 8px 18px rgba(16, 32, 48, 0.08)",
  },
  title: {
    margin: "0 0 4px 0",
    fontSize: "28px",
  },
  subtitle: {
    margin: "0 0 12px 0",
    color: "#3f556c",
  },
  nav: {
    display: "flex",
    gap: "8px",
    flexWrap: "wrap",
  },
  navButton: {
    border: "1px solid #9bb1c8",
    background: "#f2f7fc",
    padding: "8px 14px",
    borderRadius: "999px",
    cursor: "pointer",
  },
  navButtonActive: {
    borderColor: "#1d5b9c",
    background: "#dcecff",
    fontWeight: 600,
  },
  logoutButton: {
    marginLeft: "auto",
    border: "1px solid #bf5a5a",
    background: "#ffecec",
    padding: "8px 14px",
    borderRadius: "999px",
    cursor: "pointer",
  },
  main: {
    maxWidth: "1000px",
    margin: "0 auto",
  },
};




