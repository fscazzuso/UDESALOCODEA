from reportlab.lib.colors import HexColor, white
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import mm
from reportlab.platypus import Paragraph, SimpleDocTemplate, Spacer, Table, TableStyle


output = "output/pdf/resumen_cambios_nova_store.pdf"

doc = SimpleDocTemplate(
    output,
    pagesize=A4,
    rightMargin=22 * mm,
    leftMargin=22 * mm,
    topMargin=18 * mm,
    bottomMargin=18 * mm,
)

styles = getSampleStyleSheet()
title = ParagraphStyle(
    "TitleNova",
    parent=styles["Title"],
    fontName="Helvetica-Bold",
    fontSize=23,
    leading=27,
    textColor=white,
    spaceAfter=5 * mm,
)
subtitle = ParagraphStyle(
    "SubtitleNova",
    parent=styles["Normal"],
    fontName="Helvetica",
    fontSize=10,
    leading=14,
    textColor=HexColor("#DCEEFF"),
)
heading = ParagraphStyle(
    "HeadingNova",
    parent=styles["Heading2"],
    fontName="Helvetica-Bold",
    fontSize=14,
    textColor=HexColor("#183A5A"),
    spaceBefore=5 * mm,
    spaceAfter=3 * mm,
)
body = ParagraphStyle(
    "BodyNova",
    parent=styles["BodyText"],
    fontName="Helvetica",
    fontSize=10.5,
    leading=15,
    textColor=HexColor("#263746"),
    spaceAfter=2.5 * mm,
)

story = []

header = Table(
    [[Paragraph("Nova Store", title), Paragraph("Resumen breve", subtitle)],
     [Paragraph("Cambios desde el último trabajo de mposse-bit", subtitle), ""]],
    colWidths=[115 * mm, 43 * mm],
)
header.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (-1, -1), HexColor("#091727")),
    ("SPAN", (0, 1), (1, 1)),
    ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ("ALIGN", (1, 0), (1, 0), "RIGHT"),
    ("LEFTPADDING", (0, 0), (-1, -1), 14),
    ("RIGHTPADDING", (0, 0), (-1, -1), 14),
    ("TOPPADDING", (0, 0), (-1, -1), 12),
    ("BOTTOMPADDING", (0, 0), (-1, -1), 10),
]))
story.append(header)
story.append(Spacer(1, 5 * mm))

story.append(Paragraph("Punto de partida", heading))
story.append(Paragraph(
    "Se tomó como base el commit <b>23ba2cd - Centro el contenido principal</b>, "
    "último commit de mposse-bit incluido en la rama.", body
))

story.append(Paragraph("Qué cambiamos", heading))
changes = [
    ("1", "<b>Integración:</b> unimos los cambios locales con los cinco commits nuevos de mposse-bit."),
    ("2", "<b>Estilo visual:</b> movimos el CSS a WEB, ordenamos tarjetas, formularios, navegación y pie de página."),
    ("3", "<b>Identidad:</b> aplicamos la paleta azul del logo, un fondo degradado y el logo en el encabezado."),
    ("4", "<b>Catálogo:</b> conservamos las 24 categorías, pero dejamos solamente productos tecnológicos."),
    ("5", "<b>Imágenes:</b> agregamos imágenes uniformes para laptops, celulares, tablets, auriculares y smartwatches."),
]

rows = []
for number, text in changes:
    rows.append([
        Paragraph(f"<b>{number}</b>", ParagraphStyle("Number", parent=body, textColor=white, alignment=1)),
        Paragraph(text, body),
    ])

table = Table(rows, colWidths=[12 * mm, 146 * mm], rowHeights=[18 * mm] * len(rows))
table.setStyle(TableStyle([
    ("BACKGROUND", (0, 0), (0, -1), HexColor("#315F87")),
    ("BACKGROUND", (1, 0), (1, -1), HexColor("#EDF5FC")),
    ("VALIGN", (0, 0), (-1, -1), "MIDDLE"),
    ("LEFTPADDING", (1, 0), (1, -1), 10),
    ("RIGHTPADDING", (1, 0), (1, -1), 10),
    ("GRID", (0, 0), (-1, -1), 0.5, HexColor("#B9CCE0")),
]))
story.append(table)

story.append(Paragraph("Resultado", heading))
story.append(Paragraph(
    "La web mantiene su estructura simple de HTML y CSS, pero ahora tiene una identidad visual consistente "
    "y un catálogo centrado en tecnología.", body
))

doc.build(story)
print(output)
