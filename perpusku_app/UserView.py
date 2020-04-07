
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from UserVController import UserController

class UserView_Window(object):

    def __init__(self,nim):
        self.usercontroller = UserController(nim)
        self.nim = self.usercontroller.showNIM()
        self.name = self.usercontroller.showName(self.nim)
        self.prodi = self.usercontroller.showProdi(self.nim)
        self.allbuku = self.usercontroller.lihatsemuaBuku()
        self.MainWindow = QtWidgets.QMainWindow()
        self.setupUi(self.MainWindow)
        self.MainWindow.show()
    
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(807, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 161, 31))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(500, 20, 131, 31))
        self.label_2.setObjectName("label_2")
        self.lineEdit = QtWidgets.QLineEdit(self.centralwidget)
        self.lineEdit.setGeometry(QtCore.QRect(440, 90, 171, 31))
        self.lineEdit.setObjectName("lineEdit")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(410, 50, 311, 31))
        self.label_3.setObjectName("label_3")
        self.textBrowser = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser.setGeometry(QtCore.QRect(380, 170, 401, 71))
        self.textBrowser.setObjectName("textBrowser")
        self.textBrowser_5 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_5.setGeometry(QtCore.QRect(30, 320, 751, 231))
        self.textBrowser_5.setObjectName("textBrowser_5")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(630, 90, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(530, 140, 121, 21))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(320, 280, 171, 31))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(20, 60, 41, 21))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(20, 100, 41, 21))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(20, 140, 51, 31))
        self.label_8.setObjectName("label_8")
        self.textBrowser_2 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_2.setGeometry(QtCore.QRect(70, 60, 141, 31))
        self.textBrowser_2.setObjectName("textBrowser_2")
        self.textBrowser_3 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_3.setGeometry(QtCore.QRect(70, 100, 141, 31))
        self.textBrowser_3.setObjectName("textBrowser_3")
        self.textBrowser_4 = QtWidgets.QTextBrowser(self.centralwidget)
        self.textBrowser_4.setGeometry(QtCore.QRect(70, 140, 141, 31))
        self.textBrowser_4.setObjectName("textBrowser_4")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(550, 250, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 807, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "UserView"))
        self.label.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt; font-weight:600;\">Selamat datang!</span></p></body></html>"))
        self.label_2.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Pencarian Buku</span></p></body></html>"))
        self.label_3.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Masukkan judul buku yang ingin Anda cari:</span></p></body></html>"))
        self.pushButton.setText(_translate("MainWindow", "Cari"))
        self.label_4.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:12pt;\">Hasil pencarian:</span></p></body></html>"))
        self.label_5.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:14pt;\">Buku yang tersedia:</span></p></body></html>"))
        self.label_6.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Nama:</span></p></body></html>"))
        self.label_7.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">Prodi:</span></p></body></html>"))
        self.label_8.setText(_translate("MainWindow", "<html><head/><body><p><span style=\" font-size:11pt;\">NIM:</span></p></body></html>"))
        self.pushButton_2.setText(_translate("MainWindow", "Pinjam"))
        self.pushButton.clicked.connect(lambda: self.pushcariBuku(MainWindow))
        self.pushButton_2.clicked.connect(lambda: self.pushpinjamBuku(MainWindow))
        self.textBrowser_2.append(self.name)
        self.textBrowser_3.append(self.prodi)
        self.textBrowser_4.append(self.nim)
        for i in self.allbuku:
            judulall = i['Judul Buku']
            pengarangall = i['Pengarang']
            tahunall = i['Tahun Terbit']
            jumlahall = i['Jumlah']
            isisemua = 'Judul Buku: ' + str(judulall) + ' ||| Pengarang: ' + str(pengarangall) + ' ||| Tahun Terbit: ' + str(tahunall) + ' ||| Jumlah: ' + str(jumlahall)
            self.textBrowser_5.append(isisemua)

    def pushcariBuku(self,MainWindow):
        judulcari = self.lineEdit.text()
        buku = self.usercontroller.cariBuku(judulcari)
        if buku == None:
            self.ErrorSearch()
        else:
            judul = buku['Judul Buku']
            pengarang = buku['Pengarang']
            tahun = buku['Tahun Terbit']
            jumlah = buku['Jumlah']
            isijudul = 'Judul Buku: ' + str(judul)
            isipengarang = 'Pengarang: ' + str(pengarang)
            isitahun = 'Tahun Terbit: ' + str(tahun)
            isijumlah = 'Jumlah: ' + str(jumlah)
            self.textBrowser.append(isijudul)
            self.textBrowser.append(isipengarang)
            self.textBrowser.append(isitahun)
            self.textBrowser.append(isijumlah)

    def pushpinjamBuku(self,MainWindow):
        judul = self.lineEdit.text()
        self.pinjambuku = self.usercontroller.pinjamBuku(judul)
        self.SuccessPopup()
        
    def ErrorSearch(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Pencarian Error!")
        msg.setIcon(QtWidgets.QMessageBox.Critical)
        msg.setText("Judul tidak ditemukan!")
        msg.exec_()

    def SuccessPopup(self):
        msg = QtWidgets.QMessageBox()
        msg.setWindowTitle("Berhasil!")
        msg.setIcon(QtWidgets.QMessageBox.Information)
        msg.setText("Peminjaman buku berhasil! Silakan temui pustakawan untuk mengambil buku")
        msg.exec_()  


if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ui = UserView_Window()
    sys.exit(app.exec_())
