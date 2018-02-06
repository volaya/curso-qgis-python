from PyQt4.QtCore import *
from PyQt4.QtGui import *
import urllib
 
def formOpen(dialog,layerid,featureid):
	buttonBox = dialog.findChild(QDialogButtonBox,"buttonBox")

	def validate(): 
		wikipediaField = dialog.findChild(QLineEdit,"wikipedia")
		value = wikipediaField.text()
		print value
		if not value:
			wikipediaField.setStyleSheet("QLineEdit{background: yellow}")
		else:
			url = "https://en.wikipedia.org/wiki/" + value
			response = urllib.urlopen(url).getcode()
			print response
			if str(response) == "404":
				wikipediaField.setStyleSheet("QLineEdit{background: yellow}")
			else:
				dialog.accept()

	buttonBox.accepted.disconnect(dialog.accept)
	buttonBox.accepted.connect(validate)
	buttonBox.rejected.connect(dialog.reject)
 


