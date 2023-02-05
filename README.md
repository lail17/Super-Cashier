# Background Project

Andi adalah seorang pemilik supermarket besar di salah satu kota di Indonesia. Andi memiliki rencana untuk melakukan perbaikan proses bisnis, yaitu Andi akan membuat sistem kasir yang self-service di supermarket miliknya. Sehingga customer bisa langsung memasukkan item yang dibeli, jumlah item yang dibeli, dan harga item yang dibeli dan fitur yang lain. Sehingga customer yang tidak berada di kota tersebut bisa membeli barang dari supermarket tersebut. Setelah Andi melakukan riset, ternyata Andi memiliki masalah, yaitu Andi membutuhkan Programmer untuk membuatkan fitur - fitur agar bisa sistem kasir self-service di supermarket itu bisa berjalan dengan lancar.

# Feature Requirements

1.	Membuat ID transaksi. Dilakukan dengan membuat object dari kelas transaksi yang sudah didefinisikan.
2.	Memasukkan data transaksi yang berisi nama, jumlah, dan harga peritem
3.	Mengupdate data transaksi dengan:
    - Update nama, jika terjadi kesalahan saat input nama item.
    - Update jumlah jika terjadi kesalahan saat input jumlah item.
    - Update harga jika terdai kesalahan saat input harga per item.
4.	Membatalkan data transaksi dengan pilihan:
    - Menghapus salah satu item
    - Menghapus semuanya data transaksi
5.	Melakukan pengecekan terhadap data transaksi.
6.	Menghitung total belanja dengan ketentuan diskon sebagai berikut:
    - Jika totalbelanja di atas Rp200.000 maka akan mendapatkan diskon 5%.
    - Jika totalbelanja di atas Rp300.000 maka akan mendapatkan diskon 8%.
    - Jika totalbelanja di atas Rp500.000 maka akan mendapatkan diskon 10%.

# Flowchart

![image](https://user-images.githubusercontent.com/124485986/216821516-bcf99723-720a-4c87-86df-940131b83f6a.png)



# Code (penjelasan tentang fungsinya)

- `class Transaction:` Kelas digunakan untuk menampung method-method yang berisi feature requirements yang dibutuhkan.

- `def __init__(self):`   fungsi untuk menginisialisasi sebuah atribut data pada class Transaction. Pada fungsi ini terdapat satu parameter `self.data_transaksi (dict)` yang merupakan variabel untuk menampung data transaksi customer yang masuk.

- ` def add_item(self, nama, jumlah, harga):`  Fungsi untuk memasukkan item yang ingin dibeli. Dengan input nama, jumlah, dan harga peritem.

- `print_item(self):` Fungsi untuk mencetak item-item yang masuk dengan memberikan input berupa tabulate.

- `update_item_name(self, nama, nama_baru):`  Fungsi untuk mengupdate nama item.

- `update_item_qyt(self, nama, jumlah_baru):`  Fungsi untuk mengupdate jumlah item. 

- `def update_item_price(self, nama, harga_baru):`  Fungsi untuk mengupdate harga per item .

- `def delete_item(self, nama):` Fungsi untuk menghapus salah satu item .

- `def reset_transaction(self):` Fungsi untuk mereset atau menghapus semua data transaksi yang ada.

- ` def check_order(self):`Fungsi untuk mengecek apakah data transaksi yang diinput sudah benar atau belum. Pengecekan dilakukan dengan mengecek apakah nama yang diinput bukan string kosong " " dan jumlah serta harga per item harus dalam tipe data integer. 

- `def total_price(self):`  Fungsi untuk menghitung total belanja yang harus dibayar. 
    Dengan memberikan diskon dengan ketentuan:
    - Jika totalbelanja di atas Rp200.000 maka akan mendapatkan diskon 5%.
    - Jika totalbelanja di atas Rp300.000 maka akan mendapatkan diskon 8%.
    - Jika totalbelanja di atas Rp500.000 maka akan mendapatkan diskon 10%. 







# Test Code

#### Test 1:
Customer ingin menambahkan dua item dengan method `add_item()` kemudian mencetak list data yang sudah masuk dengan `print_item()`

![image](https://user-images.githubusercontent.com/124485986/216821772-794df4cb-7b21-4c15-979a-a3cedc0cbd01.png)

![image](https://user-images.githubusercontent.com/124485986/216821804-aefc14af-28f1-4458-9984-b6519650bff7.png)


#### Test 2:
Customer salah membeli barang, sehingga ingin menghapus item "Pasta Gigi" dengan method `delete_item()`

![image](https://user-images.githubusercontent.com/124485986/216821828-806168e5-2e19-4dfe-b3e5-f5e268a46bf4.png)


#### Test 3:
Ternyata customer salah memasukkan semua item yang ingin dibelanjakan, sehingga customer ingin menghapus semua data transaksi yang masuk dengan method `reset_transaction()`

![image](https://user-images.githubusercontent.com/124485986/216821855-73e1dd93-10bc-441e-ac2d-a27e60bdd862.png)

#### Test 4:
Customer menginput kembali item-item yang ingin dibeli, kemudian akan menghitung semua total belanja yang harus dibayar dengan method `total_price()`

![image](https://user-images.githubusercontent.com/124485986/216821904-fa6ffc5f-8977-4123-b477-fbf2a1f81852.png)

![image](https://user-images.githubusercontent.com/124485986/216821934-d58ea3c6-76a9-440d-bd41-ebb7fa4bb2a4.png)

# Conclution

Modul Transaction sudah berhasil menjalankan feature requirements yang diharapkan Andi sehingga bisa digunakan untuk sistem self-service pada Supermarketnya

# Improvement Suggestions

Agar program lebih mudah digunakan, bisa ditambahkan fungsi input pada setiap methodnya.
