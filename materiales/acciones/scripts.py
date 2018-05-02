import urllib
import webbrowser  

url = "https://en.wikipedia.org/wiki/" + "[%wikipedia%]"
try:
	urllib.request.urlopen(url)
	webbrowser.open(url, new=0, autoraise=True)
except:
	QtGui.QMessageBox.warning(None, "Wrong value", "The corresponding Wikipedia page does not exist")
	

