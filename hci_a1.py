# COMP 3020 Assignment 1, Question II (b)
# Joshua Chan 7722727
# Josh Lemer

import sys
from PyQt4.QtGui import *
from PyQt4 import QtGui

app = QApplication(sys.argv)

def okevent():
    print("ok")
    sys.exit()
    
def cancelevent():
    print("cancel")
    sys.exit()

offScreen = -9999999
buttonYCord = 80
gap = 5
    
window = QWidget()
window.setWindowTitle("Properties Window")

advisoryImage = QtGui.QLabel("",window)
advisoryImage.setPixmap(QPixmap("advisory.jpg"))
advisoryImage.move(20,20)

textlabel = QtGui.QLabel("Invalid property value",window)
textlabel.move(30 + advisoryImage.sizeHint().width(),27)
detailString = "The provided fildter string is invalid. The filter\nstring should contain a description of the filter,\nfollowed by the vertical bar (|) and the filter\npattern. The strings for different filtering options\nshould also be separated by the vertical bar.\nExample:\"Text files(*.txt)|*.txt|All files\n(*.*)|*.*\""
detaillabel = QtGui.QLabel(detailString,window)
detaillabel.move(0,offScreen)


detailbutton = QPushButton("D&etails",window)
detailYCord = buttonYCord + detailbutton.sizeHint().height() + gap
hidden = 0
windowHeightNormal = 115
windowWidth = 310
window.setFixedSize(windowWidth,windowHeightNormal)
def toggle():
    global hidden
    if hidden == 0:
        detaillabel.move(7,detailYCord)
        window.setFixedSize(windowWidth,windowHeightNormal + detaillabel.sizeHint().height() + 5)
        hidden = 1
    else:
        detaillabel.move(offScreen,offScreen)
        window.setFixedSize(windowWidth,windowHeightNormal)
        hidden = 0

okbutton = QPushButton("Ok",window)
cancelbutton = QPushButton("Cancel",window)
okbutton.clicked.connect(okevent)
cancelbutton.clicked.connect(cancelevent)
detailbutton.clicked.connect(toggle)


okXCord = detailbutton.sizeHint().width() + gap*4
cancelXCord = okXCord + gap + okbutton.sizeHint().width()
detailbutton.move(5,buttonYCord)
okbutton.move(okXCord,buttonYCord)
cancelbutton.move(cancelXCord,buttonYCord)

window.show()
sys.exit(app.exec_())