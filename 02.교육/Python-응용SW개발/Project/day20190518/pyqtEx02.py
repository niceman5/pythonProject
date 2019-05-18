import sys
from PyQt5.QtWidgets import *
from PyQt5.QtCore import *

class Form(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setupUI()

    def setupUI(self):
        self.setWindowTitle('Test')
        self.setGeometry(200,200,300,300)   # x,y,x길이,y길이
        btn1 = QPushButton('Click1', self)
        btn2 = QPushButton('Click2', self)
        btn3 = QPushButton('Click3', self)

        btn1.move(30,30)
        btn2.move(30,60)
        btn3.move(30,90)

        btn1.clicked.connect(self.btn1_clicked)
        btn2.clicked.connect(self.btn2_clicked)
        btn3.clicked.connect(QCoreApplication.instance().quit)


    def btn1_clicked(self):
        QMessageBox.about(self, 'message', 'clicked')

    def btn2_clicked(self):
        print('Buttin2 Clicked!!!')


if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = Form()
    # window.setupUI()
    window.show()
    app.exec_()
