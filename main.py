from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow,QDialog
import sys

def add_label():
    print("Push Button")


def application():
    app = QApplication(sys.argv)
    window = QDialog()
    window.setGeometry(400, 400, 400, 400)
    window.setWindowTitle('Hello world')
    main_text = QtWidgets.QLabel(window)
    main_text.setText('Geektech')
    main_text.move(150, 100)

    btn = QtWidgets.QPushButton(window)
    btn.setText('Нажми')
    btn.clicked.connect(add_label)

    window.show()
    sys.exit(app.exec_())

application()