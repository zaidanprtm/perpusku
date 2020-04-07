
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from AdminVController import AdminController


class TambahUser_Window(object):
    
    def __init__(self,nip):
        self.admincontroller = AdminController(nip)
        self.alluser = self.admincontroller.lihatsemuaUser()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()
        
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 348)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 30, 221, 31))
        self.label.setObjectName("label")
        self.lineEdit_5 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_5.setGeometry(QtCore.QRect(130, 250, 161, 21))
        self.lineEdit_5.setObjectName("lineEdit_5")
        self.lineEdit_3 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_3.setGeometry(QtCore.QRect(130, 190, 161, 21))
        self.lineEdit_3.setObjectName("lineEdit_3")
        self.lineEdit_2 = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit_2.setGeometry(QtCore.QRect(130, 140, 161, 21))
        self.lineEdit_2.setObjectName("lineEdit_2")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(20, 190, 81, 21))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(20, 140, 81, 21))
        self.label_4.setObjectName("label_4")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(130, 80, 161, 21))
        self.lineEdit.setObjectName("lineEdit")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(20, 240, 91, 31))
        self.label_5.setObjectName("label_5")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(20, 80, 61, 16))
        self.label_2.setObjectName("label_2")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(340, 80, 431, 221))
        self.textBrowser.setObjectName("textBrowser")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 30, 141, 21))
        self.label_6.setObjectName("label_6")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(100, 280, 75, 23))
        self.pushButton.setObjectName("pushButton")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "TambahUser"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Masukkan data user di bawah ini:</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Nama:</span></p></body></html>"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Password:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Prodi:</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">NIM:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">User yang terdaftar:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Tambah"))
        self.pushButton.clicked.connect(lambda: self.pushtambahUser(MainWindow))
        for i in self.alluser:
            namaall = i['Nama']
            nimall =  i['_id']
            prodiall = i['Prodi']
            isisemua = 'Nama: ' + str(namaall) + ' <<<|||>>> ' + ' NIM: ' + str(nimall) + ' <<<|||>>> ' + ' Prodi: ' + str(prodiall)
            self.textBrowser.append(isisemua)

    def pushtambahUser(self,MainWindow):
        iduser = self.lineEdit.text()
        password = self.lineEdit_2.text()
        nama = self.lineEdit_3.text()
        prodi = self.lineEdit_5.text()
        self.tambahadmin = self.admincontroller.tambahUser(iduser,password,nama,prodi)
        isitambahan = 'Nama: ' + str(nama) + ' <<<|||>>> ' + ' NIM: ' + str(iduser) + ' <<<|||>>> ' + ' Prodi: ' + str(prodi)
        self.textBrowser.append(isitambahan)
        self.SuccessPopup()

    def SuccessPopup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Berhasil!")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Penambahan user baru berhasil!")
        msg.exec_()

if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = TambahUser_Window()
    sys.exit(app.exec_())
