from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib import colors
from reportlab.lib.styles import getSampleStyleSheet
from reportlab.lib.pagesizes import A4
import io


def build_pdf_bytes(data):

    # ✅ MEMORY BUFFER (file save nahi karega disk pe)
    buffer = io.BytesIO()

    doc = SimpleDocTemplate(buffer, pagesize=A4)
    styles = getSampleStyleSheet()

    elements = []

    # ===== HEADER =====
    elements.append(Paragraph(
        "<para align=center><font size=18 color='#1f4e79'><b>AI MEDICAL REPORT</b></font></para>",
        styles["Normal"]
    ))
    elements.append(Paragraph(
        "<para align=center><font size=10 color='grey'>Intelligent Analysis. Better Health.</font></para>",
        styles["Normal"]
    ))
    elements.append(Spacer(1, 15))

    # ===== PATIENT DETAILS =====
    elements.append(Paragraph("<b>1. PATIENT DETAILS</b>", styles["Heading2"]))

    patient = data.get("patient", {})

    patient_table = [[
        f"Name\n{patient.get('Name', 'N/A')}",
        f"Age\n{patient.get('Age', 'N/A')}",
        f"Gender\n{patient.get('Gender', 'N/A')}"
    ]]

    t = Table(patient_table, colWidths=[150, 150, 150])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), colors.lightblue),
        ("BOX", (0, 0), (-1, -1), 1, colors.grey),
        ("ALIGN", (0, 0), (-1, -1), "CENTER"),
    ]))

    elements.append(t)
    elements.append(Spacer(1, 20))

    # ===== SAFE STATUS FUNCTION =====
    def status(val, min_v, max_v):
        try:
            val = float(val)
            return "NORMAL" if min_v <= val <= max_v else "ABNORMAL"
        except:
            return "N/A"

    vitals = data.get("vitals", {})

    # ===== MEDICAL PARAMETERS =====
    elements.append(Paragraph("<b>2. MEDICAL PARAMETERS</b>", styles["Heading2"]))

    table_data = [
        ["Parameter", "Your Value", "Normal Range", "Status"],
        ["Glucose", vitals.get("Glucose", "N/A"), "70-140",
         status(vitals.get("Glucose", "N/A"), 70, 140)],

        ["Blood Pressure", vitals.get("BP", "N/A"), "90-120",
         status(vitals.get("BP", "N/A"), 90, 120)],

        ["BMI", vitals.get("BMI", "N/A"), "18.5-24.9",
         status(vitals.get("BMI", "N/A"), 18.5, 24.9)],

        ["Oxygen", vitals.get("Oxygen", "N/A"), "95-100",
         status(vitals.get("Oxygen", "N/A"), 95, 100)],

        ["Temperature", vitals.get("Temperature", "N/A"), "36-37.5",
         status(vitals.get("Temperature", "N/A"), 36, 37.5)],
    ]

    t = Table(table_data, colWidths=[120, 100, 120, 100])

    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, 0), colors.teal),
        ("TEXTCOLOR", (0, 0), (-1, 0), colors.white),
        ("GRID", (0, 0), (-1, -1), 1, colors.grey),
    ]))

    elements.append(t)
    elements.append(Spacer(1, 20))

    # ===== AI DIAGNOSIS =====
    elements.append(Paragraph("<b>3. AI DIAGNOSIS</b>", styles["Heading2"]))

    results = data.get("results", {})

    for k, v in results.items():
        elements.append(Paragraph(f"<b>{k}:</b> {v}", styles["Normal"]))

    elements.append(Spacer(1, 10))

    # ===== RISK =====
    risk = data.get("risk", "N/A")

    color = "green"
    if risk == "High":
        color = "red"
    elif risk == "Medium":
        color = "orange"

    elements.append(Paragraph(
        f"<b>RISK LEVEL:</b> <font color='{color}'>{risk}</font>",
        styles["Normal"]
    ))

    elements.append(Spacer(1, 20))

    # ===== DOCTOR SUGGESTION =====
    elements.append(Paragraph("<b>4. DOCTOR SUGGESTION</b>", styles["Heading2"]))

    suggestion = """
    Your health parameters are within acceptable range.<br/><br/>
    • Eat a balanced diet<br/>
    • Exercise regularly (30–45 min daily)<br/>
    • Stay hydrated<br/>
    • Sleep 7–8 hours daily<br/>
    • Manage stress<br/>
    • Regular health checkups recommended
    """

    elements.append(Paragraph(suggestion, styles["Normal"]))
    elements.append(Spacer(1, 15))

    # ===== PRECAUTIONS =====
    elements.append(Paragraph("<b>5. PRECAUTIONS</b>", styles["Heading2"]))

    precautions = """
    • Avoid junk food<br/>
    • Limit sugar & salt<br/>
    • Avoid smoking & alcohol<br/>
    • Stay active<br/>
    • Consult doctor if symptoms appear
    """

    elements.append(Paragraph(precautions, styles["Normal"]))
    elements.append(Spacer(1, 20))

    # ===== DISCLAIMER =====
    elements.append(Paragraph(
        "<font size=8>This is an AI-generated report. Not a substitute for medical advice.</font>",
        styles["Normal"]
    ))

    # ===== BUILD PDF =====
    doc.build(elements)

    # ✅ RETURN BYTES
    pdf = buffer.getvalue()
    buffer.close()

    return pdf