import pymongo

class Admin:
    def __init__(self,idadmin = None):
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["databaseperpus"]
        self.coladmin = mydb["admin"]
        if idadmin:
            self.idadmin = idadmin

    def getNIP(self):
       return self.idadmin

    def addAdmin(self,idadmin,password,nama):
        dict_admin = {"_id":int(idadmin), "Password":password, "Nama":nama}
        return self.coladmin.insert_one(dict_admin)

    def getdataAdmin(self):
        return self.coladmin.find_one({'_id':self.idadmin})

    def getName(self,idadmin):
        carinama = self.coladmin.find_one({'_id':int(idadmin)})
        if carinama == None:
            return None
        return carinama['Nama']

    def setName(self,newnama):
        byid = {"_id": self.idadmin}
        setnamabaru = {"$set":{"Nama":newnama}}
        return self.coladmin.update_one(byid,setnamabaru)

    def getPassword(self):
        caripass = self.coladmin.find_one({'_id':self.idadmin})
        if caripass == None:
            return None
        return caripass['Password']

    def setpassword(self, newpassword):
        byid = {"_id": self.idadmin}
        setpassbaru = {"$set": {"Password": newpassword}}
        return self.coladmin.update_one(byid, setpassbaru)

    def getallAdmin(self):
        lisadmin = []
        for x in self.coladmin.find({},{"Password" : 0}):
            lisadmin.append(x)
        return lisadmin


    


    
