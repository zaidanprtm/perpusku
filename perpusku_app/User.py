import pymongo

class User:

    def __init__(self,iduser = None):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["databaseperpus"]
        self.coluser = mydb["user"]
        if iduser:
            self.iduser = iduser

    def getNIM(self):
       return self.iduser

    def addUser(self,iduser,password,nama,prodi):
        dict_user = {"_id":int(iduser), "Password":password, "Nama":nama, "Prodi":prodi}
        return self.coluser.insert_one(dict_user)

    def getdataUser(self):
        return self.coluser.find_one({'_id':self.iduser})

    def getName(self,iduser):
        carinama = self.coluser.find_one({'_id': int(iduser)})
        if carinama == None:
            return None
        return carinama['Nama']

    def setName(self,newnama):
        byid = {"_id": self.iduser}
        setnamabaru = {"$set":{"Nama":newnama}}
        return self.coluser.update_one(byid,setnamabaru)

    def getPassword(self):
        caripass = self.coluser.find_one({'_id':self.iduser})
        if caripass == None:
            return None
        return caripass['Password']

    def setpassword(self, newpassword):
        byid = {"_id": self.iduser}
        setpassbaru = {"$set": {"Password": newpassword}}
        return self.coluser.update_one(byid, setpassbaru)
    
    def getProdi(self,iduser):
        cariprodi = self.coluser.find_one({'_id':int(iduser)})
        if cariprodi == None:
            return None
        return cariprodi['Prodi']

    def setProdi(self,newprodi):
        byid = {"_id": self.iduser}
        setprodibaru = {"$set":{"Prodi":newprodi}}
        return self.coluser.update_one(byid,setprodibaru)

    def getallUser(self):
        lisuser = []
        for x in self.coluser.find({},{"Password" : 0}):
            lisuser.append(x)
        return lisuser

