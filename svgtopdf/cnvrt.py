from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF, renderPM
import glob

filename = "".join(glob.glob('*.svg'))

draw = svg2rlg(filename)
renderPDF.drawToFile(draw, filename.replace('.svg', '').replace('.SVG', '') + ".pdf")
renderPM.drawToFile(draw, filename.replace('.svg', '').replace('.SVG', '') + ".png", fmt="PNG")