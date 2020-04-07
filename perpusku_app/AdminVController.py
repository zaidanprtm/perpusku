from Admin import Admin
from Buku import Buku
from User import User

class AdminController:
    def __init__ (self,nip):
        self.admin = Admin(nip)
        self.user = User()
        pass

    def showNIP(self):
        return self.admin.getNIP()

    def showName(self,nip):
        return self.admin.getName(nip)

    def cariBuku(self,judul):
        buku = Buku()
        return buku.getBuku(judul)

    def tambahpcsBuku(self,judul):
        buku = Buku()
        return buku.tambahjumlahBuku(judul)

    def tambahBuku(self,idbuku,judul,pengarang,tahun,jumlah):
        buku = Buku()
        return buku.addBuku(idbuku,judul,pengarang,tahun,jumlah)

    def tambahAdmin(self,idadmin,password,nama):
        return self.admin.addAdmin(idadmin,password,nama)

    def tambahUser(self,iduser,password,nama,prodi):
        return self.user.addUser(iduser,password,nama,prodi)

    def lihatsemuaUser(self):
        return self.user.getallUser()

    def lihatsemuaAdmin(self):
        return self.admin.getallAdmin()

    def lihatsemuaBuku(self):
        buku = Buku()
        return buku.getallBuku()
