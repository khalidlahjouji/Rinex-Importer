import os
import shutil
import math
from qgis.PyQt.QtWidgets import QFileDialog, QMessageBox, QProgressBar,QAction
from qgis.core import (QgsVectorLayer, QgsField, QgsFeature, QgsGeometry, QgsPointXY, QgsProject)
from PyQt5.QtCore import QVariant
from qgis.PyQt.QtGui import QIcon


class RinexImporter:
    def __init__(self, iface):
        self.iface = iface
        self.progress_bar = None
    def initGui(self):
        """Ajoute le plugin à l'interface QGIS"""
        
        icon_path = os.path.join(os.path.dirname(__file__), "icon.png")
        self.action = QAction(QIcon(icon_path), "Importer RINEX", self.iface.mainWindow())
        self.iface.addPluginToMenu("&RINEX Importer", self.action)
        self.iface.addToolBarIcon(self.action)
        self.action.triggered.connect(self.run)
        self.iface.addToolBarIcon(self.action)
        self.iface.addPluginToMenu("&RINEX Importer", self.action)

    def unload(self):
        """Supprime le plugin de l'interface"""
        self.iface.removeToolBarIcon(self.action)
        self.iface.removePluginMenu("&RINEX Importer", self.action)

    def run(self):
        """Exécute le plugin (ouvre la boîte de dialogue)"""
        from .rinex_importer_dialog import RinexImporterDialog
        self.dlg = RinexImporterDialog()
        self.dlg.show()
    