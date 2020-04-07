from Buku import Buku

class TambahBukuController:
    def __init__ (self):
        pass

    def tambahBuku(self,idbuku,judul,pengarang,tahun,jumlah):
        buku = Buku()
        return buku.addBuku(idbuku,judul,pengarang,tahun,jumlah)

