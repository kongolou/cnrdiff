from PySide6.QtWidgets import QApplication, QMainWindow
import mainwindow as ui
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = QMainWindow()
    ui = ui.Ui_MainWindow()
    ui.setupUi(window)
    window.show()
    sys.exit(app.exec())
