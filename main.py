from PySide6.QtWidgets import QApplication
from mainwindow import MainWindow
import sys
import pyi_splash


def main():
    app = QApplication(sys.argv)
    mainwindow = MainWindow()
    mainwindow.show()
    sys.exit(app.exec())


if __name__ == '__main__':
    pyi_splash.close()
    main()
