"""
Purpose:
    Transform raw VirusTotal-style payloads into simple safety report fields.
Inputs:
    Scan ID and raw VT response JSON.
Outputs:
    Simplified report fields used by API responses and PDF generation.
Dependencies:
    Standard library datetime.
TODO Checklist:
    - [ ] Calibrate score thresholds using real dataset validation.
    - [ ] Add richer reason templates by engine/category.
    - [ ] Add localization support if needed.
"""

from datetime import datetime, timezone
from typing import Any


def _extract_stats(vt_payload: dict[str, Any]) -> dict[str, int]:
    """
    Extract analysis stats from multiple possible payload shapes.

    Handles both:
        - VT-like nested payload (`data.attributes.last_analysis_stats`)
        - Simplified test payload (`stats` at root).
    """
    stats = vt_payload.get("stats")
    if isinstance(stats, dict):
        return {
            "malicious": int(stats.get("malicious", 0)),
            "suspicious": int(stats.get("suspicious", 0)),
            "harmless": int(stats.get("harmless", 0)),
            "undetected": int(stats.get("undetected", 0)),
        }

    nested = (
        vt_payload.get("data", {})
        .get("attributes", {})
        .get("last_analysis_stats", {})
    )
    if isinstance(nested, dict):
        return {
            "malicious": int(nested.get("malicious", 0)),
            "suspicious": int(nested.get("suspicious", 0)),
            "harmless": int(nested.get("harmless", 0)),
            "undetected": int(nested.get("undetected", 0)),
        }

    return {"malicious": 0, "suspicious": 0, "harmless": 0, "undetected": 0}


def build_safety_report(scan_id: str, vt_payload: dict[str, Any]) -> dict[str, Any]:
    """
    Build simplified SAFE/SUSPICIOUS/MALICIOUS report.

    Output keys match required API contract.
    """
    stats = _extract_stats(vt_payload)
    malicious = stats["malicious"]
    suspicious = stats["suspicious"]

    if malicious > 0:
        status = "MALICIOUS"
        score = min(100, 80 + malicious * 5)
        summary = "Multiple security engines flagged this target as malicious."
        reasons = [
            f"{malicious} engine(s) marked it as malicious.",
            "Do not open/click/execute related content.",
        ]
    elif suspicious > 0:
        status = "SUSPICIOUS"
        score = min(79, 40 + suspicious * 5)
        summary = "At least one indicator appears suspicious."
        reasons = [
            f"{suspicious} engine(s) marked it as suspicious.",
            "Use caution and verify with additional evidence.",
        ]
    else:
        status = "SAFE"
        score = 10
        summary = "No immediate malicious indicators were detected."
        reasons = [
            "No malicious engine hits were reported in this lookup.",
            "Continue monitoring because no scan is 100% perfect.",
        ]

    return {
        "scan_id": scan_id,
        "status": status,
        "score": score,
        "summary": summary,
        "reasons": reasons,
        "created_at": datetime.now(timezone.utc),
    }
