from PySide6.QtWidgets import QApplication, QMainWindow
from mainwindow import MainWindow
import sys


def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    main()
