from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
import os

def generate_pdf_report(session, transcript, chart_path):
    os.makedirs("reports", exist_ok=True)

    pdf_path = f"reports/session_{session.id}_report.pdf"
    c = canvas.Canvas(pdf_path, pagesize=A4)

    width, height = A4
    y = height - 50

    c.setFont("Helvetica-Bold", 16)
    c.drawString(50, y, "Mock Interview Assessment Report")

    y -= 40
    c.setFont("Helvetica", 12)
    c.drawString(50, y, f"Role: {session.role}")

    y -= 25
    c.drawString(50, y, f"Eye Contact Score: {session.eye_contact_score}")

    y -= 25
    c.drawString(50, y, f"Confidence Score: {session.confidence_score}")

    y -= 40
    c.setFont("Helvetica-Bold", 14)
    c.drawString(50, y, "Speech Transcript:")

    y -= 20
    c.setFont("Helvetica", 10)

    for line in transcript.split("."):
        c.drawString(50, y, line.strip())
        y -= 15
        if y < 100:
            c.showPage()
            y = height - 50

    # Add chart image
    if os.path.exists(chart_path):
        c.showPage()
        c.drawImage(chart_path, 50, 200, width=500, preserveAspectRatio=True)

    c.save()
    return pdf_path
