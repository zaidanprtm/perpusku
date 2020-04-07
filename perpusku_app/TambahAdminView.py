
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from AdminVController import AdminController


class TambahAdmin_Window(object):
    
    def __init__(self,nip):
        self.admincontroller = AdminController(nip)
        self.alladmin = self.admincontroller.lihatsemuaAdmin()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(784, 334)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(10, 130, 81, 21))
        self.label_4.setObjectName("label_4")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(10, 180, 81, 21))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(330, 70, 431, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(10, 70, 61, 16))
        self.label_2.setObjectName("label_2")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(10, 20, 231, 31))
        self.label.setObjectName("label")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(120, 130, 161, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(120, 70, 161, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(490, 20, 141, 21))
        self.label_6.setObjectName("label_6")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(120, 180, 161, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(90, 230, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 784, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TambahAdmin"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Password:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Nama:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">NIP:</span></p></body></html>"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Masukkan data admin di bawah ini:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Admin yang terdaftar:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Tambah"))
        self.pushButton.clicked.connect(lambda: self.pushtambahAdmin(MainWindow))
        for i in self.alladmin:
            namaall = i['Nama']
            nipall = i['_id']
            isisemua = 'Nama: ' + str(namaall) +' <<<|||>>> '+  'NIP: ' + str(nipall)
            self.textBrowser.append(isisemua)

    def pushtambahAdmin(self,MainWindow):
        idadmin = self.lineEdit.text()
        password = self.lineEdit_2.text()
        nama = self.lineEdit_3.text()
        self.tambahadmin = self.admincontroller.tambahAdmin(idadmin,password,nama)
        self.SuccessPopup()
        isitambahan = 'Nama: ' + str(nama) +  ' <<<|||>>> ' + 'NIP: ' + str(idadmin)
        self.textBrowser.append(isitambahan)

    def SuccessPopup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Berhasil!")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Penambahan admin baru berhasil!")
        msg.exec_()


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = TambahAdmin_Window()
    sys.exit(app.exec_())
