# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindowtBAEFP.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import QCoreApplication, QDateTime, QMetaObject, QRect, QSize
from PySide6.QtGui import QFont, QIcon, QStandardItemModel, QStandardItem
from PySide6.QtWidgets import (
    QCheckBox,
    QComboBox,
    QDateTimeEdit,
    QDoubleSpinBox,
    QGroupBox,
    QLabel,
    QLineEdit,
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
        # MainWindow.resize(640, 480)
        MainWindow.setFixedSize(QSize(640, 480))  # my code
        icon = QIcon()
        icon.addFile("cnrdiff-logo.svg", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.groupBoxInput = QGroupBox(self.centralwidget)
        self.groupBoxInput.setObjectName("groupBoxInput")
        self.groupBoxInput.setGeometry(QRect(20, 200, 601, 251))
        self.listViewInput = QListView(self.groupBoxInput)
        self.listViewInput.setObjectName("listViewInput")
        self.listViewInput.setGeometry(QRect(20, 70, 561, 161))
        font = QFont()
        font.setPointSize(11)
        self.listViewInput.setFont(font)
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
        self.groupBoxOptions.setGeometry(QRect(20, 20, 291, 171))
        self.checkBoxStartTime = QCheckBox(self.groupBoxOptions)
        self.checkBoxStartTime.setObjectName("checkBoxStartTime")
        self.checkBoxStartTime.setGeometry(QRect(20, 30, 81, 31))
        self.checkBoxEndTime = QCheckBox(self.groupBoxOptions)
        self.checkBoxEndTime.setObjectName("checkBoxEndTime")
        self.checkBoxEndTime.setGeometry(QRect(20, 60, 81, 31))
        self.checkBoxInterval = QCheckBox(self.groupBoxOptions)
        self.checkBoxInterval.setObjectName("checkBoxInterval")
        self.checkBoxInterval.setGeometry(QRect(20, 90, 151, 31))
        self.checkBoxCutoff = QCheckBox(self.groupBoxOptions)
        self.checkBoxCutoff.setObjectName("checkBoxCutoff")
        self.checkBoxCutoff.setGeometry(QRect(20, 120, 151, 31))
        self.dateTimeEditStartTime = QDateTimeEdit(self.groupBoxOptions)
        self.dateTimeEditStartTime.setObjectName("dateTimeEditStartTime")
        self.dateTimeEditStartTime.setGeometry(QRect(100, 30, 171, 31))
        self.dateTimeEditStartTime.setCalendarPopup(True)
        self.dateTimeEditEndTime = QDateTimeEdit(self.groupBoxOptions)
        self.dateTimeEditEndTime.setObjectName("dateTimeEditEndTime")
        self.dateTimeEditEndTime.setGeometry(QRect(100, 60, 171, 31))
        self.dateTimeEditEndTime.setCalendarPopup(True)
        self.doubleSpinBoxInterval = QDoubleSpinBox(self.groupBoxOptions)
        self.doubleSpinBoxInterval.setObjectName("doubleSpinBoxInterval")
        self.doubleSpinBoxInterval.setGeometry(QRect(170, 90, 101, 31))
        self.doubleSpinBoxInterval.setDecimals(3)
        self.doubleSpinBoxInterval.setMaximum(60.000000000000000)
        self.doubleSpinBoxInterval.setValue(1.000000000000000)
        self.doubleSpinBoxCutoff = QDoubleSpinBox(self.groupBoxOptions)
        self.doubleSpinBoxCutoff.setObjectName("doubleSpinBoxCutoff")
        self.doubleSpinBoxCutoff.setGeometry(QRect(170, 120, 101, 31))
        self.doubleSpinBoxCutoff.setDecimals(3)
        self.doubleSpinBoxCutoff.setMaximum(90.000000000000000)
        self.doubleSpinBoxCutoff.setSingleStep(10.000000000000000)
        self.groupBoxOutput = QGroupBox(self.centralwidget)
        self.groupBoxOutput.setObjectName("groupBoxOutput")
        self.groupBoxOutput.setGeometry(QRect(330, 20, 291, 171))
        self.checkBoxExportCNR = QCheckBox(self.groupBoxOutput)
        self.checkBoxExportCNR.setObjectName("checkBoxExportCNR")
        self.checkBoxExportCNR.setGeometry(QRect(40, 60, 101, 31))
        self.pushButtonProcess = QPushButton(self.groupBoxOutput)
        self.pushButtonProcess.setObjectName("pushButtonProcess")
        self.pushButtonProcess.setGeometry(QRect(150, 90, 101, 31))
        self.checkBoxPlotDCNR = QCheckBox(self.groupBoxOutput)
        self.checkBoxPlotDCNR.setObjectName("checkBoxPlotDCNR")
        self.checkBoxPlotDCNR.setGeometry(QRect(40, 90, 101, 31))
        self.checkBoxExportDCNR = QCheckBox(self.groupBoxOutput)
        self.checkBoxExportDCNR.setObjectName("checkBoxExportDCNR")
        self.checkBoxExportDCNR.setGeometry(QRect(150, 60, 101, 31))
        self.progressBarProcess = QProgressBar(self.groupBoxOutput)
        self.progressBarProcess.setObjectName("progressBarProcess")
        self.progressBarProcess.setGeometry(QRect(20, 120, 251, 31))
        self.progressBarProcess.setValue(0)
        self.labelOutDir = QLabel(self.groupBoxOutput)
        self.labelOutDir.setObjectName("labelOutDir")
        self.labelOutDir.setGeometry(QRect(20, 30, 51, 31))
        self.lineEditOutDir = QLineEdit(self.groupBoxOutput)
        self.lineEditOutDir.setObjectName("lineEditOutDir")
        self.lineEditOutDir.setGeometry(QRect(70, 30, 161, 31))
        self.pushButtonOutDir = QPushButton(self.groupBoxOutput)
        self.pushButtonOutDir.setObjectName("pushButtonOutDir")
        self.pushButtonOutDir.setGeometry(QRect(240, 30, 31, 31))
        MainWindow.setCentralWidget(self.centralwidget)
        QWidget.setTabOrder(self.checkBoxStartTime, self.checkBoxEndTime)
        QWidget.setTabOrder(self.checkBoxEndTime, self.checkBoxInterval)
        QWidget.setTabOrder(self.checkBoxInterval, self.checkBoxCutoff)
        QWidget.setTabOrder(self.checkBoxCutoff, self.dateTimeEditStartTime)
        QWidget.setTabOrder(self.dateTimeEditStartTime, self.dateTimeEditEndTime)
        QWidget.setTabOrder(self.dateTimeEditEndTime, self.doubleSpinBoxInterval)
        QWidget.setTabOrder(self.doubleSpinBoxInterval, self.doubleSpinBoxCutoff)
        QWidget.setTabOrder(self.doubleSpinBoxCutoff, self.comboBoxFileType)
        QWidget.setTabOrder(self.comboBoxFileType, self.comboBoxSolutionMode)
        QWidget.setTabOrder(self.comboBoxSolutionMode, self.pushButtonAddFile)
        QWidget.setTabOrder(self.pushButtonAddFile, self.pushButtonRemoveFile)
        QWidget.setTabOrder(self.pushButtonRemoveFile, self.listViewInput)
        QWidget.setTabOrder(self.listViewInput, self.lineEditOutDir)
        QWidget.setTabOrder(self.lineEditOutDir, self.pushButtonOutDir)
        QWidget.setTabOrder(self.pushButtonOutDir, self.checkBoxExportCNR)
        QWidget.setTabOrder(self.checkBoxExportCNR, self.checkBoxExportDCNR)
        QWidget.setTabOrder(self.checkBoxExportDCNR, self.checkBoxPlotDCNR)
        QWidget.setTabOrder(self.checkBoxPlotDCNR, self.pushButtonProcess)

        # my code begin
        self.comboBoxFileType.addItems(["BNC QC LOG", "RINEX V3 OBS"])
        self.comboBoxSolutionMode.addItems(["Mean", "Max"])
        self.dateTimeEditStartTime.setDateTime(QDateTime.currentDateTime())
        self.dateTimeEditEndTime.setDateTime(QDateTime.currentDateTime())
        self.lineEditOutDir.setText(os.path.expanduser("~"))

        self.standardItemModelInput = QStandardItemModel()
        self.listViewInput.setModel(self.standardItemModelInput)

        self.pushButtonAddFile.clicked.connect(self.on_pushButtonAddFile_clicked)
        self.pushButtonRemoveFile.clicked.connect(self.on_pushButtonRemoveFile_clicked)
        self.pushButtonOutDir.clicked.connect(self.on_pushButtonOutDir_clicked)
        self.pushButtonProcess.clicked.connect(self.on_pushButtonProcess_clicked)

        self.checkBoxStartTime.toggled.connect(self.on_checkBoxStartTime_toggled)
        self.checkBoxEndTime.toggled.connect(self.on_checkBoxEndTime_toggled)
        self.checkBoxInterval.toggled.connect(self.on_checkBoxInterval_toggled)
        self.checkBoxCutoff.toggled.connect(self.on_checkBoxCutOff_toggled)

        # my code end

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)

    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(
            QCoreApplication.translate("MainWindow", "CNRDIFF V1.1", None)
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
        self.checkBoxCutoff.setText(
            QCoreApplication.translate("MainWindow", "Elevation angle cut-off", None)
        )
        self.dateTimeEditStartTime.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "yyyy-MM-dd HH:mm:ss.zzz", None)
        )
        self.dateTimeEditEndTime.setDisplayFormat(
            QCoreApplication.translate("MainWindow", "yyyy-MM-dd HH:mm:ss.zzz", None)
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
        self.labelOutDir.setText(
            QCoreApplication.translate("MainWindow", "OutDir:", None)
        )
        self.pushButtonOutDir.setText(
            QCoreApplication.translate("MainWindow", "...", None)
        )

    # retranslateUi

    # my code begin
    def on_pushButtonAddFile_clicked(self):
        fpath, _ = QFileDialog.getOpenFileName(
            None, "Select File", "", "All Files (*)", ""
        )
        self.standardItemModelInput.appendRow(QStandardItem(fpath))

    def on_pushButtonRemoveFile_clicked(self):
        self.standardItemModelInput.removeRows(self.listViewInput.selectedIndexes())

    def on_pushButtonOutDir_clicked(self):
        self.lineEditOutDir.setText(
            QFileDialog.getExistingDirectory(
                None, "Select Directory", "", QFileDialog.ShowDirsOnly
            )
        )

    def on_pushButtonProcess_clicked(self):
        try:
            self.progressBarProcess.setValue(20)

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
            ele_cut = (
                self.doubleSpinBoxCutoff.value()
                if self.checkBoxCutoff.isChecked()
                else 0.0
            )

            inpflist, cnrflist, dcnrflist = [], [], []
            for i in range(self.standardItemModelInput.rowCount()):
                inpflist.append(self.standardItemModelInput.item(i).text())
                inpfname = os.path.basename(inpflist[-1])
                cnrflist.append(
                    os.path.join(self.lineEditOutDir.text(), inpfname + ".cnr")
                )
                dcnrflist.append(
                    os.path.join(self.lineEditOutDir.text(), inpfname + ".dcnr")
                )

            savecnr = cnrflist if self.checkBoxExportCNR.isChecked() else False
            savedcnr = dcnrflist if self.checkBoxExportDCNR.isChecked() else False
            plotdcnr = self.checkBoxPlotDCNR.isChecked()

            inpftype = self.comboBoxFileType.currentText()
            slnmode = self.comboBoxSolutionMode.currentText()
            match inpftype:
                case "BNC QC LOG":
                    cnr = cnrdiff.log2cnr(
                        inpflist, savecnr, start, end, interval, ele_cut
                    )
                case "RINEX V3 OBS":
                    cnr = cnrdiff.rnx2cnr(
                        inpflist, savecnr, start, end, interval, ele_cut
                    )

            self.progressBarProcess.setValue(50)

            cnrdiff.cnr2dcnr(cnr, savedcnr, slnmode, plotdcnr)

            self.progressBarProcess.setValue(100)

        except Exception as e:
            QMessageBox.warning(None, "Error", str(e))
            self.progressBarProcess.setValue(0)

    def on_checkBoxStartTime_toggled(self, checked):
        self.dateTimeEditStartTime.setEnabled(checked)

    def on_checkBoxEndTime_toggled(self, checked):
        self.dateTimeEditEndTime.setEnabled(checked)

    def on_checkBoxInterval_toggled(self, checked):
        self.doubleSpinBoxInterval.setEnabled(checked)

    def on_checkBoxCutOff_toggled(self, checked):
        self.doubleSpinBoxCutoff.setEnabled(checked)

    # my code end
