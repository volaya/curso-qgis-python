layer = iface.activeLayer()
features = layer.getFeatures()
totalPopulation = 0
for feat in features:
	pop = feat["pop_est"]
	if pop > 0:
		totalPopulation += pop

print (totalPopulation)

##################

layer = iface.activeLayer()
features = layer.getFeatures()
totalPopulation = {}
for feat in features:
	pop = feat["pop_est"]
	continent = feat["continent"]
	if pop > 0:
		if continent in totalPopulation:
			totalPopulation[continent] += pop
		else:
			totalPopulation[continent] = pop
print (totalPopulation)


#####


from qgis.PyQt.QtCore import QVariant

def hemisphere(geom):
	box = geom.boundingBox()
	if box.yMinimum() > 0 and box.yMaximum() > 0:
		return "N"
	if box.yMinimum() <= 0 and box.yMaximum() <= 0:
		return "S"
	else:
		return "A"

layer = iface.activeLayer()
provider = layer.dataProvider()
provider.addAttributes([QgsField("hemisphere", QVariant.String)])
layer.updateFields()
idxField = layer.fieldNameIndex("hemisphere")
features = layer.getFeatures()

for feat in features:
	geom = feat.geometry()            
	hemi = hemisphere(geom)
	provider.changeAttributeValues({feat.id() : {idxField: hemi}})
