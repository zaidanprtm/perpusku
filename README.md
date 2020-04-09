# perpusku
Aplikasi desktop untuk perpustakaan. Digunakan untuk user dan admin yang memiliki fungsi masing-masing.

### Requirement
- Python 3.5+
- MongoDB
- Library Python : pymongo dan pyqt5

### Fitur
User:
- Cari buku berdasarkan judul
- Pinjam buku yang sudah dicari
- Melihat seluruh buku yang tersedia

Admin:
- Cari buku berdasarkan judul
- Tambah jumlah/amount buku yang sudah dicari
- Melihat seluruh buku yang tersedia
- Tambah akun baru untuk user
- Tambah akun baru untuk admin
- Tambah buku baru

### How to use
1. Unduh/clone repository ini.
2. Install python, MongoDB, dan library yang diperlukan. Untuk library dapat diinstall melalui cmd: ```pip install <nama library>``` 
3. Jalankan script ```createdatabase.py``` terlebih dahulu untuk membuat database. Jalankan hanya waktu pertama kali penggunaan karena setelahnya database berarti sudah terbuat.
4. Jalankan script ```main.py``` pada folder perpusku_app.
5. Login menggunakan akun yang tersedia pada ```daftarakun.txt``` 
6. Gunakan fitur-fitur yang tersedia baik bagi Admin atau User.
7. Untuk buku yang baru saja ditambahkan untuk melihat pada daftar buku yang tersedia harus restart app terlebih dahulu.
