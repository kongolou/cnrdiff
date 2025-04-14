from PySide6.QtWidgets import QApplication, QMainWindow, QFileDialog, QMessageBox
from PySide6.QtCore import QDateTime, Slot
from ui_mainwindow import Ui_MainWindow
import sys
import os
import cnrdiff


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)

        self.dateTimeEditStartTime.setDateTime(QDateTime.currentDateTimeUtc())
        self.dateTimeEditEndTime.setDateTime(QDateTime.currentDateTimeUtc())

    @Slot()
    def on_pushButtonAddFile_clicked(self):
        fpath, _ = QFileDialog.getOpenFileName(self, "Select File")
        self.listWidgetInput.addItem(fpath)

    @Slot()
    def on_pushButtonRemoveFile_clicked(self):
        self.listWidgetInput.takeItem(self.listWidgetInput.currentRow())

    @Slot()
    def on_comboBoxInputFileType_currentIndexChanged(self):
        self.checkBoxElevationCutoff.setEnabled(self.comboBoxInputFileType.currentText() == "BNC QC LOG")

    @Slot()
    def on_checkBoxStartTime_toggled(self):
        self.dateTimeEditStartTime.setEnabled(self.checkBoxStartTime.isChecked())

    @Slot()
    def on_checkBoxEndTime_toggled(self):
        self.dateTimeEditEndTime.setEnabled(self.checkBoxEndTime.isChecked())

    @Slot()
    def on_checkBoxInterval_toggled(self):
        self.doubleSpinBoxInterval.setEnabled(self.checkBoxInterval.isChecked())

    @Slot()
    def on_checkBoxElevationCutoff_toggled(self):
        self.doubleSpinBoxElevationCutoff.setEnabled(self.checkBoxElevationCutoff.isChecked())

    def shouldOutputDirectoryEnabled(self):
        if self.checkBoxExportCNR.isChecked() or self.checkBoxExportDCNR.isChecked() or self.checkBoxExportXLSX.isChecked():
            self.lineEditOutputDirectory.setEnabled(True)
            self.pushButtonSelect.setEnabled(True)
        else:
            self.lineEditOutputDirectory.setEnabled(False)
            self.pushButtonSelect.setEnabled(False)

    @Slot()
    def on_checkBoxExportCNR_toggled(self):
        self.shouldOutputDirectoryEnabled()

    @Slot()
    def on_checkBoxExportDCNR_toggled(self):
        self.shouldOutputDirectoryEnabled()

    @Slot()
    def on_checkBoxExportXLSX_toggled(self):
        self.shouldOutputDirectoryEnabled()

    @Slot()
    def on_pushButtonSelect_clicked(self):
        directory = QFileDialog.getExistingDirectory(self, "Select Directory")
        self.lineEditOutputDirectory.setText(directory)

    @Slot()
    def on_pushButtonProcess_clicked(self):
        if not (self.pushButtonSelect.isEnabled() or self.checkBoxPlotDCNR.isChecked()):
            return

        self.pushButtonProcess.setEnabled(False)

        try:
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
                self.doubleSpinBoxElevationCutoff.value()
                if self.checkBoxElevationCutoff.isChecked()
                else 0.0
            )

            inpflist, cnrflist, dcnrflist = [], [], []
            for i in range(self.listWidgetInput.count()):
                inpflist.append(self.listWidgetInput.item(i).text())
                inpfname = os.path.basename(inpflist[-1])
                cnrflist.append(
                    os.path.join(self.lineEditOutputDirectory.text(), inpfname + ".cnr")
                )
                dcnrflist.append(
                    os.path.join(self.lineEditOutputDirectory.text(), inpfname + ".cnr.dcnr")
                )

            xlsxfpath = os.path.join(
                self.lineEditOutputDirectory.text(), "summary.cnr.dcnr.xlsx"
            )

            savecnr = cnrflist if self.checkBoxExportCNR.isChecked() else False
            savedcnr = dcnrflist if self.checkBoxExportDCNR.isChecked() else False
            plotdcnr = self.checkBoxPlotDCNR.isChecked()
            savexlsx = self.checkBoxExportXLSX.isChecked()

            inpftype = self.comboBoxInputFileType.currentText()
            how = self.comboBoxHow.currentText()
            by = self.comboBoxBy.currentText()

            match inpftype:
                case "RINEX V3 OBS":
                    cnr = cnrdiff.rnx2cnr(
                        inpflist, savecnr, start, end, interval, ele_cut
                    )
                case "BNC QC LOG":
                    cnr = cnrdiff.log2cnr(
                        inpflist, savecnr, start, end, interval, ele_cut
                    )

            dcnr = cnrdiff.cnr2dcnr(cnr, savedcnr, plotdcnr, how.upper(), by.upper())

            if savexlsx:
                cnrdiff.dcnr2xlsx([dcnr], xlsxfpath)

        except Exception as e:
            QMessageBox.warning(None, "Error", f"Error: {str(e)}")

        else:
            QMessageBox.information(None, "Success", "Process completed successfully.")

        self.pushButtonProcess.setEnabled(True)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())
