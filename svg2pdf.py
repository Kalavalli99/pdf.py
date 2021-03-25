from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF

drawing = svg2rlg("Freesample.svg")
renderPDF.drawToFile(drawing, "svg2pdf.pdf")
