/**
 * Purpose:
 *   Auth-protected IoC submission page with anonymity-focused guidance.
 * Inputs:
 *   IoC form values (type/value/confidence/tags/first_seen).
 * Outputs:
 *   Calls IoC submit endpoint and displays submission result.
 * Dependencies:
 *   Auth token prop and IoC endpoint helper.
 * TODO Checklist:
 *   - [ ] Add per-IoC-type format validation.
 *   - [ ] Add duplicate detection warning from backend response.
 */

import type * as React from "react";
import { useState } from "react";

import { postSubmitIoc } from "../api/endpoints";
import type { IocType } from "../types/ioc";
import { isConfidenceInRange } from "../utils/validators";

interface SubmitIocPageProps {
  token: string;
}

const iocTypes: IocType[] = ["ip", "domain", "url", "hash", "email", "file_name", "other"];

export default function SubmitIocPage({ token }: SubmitIocPageProps) {
  const [type, setType] = useState<IocType>("domain");
  const [value, setValue] = useState("");
  const [confidence, setConfidence] = useState(50);
  const [tagsText, setTagsText] = useState("phishing");
  const [firstSeen, setFirstSeen] = useState("");
  const [statusMessage, setStatusMessage] = useState("");
  const [error, setError] = useState("");
  const [loading, setLoading] = useState(false);

  async function handleSubmit(event: React.FormEvent<HTMLFormElement>) {
    event.preventDefault();
    setError("");
    setStatusMessage("");

    if (!token) {
      setError("Please login first.");
      return;
    }
    if (!value.trim()) {
      setError("IoC value is required.");
      return;
    }
    if (!isConfidenceInRange(confidence)) {
      setError("Confidence must be between 0 and 100.");
      return;
    }

    const tags = tagsText
      .split(",")
      .map((tag) => tag.trim())
      .filter(Boolean);

    setLoading(true);
    try {
      const result = await postSubmitIoc(
        {
          type,
          value: value.trim(),
          confidence,
          tags,
          first_seen: firstSeen || undefined,
        },
        token
      );
      setStatusMessage(`Stored IoC successfully. ID: ${result.ioc_id}`);
      setValue("");
    } catch (err) {
      setError(err instanceof Error ? err.message : "IoC submission failed.");
    } finally {
      setLoading(false);
    }
  }

  return (
    <section style={styles.page}>
      <h2 style={styles.heading}>Submit Anonymous IoC</h2>
      <p style={styles.info}>
        Privacy rule: backend must strip/reject identity fields. Do not include user/org identity.
      </p>
      <form style={styles.form} onSubmit={handleSubmit}>
        <label style={styles.label}>
          Type
          <select value={type} onChange={(event) => setType(event.target.value as IocType)} style={styles.input}>
            {iocTypes.map((iocType) => (
              <option key={iocType} value={iocType}>
                {iocType}
              </option>
            ))}
          </select>
        </label>
        <label style={styles.label}>
          Value
          <input style={styles.input} value={value} onChange={(event) => setValue(event.target.value)} />
        </label>
        <label style={styles.label}>
          Confidence (0-100)
          <input
            style={styles.input}
            type="number"
            min={0}
            max={100}
            value={confidence}
            onChange={(event) => setConfidence(Number(event.target.value))}
          />
        </label>
        <label style={styles.label}>
          Tags (comma-separated)
          <input style={styles.input} value={tagsText} onChange={(event) => setTagsText(event.target.value)} />
        </label>
        <label style={styles.label}>
          First Seen (optional ISO datetime)
          <input
            style={styles.input}
            placeholder="2026-02-26T09:30:00Z"
            value={firstSeen}
            onChange={(event) => setFirstSeen(event.target.value)}
          />
        </label>
        <button disabled={loading} style={styles.button} type="submit">
          {loading ? "Submitting..." : "Submit IoC"}
        </button>
      </form>
      {statusMessage ? <p style={styles.success}>{statusMessage}</p> : null}
      {error ? <p style={styles.error}>{error}</p> : null}
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
    maxWidth: "520px",
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
  success: {
    margin: 0,
    color: "#1f7a3f",
    fontWeight: 600,
  },
  error: {
    margin: 0,
    color: "#b12828",
  },
};




