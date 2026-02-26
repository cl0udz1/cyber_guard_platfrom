"""
Purpose:
    Generate downloadable PDF report from simplified scan response data.
Inputs:
    Safety report dictionary (scan_id/status/score/summary/reasons/created_at).
Outputs:
    PDF bytes suitable for HTTP response download.
Dependencies:
    reportlab (recommended), io buffer.
TODO Checklist:
    - [ ] Integrate endpoint for PDF download once scan retrieval flow is stable.
    - [ ] Add organization branding/header/footer template.
    - [ ] Add test coverage for PDF content basics.
"""

from io import BytesIO
from typing import Any


def generate_safety_report_pdf(report: dict[str, Any]) -> bytes:
    """
    Create a very basic PDF document.

    NOTE:
        This function intentionally keeps formatting simple for beginner students.
    """
    try:
        from reportlab.lib.pagesizes import letter
        from reportlab.pdfgen import canvas
    except Exception:
        # Fallback keeps project runnable even if reportlab is missing.
        text_fallback = (
            "PDF generation library missing.\n"
            f"scan_id: {report.get('scan_id')}\n"
            f"status: {report.get('status')}\n"
            f"summary: {report.get('summary')}\n"
        )
        return text_fallback.encode("utf-8")

    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=letter)
    y = 750

    pdf.setTitle("Cyber Guard Safety Report")
    pdf.setFont("Helvetica-Bold", 14)
    pdf.drawString(72, y, "Cyber Guard Platform - Safety Report")
    y -= 28

    pdf.setFont("Helvetica", 11)
    lines = [
        f"Scan ID: {report.get('scan_id', '-')}",
        f"Status: {report.get('status', '-')}",
        f"Score: {report.get('score', '-')}",
        f"Created At: {report.get('created_at', '-')}",
        "",
        f"Summary: {report.get('summary', '-')}",
        "",
        "Reasons:",
    ]
    for item in report.get("reasons", []):
        lines.append(f"- {item}")

    for line in lines:
        pdf.drawString(72, y, line[:100])
        y -= 18
        if y < 72:
            pdf.showPage()
            y = 750
            pdf.setFont("Helvetica", 11)

    pdf.showPage()
    pdf.save()
    return buffer.getvalue()
