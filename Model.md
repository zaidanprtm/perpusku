## Penjelasan Model

Dalam aplikasi ini terdapat 3 model, yaitu:

### Buku
Model ini adalah model yang berhubungan dengan collection buku. Berfungsi sebagai data buku yang tersedia di perpustakaan. Pada model ini, datanya meliputi: ```id buku, judul buku, pengarang, tahun terbit, jumlah```. Terdapat fungsi untuk mencari data buku berdasarkan judul, menambah buku baru ke database, mengurangi jumlah buku yang sudah tersedia, menambah jumlah buku yang sudah tersedia, dan melihat semua buku.

### Admin
Model ini adalah model yang berhubungan dengan collection admin. Berfungsi sebagai data admin. Pada model ini, datanya meliputi: ```idadmin(NIP), password, nama```. Terdapat fungsi untuk mencari NIP admin,, menambah admin, mencari data admin berdasarkaan id, mencari data nama admin berdasarkan id, mencari data password admin berdasarkan id, dan melihat semua admin.

### User
Model ini adalah model yang berhubungan dengan collection user. Berfungsi sebagai data user. Pada model ini, datanya meliputi: ```iduser(NIM), password, nama, prodi```. Terdapat fungsi unutk mencari NIM user, mencari data user berdasarkan id, menambah user, mencari data user berdasarkan id, mencari password user berdasarkan id, mencari prodi berdasarkan id user, dan melihat semua user. 
