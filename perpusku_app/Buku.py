import pymongo

class Buku:
    def __init__(self, idbuku = None):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["databaseperpus"]
        self.colbuku = mydb["buku"]
        if idbuku :
            self.idbuku = idbuku
            self.judul = self.colbuku.find({"_id" : idbuku})["Judul Buku"]
        
    def getBuku(self,judul):
        carijudul = self.colbuku.find_one({"Judul Buku" : judul}, {"_id" : 0, "Judul Buku": 1, "Pengarang": 1, "Tahun Terbit" : 1, "Jumlah" : 1})
        if carijudul == None:
            return None
        return carijudul

    def addBuku(self,idbuku,judul,pengarang,tahun,jumlah):
        dict_buku = {"_id" : idbuku, "Judul Buku" : judul, "Pengarang": pengarang, "Tahun Terbit" : tahun, "Jumlah" : jumlah}
        return self.colbuku.insert_one(dict_buku)
    

    def kurangjumlahBuku(self,judul):
        byjudul = {"Judul Buku": judul}
        jumlahnow = self.colbuku.find_one(byjudul)
        valuejumlah= int((jumlahnow['Jumlah']))
        jumlahupdate = {"$set": { "Jumlah" : valuejumlah - 1 }}
        return self.colbuku.update_one(jumlahnow, jumlahupdate)

    def tambahjumlahBuku(self,judul):
        byjudul = {"Judul Buku": judul}
        jumlahnow = self.colbuku.find_one(byjudul)
        valuejumlah= int((jumlahnow['Jumlah']))
        jumlahupdate = {"$set": { "Jumlah" : valuejumlah + 1 }}
        return self.colbuku.update_one(jumlahnow, jumlahupdate)

    def getallBuku(self):
        lisbuku = []
        for x in self.colbuku.find({},{"_id" : 0, "Judul Buku": 1, "Pengarang": 1, "Tahun Terbit" : 1, "Jumlah" : 1}):
           lisbuku.append(x)
        return lisbuku
    

    
if __name__ == "__main__":
    model = Buku()
    print(model.getBuku("Astronomi"))
##    model.deljumlahBuku("Astronomi")
    print(model.getallBuku())






























   

    

    
        
