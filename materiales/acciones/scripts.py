import urllib
import webbrowser  

url = "https://en.wikipedia.org/wiki/" + "[%wikipedia%]"
if urllib.request.urlopen(url).getcode() == 404:
	QtGui.QMessageBox.warning(None, "Wrong value", "The corresponding Wikipedia page does not exist")
else:
	webbrowser.open(url, new=0, autoraise=True)

