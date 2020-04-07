from Buku import Buku
from User import User

class UserController:
    def __init__ (self,nim):
        self.user = User(nim)
        pass

    def showNIM(self):
        return self.user.getNIM()

    def showName(self,nim):
        return self.user.getName(nim)

    def showProdi(self,nim):
        return self.user.getProdi(nim)

    def cariBuku(self,judul):
        buku = Buku()
        return buku.getBuku(judul)

    def pinjamBuku(self,judul):
        buku = Buku()
        return buku.kurangjumlahBuku(judul)

    def lihatsemuaBuku(self):
        buku = Buku()
        return buku.getallBuku()
