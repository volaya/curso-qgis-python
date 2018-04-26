
from qgis.PyQt.QtWidgets import QMessageBox, QPushButton, QLineEdit
from qgis.PyQt.QtCore import *
import urllib

def my_form_open(dialog, layer, feature):
	button = dialog.findChild(QPushButton,"btnValidate")

	def validate(): 
		wikipediaField = dialog.findChild(QLineEdit,"wikipedia")
		value = wikipediaField.text()
		if value:			
			url = "https://en.wikipedia.org/wiki/" + value
			try:
				urllib.request.urlopen(url)
				QMessageBox.information(dialog, "Validar", "La entrada de wikipedia especificada es válida")
			except urllib.error.HTTPError:
				QMessageBox.warning(dialog, "Validar", "No existe la entrada de wikipedia especificada")				

	def findWidget(w, name):
		for sub in w.children():
			if sub.objectName() == name:
				return sub
			else:
				ret = findWidget(sub, name)
				if ret is not None:
					return ret
	btn = findWidget(dialog, "btnValidate")
	btn.clicked.connect(validate)