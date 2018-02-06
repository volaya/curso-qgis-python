from qgis.core import *
from qgis.gui import *

@qgsfunction(args="auto", group="Custom", usesgeometry=True)
def hemisphere(geom):
	box = geom.boundingBox()
	if box.yMinimum() > 0 and box.yMaximum() > 0:
		return "N"
	if box.yMinimum() <= 0 and box.yMaximum() <= 0:
		return "S"
	else:
		return "B"

## usar expresión para color