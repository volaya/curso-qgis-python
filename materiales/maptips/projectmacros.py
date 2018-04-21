def openProject():
	from qgis.utils import iface
	from qgis.gui import QgsMessageBar
	from qgis.core import Qgis
	iface.messageBar().pushMessage(
		"Warning",
		"This project contains classified data. Don't distribute it",
		Qgis.Warning,
		10
	)
