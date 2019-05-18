import sys
from PyQt5.QtWidgets import *

app = QApplication(sys.argv)

# print(sys.argv)

label = QLabel("Test~~~~")
label.show()

print('Before')
app.exec_()
print('after')
