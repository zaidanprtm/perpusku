import pymongo

myclient = pymongo.MongoClient("mongodb://localhost:27017/")

mydb = myclient["databaseperpus"]
#Membuat tabel buku"
colbuku = mydb["buku"]
lisbuku = [
  { "_id": 1, "Judul Buku": "Calculus", "Pengarang": "Edwin P", "Tahun Terbit": "2011", "Jumlah": "4"},
  { "_id": 2, "Judul Buku": "Algoritma Sederhana", "Pengarang": "Smith G", "Tahun Terbit": "2013", "Jumlah": "5"},
  { "_id": 3, "Judul Buku": "Astronomi", "Pengarang": "Nanik K", "Tahun Terbit": "2007", "Jumlah": "6"}
]

x = colbuku.insert_many(lisbuku)
print(x.inserted_ids)

#Membuat tabel user
coluser = mydb["user"]
lisuser = [
  { "_id": 1313618013, "Password": "passuser1", "Nama": "user1", "Prodi": "Ilmu Komputer"},
  { "_id": 1313618102, "Password": "passuser2", "Nama": "user2", "Prodi": "Teknik Komputer"}
]

y = coluser.insert_many(lisuser)
print(y.inserted_ids)

#Membuat tabel admin
coladmin = mydb["admin"]
lisadmin = [
  { "_id": 101, "Password": "passadmin1", "Nama": "admin1"},
  { "_id": 102, "Password": "passadmin2", "Nama": "admin2"}
]

z = coladmin.insert_many(lisadmin)
print(z.inserted_ids)

for x in colbuku.find():
  print(x)
for y in coluser.find():
  print(y)
for z in coladmin.find():
  print(z)
