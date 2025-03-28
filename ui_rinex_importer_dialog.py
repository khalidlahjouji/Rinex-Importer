# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'rinex_importer_dialog_base.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.

from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_RinexImporterDialog(object):
    def setupUi(self, RinexImporterDialog):
        RinexImporterDialog.setObjectName("RinexImporterDialog")
        RinexImporterDialog.resize(450, 150)

        self.verticalLayout = QtWidgets.QVBoxLayout(RinexImporterDialog)
        self.verticalLayout.setObjectName("verticalLayout")

        # Titre
        self.lblTitle = QtWidgets.QLabel(RinexImporterDialog)
        self.lblTitle.setObjectName("lblTitle")
        self.verticalLayout.addWidget(self.lblTitle)

        # Zone de sélection du dossier
        
        self.horizontalLayout = QtWidgets.QHBoxLayout()
        self.horizontalLayout.setObjectName("horizontalLayout")
        
        self.lblFolderPath = QtWidgets.QLabel(RinexImporterDialog)
        self.lblFolderPath.setObjectName("lblFolderPath")
        self.lblFolderPath.setEnabled(True)
        
        self.horizontalLayout.addWidget(self.lblFolderPath)
        
        self.txtFolderPath = QtWidgets.QLineEdit(RinexImporterDialog)
        self.txtFolderPath.setObjectName("txtFolderPath")
        self.txtFolderPath.setReadOnly(True)  # Lecture seule
        
        self.horizontalLayout.addWidget(self.txtFolderPath)

        self.btnSelectFolder = QtWidgets.QPushButton(RinexImporterDialog)
        self.btnSelectFolder.setObjectName("btnSelectFolder")
        self.horizontalLayout.addWidget(self.btnSelectFolder)

        self.verticalLayout.addLayout(self.horizontalLayout)

        # Bouton Importer
        self.btnImport = QtWidgets.QPushButton(RinexImporterDialog)
        self.btnImport.setObjectName("btnImport")
        self.verticalLayout.addWidget(self.btnImport)

        self.retranslateUi(RinexImporterDialog)
        QtCore.QMetaObject.connectSlotsByName(RinexImporterDialog)

    def retranslateUi(self, RinexImporterDialog):
        _translate = QtCore.QCoreApplication.translate
        RinexImporterDialog.setWindowTitle(_translate("RinexImporterDialog", "Importer des fichiers RINEX"))
        self.lblTitle.setText(_translate("RinexImporterDialog", "Sélectionner un dossier contenant des fichiers RINEX :"))  
        self.txtFolderPath.setPlaceholderText(_translate("RinexImporterDialog", "Aucun dossier sélectionné"))
        self.btnSelectFolder.setText(_translate("RinexImporterDialog", "Parcourir..."))
        self.btnImport.setText(_translate("RinexImporterDialog", "Importer"))
