from Admin import Admin

class TambahAdminController:
    def __init__ (self):
        pass

    def tambahAdmin(self,idadmin,password,nama):
        admin = Admin()
        return admin.addAdmin(iduser,password,nama)

    def lihatsemuaAdmin(self):
        admin = Admin()
        return admin.getallAdmin()
