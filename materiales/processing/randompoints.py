from qgis.PyQt.QtCore import QCoreApplication, QVariant
from qgis.core import (QgsField, QgsFeature, QgsFeatureSink, QgsFeatureRequest, 
                        QgsProcessing, QgsProcessingAlgorithm, QgsProcessingParameterFeatureSource, 
                        QgsProcessingParameterFeatureSink, QgsProcessingParameterNumber,
                        QgsProcessingParameterExtent, QgsProcessingParameterCrs, QgsFields,
                        QgsWkbTypes, QgsGeometry, QgsPointXY)
import random

class RandomPointsAlgorithm(QgsProcessingAlgorithm):
    EXTENT = 'EXTENT'
    COUNT = 'COUNT'
    OUTPUT = 'OUTPUT'
    CRS = "CRS"
 
    def __init__(self):
        super().__init__()
 
    def name(self):
        return "randompoints"
     
    def tr(self, text):
        return QCoreApplication.translate("randompoints", text)
         
    def displayName(self):
        return self.tr("Random Points")
 
    def group(self):
        return self.tr("Examples")
 
    def groupId(self):
        return "examples"
 
    def shortHelpString(self):
        return self.tr("Creates a layer with random points")
 
    def helpUrl(self):
        return "https://qgis.org"
         
    def createInstance(self):
        return type(self)()
   
    def initAlgorithm(self, config=None):
        self.addParameter(QgsProcessingParameterNumber(
            self.COUNT,
            self.tr("Point count"),
            QgsProcessingParameterNumber.Integer,
            1, False, 1, 1000000000))
        self.addParameter(QgsProcessingParameterExtent(
            self.EXTENT,
            self.tr("Extent")))
        self.addParameter(QgsProcessingParameterCrs(
            self.CRS,
            self.tr("Crs")))
        self.addParameter(QgsProcessingParameterFeatureSink(
            self.OUTPUT,
            self.tr("Output layer"),
            QgsProcessing.TypeVectorPoint))
 
    def processAlgorithm(self, parameters, context, feedback):
        extent = self.parameterAsExtent(parameters, self.EXTENT, context)
        count = int(self.parameterAsDouble(parameters, self.COUNT, context))
        crs = self.parameterAsCrs(parameters, self.CRS, context)

        fields = QgsFields()
        fields.append(QgsField('id', QVariant.Int, '', 10, 0))

        (sink, dest_id) = self.parameterAsSink(parameters, self.OUTPUT, context, fields, 
                                                QgsWkbTypes.Point, crs)
 
        for i in range(count):
            f = QgsFeature()
            f.setGeometry(QgsGeometry.fromPointXY(QgsPointXY(
                random.uniform(extent.xMinimum(), extent.xMaximum()),
                random.uniform(extent.yMinimum(), extent.yMaximum()))))
            f.setGeometry(f.geometry())
            f.setAttributes([i])
            sink.addFeature(f, QgsFeatureSink.FastInsert)
 
        return {self.OUTPUT: dest_id}