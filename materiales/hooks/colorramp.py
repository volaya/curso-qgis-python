import os
from qgis.core import *
from qgis.PyQt.QtGui import QColor
from processing.core.outputs import OutputVector, OutputRaster, OutputFile

NUM_INTERVALS = 5

def createStyle(layer):
	areas = [f["area"] for f in layer.getFeatures()]
	minarea = min(areas)
	maxarea = max(areas)
	interval = (maxarea - minarea) / NUM_INTERVALS
	colorInterval = 255 / NUM_INTERVALS
	
	ranges = []
	for i in xrange(NUM_INTERVALS):		
		symbol = QgsSymbolV2.defaultSymbol(layer.geometryType())
		value = 255- colorInterval * i
		symbol.setColor(QColor(value, value, value))
		rng = QgsRendererRangeV2(minarea + interval * i, minarea + interval * (i + 1), symbol, "class " + str(i+1))
		ranges.append(rng)

	renderer = QgsGraduatedSymbolRendererV2("area", ranges)
	layer.setRendererV2(renderer)
	source = layer.source()
	styleFile = os.path.splitext(layer.source())[0] + ".qml"
	layer.saveNamedStyle(styleFile)

for output in alg.outputs:
	print output.value
	if isinstance(output, (OutputVector)):
		dirname, basename = os.path.split(output.value)
		layer = QgsVectorLayer(output.value, "layer", "ogr")
		fields = [f.name().lower() for f in layer.fields()]
		if "area" in fields:
			createStyle(layer)


		