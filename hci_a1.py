# COMP 3020 Assignment 1, Question II (b)
# Joshua Chan 7722727
# Josh Lemer 7634755

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

windowHeightNormal = 115
windowWidth = 310
offScreen = -9999999
buttonYCord = 80
gap = 5
hidden = 0
    
window = QWidget()
window.setWindowTitle("Properties Window")
window.setFixedSize(windowWidth,windowHeightNormal)

# Create and place the image
advisoryImage = QtGui.QLabel("",window)
advisoryImage.setPixmap(QPixmap("advisory.jpg"))
advisoryImage.move(20,20)

# Create and place the primary text label
textlabel = QtGui.QLabel("Invalid property value",window)
textlabel.move(30 + advisoryImage.sizeHint().width(),27)

#Create and place the detail text label
detailString = "The provided fildter string is invalid. The filter\nstring should contain a description of the filter,\nfollowed by the vertical bar (|) and the filter\npattern. The strings for different filtering options\nshould also be separated by the vertical bar.\nExample:\"Text files(*.txt)|*.txt|All files\n(*.*)|*.*\""
detaillabel = QtGui.QLabel(detailString,window)
detaillabel.move(0,offScreen)

# Create detail button
detailbutton = QPushButton("D&etails",window)
detailYCord = buttonYCord + detailbutton.sizeHint().height() + gap


# Create ok and cancel buttons
okbutton = QPushButton("Ok",window)
cancelbutton = QPushButton("Cancel",window)
# Connect buttons to functions
okbutton.clicked.connect(okevent)
cancelbutton.clicked.connect(cancelevent)
detailbutton.clicked.connect(toggle)

okXCord = detailbutton.sizeHint().width() + gap*4
cancelXCord = okXCord + gap + okbutton.sizeHint().width()

# Place buttons
detailbutton.move(5,buttonYCord)
okbutton.move(okXCord,buttonYCord)
cancelbutton.move(cancelXCord,buttonYCord)

window.show()
sys.exit(app.exec_())
