
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from LoginUserView import LoginUser_Window
from LoginAdminView import LoginAdmin_Window

class LoginAs_Window(object):
    def __init__(self):
        MainWindow = QtWidgets.QMainWindow()
        self.setupUi(MainWindow)
        MainWindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 497)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(70, 40, 391, 211))
        self.label.setObjectName("label")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(154, 250, 221, 41))
        self.pushButton.setObjectName("pushButton")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(154, 320, 221, 41))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 521, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LoginAs"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Selamat datang di Perpusku</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Login sebagai User"))
        self.pushButton_2.setText(_translate("MainWindow", "Login sebagai Admin"))
        self.pushButton.clicked.connect(lambda: self.pushLoginUser(MainWindow))
        self.pushButton_2.clicked.connect(lambda: self.pushLoginAdmin(MainWindow))
        
    def pushLoginUser(self, MainWindow):
        self.loginuser = LoginUser_Window()
        MainWindow.close()
        
    def pushLoginAdmin(self, MainWindow):
        self.loginadmin = LoginAdmin_Window()
        MainWindow.close()
        
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = LoginAs_Window()
    sys.exit(app.exec_())
