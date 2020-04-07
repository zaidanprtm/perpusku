
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from LoginController import LoginControl
from AdminView import AdminView_Window

class LoginAdmin_Window(object):

    def __init__(self):
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()

        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(521, 498)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(60, 40, 391, 211))
        self.label.setObjectName("label")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(140, 290, 241, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(140, 380, 241, 31))
        self.lineEdit_2.setEchoMode(QtWidgets.QLineEdit.Password)
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(170, 250, 171, 31))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(150, 340, 231, 31))
        self.label_3.setObjectName("label_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(220, 420, 81, 31))
        self.pushButton.setObjectName("pushButton")
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
        MainWindow.setWindowTitle(_translate("MainWindow", "LoginAdmin"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p align=\"center\"><span style=\" font-size:20pt; font-weight:600;\">Selamat datang di Perpusku</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Masukkan NIP Anda:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Masukkan password Anda:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Login"))
        self.pushButton.clicked.connect(lambda: self.pushAdminView(MainWindow))

    def pushAdminView(self, MainWindow):
        nip = self.lineEdit.text()
        password = self.lineEdit_2.text()
        if LoginControl().checkloginAdmin(nip,password):
            self.adminview = AdminView_Window(nip)
            MainWindow.close()
        else:
            self.ErrorLogin()

    def ErrorLogin(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Login Error!")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("NIP atau password yang Anda masukkan salah!")
        msg.exec_()

            


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = LoginAdmin_Window()
    sys.exit(app.exec_())
