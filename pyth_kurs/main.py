from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow

import sys

def application():
    app = QApplication(sys.argv)
    w = QMainWindow()

    w.setWindowTitle("Простая программа")
    w.setGeometry(500, 200, 350, 200)

    w.show()
    sys.exit(app.exec_())

if __name__ == "__main__":
    application()
