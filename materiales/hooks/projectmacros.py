from qgis.utils import iface
from qgis.gui import QgsMessageBar
from qgis.core import Qgis

def openProject():
	iface.messageBar().pushMessage(
		"Warning",
		"This project contains classified data. Don't distribute it",
		Qgis.Warning,
		10
	)

from qgis.core import QgsProject
import shutil
from subprocess import call

REPO_FOLDER = "repo_folder"
def saveProject():
	projFile = QgsProject.instance().fileName()
	scope = QgsExpressionContextUtils.projectScope()
	if not scope.hasVariable(REPO_FOLDER):
			return
		call("git pull".split(" "))
		
		repoFolder = scope.variable(REPO_FOLDER):
		destFile = os.path.join(repoFolder, os.path.basename(projFile))
		shutil.copyfile(projFile, destFile)

		call("git add .".split(" "))
		call("git commit -m 'updated QGIS project file'".split(" "))
		call("git push".split(" "))
