# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowuKdhFq.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QDateTime, QMetaObject, QRect
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QDoubleSpinBox,
    QGroupBox,
    QLabel,
    QListView,
    QProgressBar,
    QPushButton,
    QWidget,
    QFileDialog,
    QMessageBox,
)

# my code begin
import cnrdiff
import os

# my code end


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName("MainWindow")
        MainWindow.resize(640, 480)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxInput = QGroupBox(self.centralwidget)
        self.groupBoxInput.setObjectName("groupBoxInput")
        self.groupBoxInput.setGeometry(QRect(20, 200, 601, 251))
        self.listViewInput = QListView(self.groupBoxInput)
        self.listViewInput.setObjectName("listViewInput")
        self.listViewInput.setGeometry(QRect(20, 70, 561, 161))
        self.labelFileType = QLabel(self.groupBoxInput)
        self.labelFileType.setObjectName("labelFileType")
        self.labelFileType.setGeometry(QRect(40, 30, 61, 31))
        self.comboBoxFileType = QComboBox(self.groupBoxInput)
        self.comboBoxFileType.setObjectName("comboBoxFileType")
        self.comboBoxFileType.setGeometry(QRect(100, 30, 161, 31))
        self.labelSolutionMode = QLabel(self.groupBoxInput)
        self.labelSolutionMode.setObjectName("labelSolutionMode")
        self.labelSolutionMode.setGeometry(QRect(290, 30, 81, 31))
        self.comboBoxSolutionMode = QComboBox(self.groupBoxInput)
        self.comboBoxSolutionMode.setObjectName("comboBoxSolutionMode")
        self.comboBoxSolutionMode.setGeometry(QRect(380, 30, 81, 31))
        self.pushButtonAddFile = QPushButton(self.groupBoxInput)
        self.pushButtonAddFile.setObjectName("pushButtonAddFile")
        self.pushButtonAddFile.setGeometry(QRect(490, 30, 31, 31))
        self.pushButtonRemoveFile = QPushButton(self.groupBoxInput)
        self.pushButtonRemoveFile.setObjectName("pushButtonRemoveFile")
        self.pushButtonRemoveFile.setGeometry(QRect(530, 30, 31, 31))
        self.groupBoxOptions = QGroupBox(self.centralwidget)
        self.groupBoxOptions.setObjectName("groupBoxOptions")
        self.groupBoxOptions.setGeometry(QRect(20, 20, 281, 171))
        self.checkBoxStartTime = QCheckBox(self.groupBoxOptions)
        self.checkBoxStartTime.setObjectName("checkBoxStartTime")
        self.checkBoxStartTime.setGeometry(QRect(20, 30, 81, 31))
        self.checkBoxEndTime = QCheckBox(self.groupBoxOptions)
        self.checkBoxEndTime.setObjectName("checkBoxEndTime")
        self.checkBoxEndTime.setGeometry(QRect(20, 60, 81, 31))
        self.checkBoxInterval = QCheckBox(self.groupBoxOptions)
        self.checkBoxInterval.setObjectName("checkBoxInterval")
        self.checkBoxInterval.setGeometry(QRect(20, 90, 151, 31))
        self.checkBoxCutOff = QCheckBox(self.groupBoxOptions)
        self.checkBoxCutOff.setObjectName("checkBoxCutOff")
        self.checkBoxCutOff.setGeometry(QRect(20, 120, 151, 31))
        self.dateTimeEditStartTime = QDateTimeEdit(self.groupBoxOptions)
        self.dateTimeEditStartTime.setObjectName("dateTimeEditStartTime")
        self.dateTimeEditStartTime.setGeometry(QRect(100, 30, 161, 31))
        self.dateTimeEditEndTime = QDateTimeEdit(self.groupBoxOptions)
        self.dateTimeEditEndTime.setObjectName("dateTimeEditEndTime")
        self.dateTimeEditEndTime.setGeometry(QRect(100, 60, 161, 31))
        self.doubleSpinBoxInterval = QDoubleSpinBox(self.groupBoxOptions)
        self.doubleSpinBoxInterval.setObjectName("doubleSpinBoxInterval")
        self.doubleSpinBoxInterval.setGeometry(QRect(170, 90, 91, 31))
        self.doubleSpinBoxCutOff = QDoubleSpinBox(self.groupBoxOptions)
        self.doubleSpinBoxCutOff.setObjectName("doubleSpinBoxCutOff")
        self.doubleSpinBoxCutOff.setGeometry(QRect(170, 120, 91, 31))
        self.groupBoxOutput = QGroupBox(self.centralwidget)
        self.groupBoxOutput.setObjectName("groupBoxOutput")
        self.groupBoxOutput.setGeometry(QRect(320, 20, 301, 171))
        self.checkBoxExportCNR = QCheckBox(self.groupBoxOutput)
        self.checkBoxExportCNR.setObjectName("checkBoxExportCNR")
        self.checkBoxExportCNR.setGeometry(QRect(40, 30, 101, 31))
        self.pushButtonProcess = QPushButton(self.groupBoxOutput)
        self.pushButtonProcess.setObjectName("pushButtonProcess")
        self.pushButtonProcess.setGeometry(QRect(160, 90, 101, 31))
        self.checkBoxPlotDCNR = QCheckBox(self.groupBoxOutput)
        self.checkBoxPlotDCNR.setObjectName("checkBoxPlotDCNR")
        self.checkBoxPlotDCNR.setGeometry(QRect(40, 90, 101, 31))
        self.checkBoxExportDCNR = QCheckBox(self.groupBoxOutput)
        self.checkBoxExportDCNR.setObjectName("checkBoxExportDCNR")
        self.checkBoxExportDCNR.setGeometry(QRect(40, 60, 101, 31))
        self.checkBoxExportHTML = QCheckBox(self.groupBoxOutput)
        self.checkBoxExportHTML.setObjectName("checkBoxExportHTML")
        self.checkBoxExportHTML.setGeometry(QRect(160, 60, 101, 31))
        self.checkBoxExportXLSX = QCheckBox(self.groupBoxOutput)
        self.checkBoxExportXLSX.setObjectName("checkBoxExportXLSX")
        self.checkBoxExportXLSX.setGeometry(QRect(160, 30, 101, 31))
        self.progressBarProcess = QProgressBar(self.groupBoxOutput)
        self.progressBarProcess.setObjectName("progressBarProcess")
        self.progressBarProcess.setGeometry(QRect(40, 130, 221, 21))
        self.progressBarProcess.setValue(0)
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.checkBoxStartTime, self.checkBoxEndTime)
        QWidget.setTabOrder(self.checkBoxEndTime, self.checkBoxInterval)
        QWidget.setTabOrder(self.checkBoxInterval, self.checkBoxCutOff)
        QWidget.setTabOrder(self.checkBoxCutOff, self.dateTimeEditStartTime)
        QWidget.setTabOrder(self.dateTimeEditStartTime, self.dateTimeEditEndTime)
        QWidget.setTabOrder(self.dateTimeEditEndTime, self.doubleSpinBoxInterval)
        QWidget.setTabOrder(self.doubleSpinBoxInterval, self.doubleSpinBoxCutOff)
        QWidget.setTabOrder(self.doubleSpinBoxCutOff, self.comboBoxFileType)
        QWidget.setTabOrder(self.comboBoxFileType, self.comboBoxSolutionMode)
        QWidget.setTabOrder(self.comboBoxSolutionMode, self.pushButtonAddFile)
        QWidget.setTabOrder(self.pushButtonAddFile, self.pushButtonRemoveFile)
        QWidget.setTabOrder(self.pushButtonRemoveFile, self.listViewInput)
        QWidget.setTabOrder(self.listViewInput, self.checkBoxExportCNR)
        QWidget.setTabOrder(self.checkBoxExportCNR, self.checkBoxExportDCNR)
        QWidget.setTabOrder(self.checkBoxExportDCNR, self.checkBoxPlotDCNR)
        QWidget.setTabOrder(self.checkBoxPlotDCNR, self.checkBoxExportXLSX)
        QWidget.setTabOrder(self.checkBoxExportXLSX, self.checkBoxExportHTML)
        QWidget.setTabOrder(self.checkBoxExportHTML, self.pushButtonProcess)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

        # my code begin
        self.comboBoxFileType.addItems(["BNC QC LOG", "RINEX V3 OBS"])
        self.comboBoxSolutionMode.addItems(["Mean", "Max"])
        self.doubleSpinBoxInterval.setValue(1.0)
        self.doubleSpinBoxCutOff.setRange(0.0, 90.0)
        self.dateTimeEditStartTime.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEditEndTime.setDateTime(QDateTime.currentDateTime())

        self.standardItemModelInput = QStandardItemModel()
        self.listViewInput.setModel(self.standardItemModelInput)

        self.checkBoxStartTime.setChecked(True)
        self.checkBoxEndTime.setChecked(True)
        self.checkBoxInterval.setChecked(True)
        self.checkBoxCutOff.setChecked(True)

        self.checkBoxExportCNR.setChecked(False)
        self.checkBoxExportDCNR.setChecked(False)
        self.checkBoxExportXLSX.setChecked(False)
        self.checkBoxPlotDCNR.setChecked(False)
        self.checkBoxExportHTML.setChecked(False)

        self.pushButtonAddFile.clicked.connect(self.on_pushButtonAddFile_clicked)
        self.pushButtonRemoveFile.clicked.connect(self.on_pushButtonRemoveFile_clicked)
        self.pushButtonProcess.clicked.connect(self.on_pushButtonProcess_clicked)
        self.checkBoxStartTime.toggled.connect(self.on_checkBoxStartTime_toggled)
        self.checkBoxEndTime.toggled.connect(self.on_checkBoxEndTime_toggled)
        self.checkBoxInterval.toggled.connect(self.on_checkBoxInterval_toggled)
        self.checkBoxCutOff.toggled.connect(self.on_checkBoxCutOff_toggled)

        # my code end

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "CNRDIFF V1.0", None)
        )
        self.groupBoxInput.setTitle(
            QCoreApplication.translate("MainWindow", "Input", None)
        )
        self.labelFileType.setText(
            QCoreApplication.translate("MainWindow", "File Type", None)
        )
        self.labelSolutionMode.setText(
            QCoreApplication.translate("MainWindow", "Solution Mode", None)
        )
        self.pushButtonAddFile.setText(
            QCoreApplication.translate("MainWindow", "+", None)
        )
        self.pushButtonRemoveFile.setText(
            QCoreApplication.translate("MainWindow", "-", None)
        )
        self.groupBoxOptions.setTitle(
            QCoreApplication.translate("MainWindow", "Options", None)
        )
        self.checkBoxStartTime.setText(
            QCoreApplication.translate("MainWindow", "Start Time", None)
        )
        self.checkBoxEndTime.setText(
            QCoreApplication.translate("MainWindow", "End Time", None)
        )
        self.checkBoxInterval.setText(
            QCoreApplication.translate("MainWindow", "Interval", None)
        )
        self.checkBoxCutOff.setText(
            QCoreApplication.translate("MainWindow", "Elevation angle cut-off", None)
        )
        self.groupBoxOutput.setTitle(
            QCoreApplication.translate("MainWindow", "Output", None)
        )
        self.checkBoxExportCNR.setText(
            QCoreApplication.translate("MainWindow", "Export CNR", None)
        )
        self.pushButtonProcess.setText(
            QCoreApplication.translate("MainWindow", "Process", None)
        )
        self.checkBoxPlotDCNR.setText(
            QCoreApplication.translate("MainWindow", "Plot DCNR", None)
        )
        self.checkBoxExportDCNR.setText(
            QCoreApplication.translate("MainWindow", "Export DCNR", None)
        )
        self.checkBoxExportHTML.setText(
            QCoreApplication.translate("MainWindow", "Export HTML", None)
        )
        self.checkBoxExportXLSX.setText(
            QCoreApplication.translate("MainWindow", "Export XLSX", None)
        )

    # retranslateUi

    # my code begin
    def on_pushButtonAddFile_clicked(self):
        fpath, _ = QFileDialog.getOpenFileName(
            None, "选择文件", "", "All Files (*)", ""
        )
        self.standardItemModelInput.appendRow(QStandardItem(fpath))

    def on_pushButtonRemoveFile_clicked(self):
        for i in self.listViewInput.selectedIndexes():
            self.standardItemModelInput.removeRow(i.row())

    def on_pushButtonProcess_clicked(self):
        try:
            self.progressBarProcess.setValue(20)

            inpflist = [
                self.standardItemModelInput.item(i).text()
                for i in range(self.standardItemModelInput.rowCount())
            ]
            savecnr = self.checkBoxExportCNR.isChecked()
            start = (
                self.dateTimeEditStartTime.dateTime().toPython()
                if self.checkBoxStartTime.isChecked()
                else None
            )
            end = (
                self.dateTimeEditEndTime.dateTime().toPython()
                if self.checkBoxEndTime.isChecked()
                else None
            )
            interval = (
                self.doubleSpinBoxInterval.value()
                if self.checkBoxInterval.isChecked()
                else None
            )
            ecut = (
                self.doubleSpinBoxCutOff.value()
                if self.checkBoxCutOff.isChecked()
                else 0.0
            )

            savedcnr = self.checkBoxExportDCNR.isChecked()
            slnmode = self.comboBoxSolutionMode.currentText()
            plotdcnr = self.checkBoxPlotDCNR.isChecked()

            savexlsx = self.checkBoxExportXLSX.isChecked()
            savehtml = self.checkBoxExportHTML.isChecked()

            inpftype = self.comboBoxFileType.currentText()
            match inpftype:
                case "BNC QC LOG":
                    cnr = cnrdiff.log2cnr(inpflist, savecnr, start, end, interval, ecut)
                case "RINEX V3 OBS":
                    cnr = cnrdiff.rnx2cnr(inpflist, savecnr, start, end, interval, ecut)

            self.progressBarProcess.setValue(50)

            dcnr = cnrdiff.cnr2dcnr(cnr, savedcnr, slnmode, plotdcnr)

            self.progressBarProcess.setValue(80)

            if savexlsx:
                xlsxfpath = os.path.join(os.getcwd(), "report.xlsx")
                cnrdiff.dcnr2xlsx([dcnr], xlsxfpath, slnmode)

            if savehtml:
                htmlfpath = os.path.join(os.getcwd(), "report.html")
                cnrdiff.dcnr2html([dcnr], htmlfpath, slnmode)

            self.progressBarProcess.setValue(100)

        except Exception as e:
            self.messageBox = QMessageBox()
            self.messageBox.setText(str(e))
            self.messageBox.show()
            self.progressBarProcess.setValue(0)

    def on_checkBoxStartTime_toggled(self, checked):
        self.dateTimeEditStartTime.setEnabled(checked)

    def on_checkBoxEndTime_toggled(self, checked):
        self.dateTimeEditEndTime.setEnabled(checked)

    def on_checkBoxInterval_toggled(self, checked):
        self.doubleSpinBoxInterval.setEnabled(checked)

    def on_checkBoxCutOff_toggled(self, checked):
        self.doubleSpinBoxCutOff.setEnabled(checked)

    # my code end
