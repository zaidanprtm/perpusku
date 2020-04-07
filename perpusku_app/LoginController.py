import pymongo

from User import User
from Admin import Admin

class LoginControl:
    def __init__ (self):
        pass

    def checkloginUser(self,iduser,password):
        user = User(int(iduser))
        if user.getPassword() == password:
            return True
        return False

    def checkloginAdmin(self,idadmin,password):
        admin = Admin(int(idadmin))
        if admin.getPassword() == password:
            return True
        return False

##NIM = input("Masukkan NIM: ")
##password = input("Masukkan Password: ")
##
##print(LoginControl().checkloginUser(NIM,password))
##
##NIP = input("Masukkan NIP: ")
##password = input("Masukkan Password: ")
##
##print(LoginControl().checkloginAdmin(NIP,password))
