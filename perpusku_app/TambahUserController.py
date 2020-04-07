from User import User

class TambahUserController:
    def __init__ (self):
        pass

    def tambahUser(self,iduser,password,nama,prodi):
        user = User()
        return user.addUser(iduser,password,nama,prodi)

    def lihatsemuaUser(self):
        user = User()
        return user.getallUser()
