# Membuat List

# Contoh Struktur data list
buah = ["mangga", "Melon", "anggur", "jeruk"]
# Untuk Mrngakses menggunakan index
print(buah[3])

# Untuk Menambah list
buah.append("Pisang")
print(buah)

# Mengubah list dengan list index[index yang mau di ubah] = "value"
buah[2] = "nangka"
print(buah)

# Menghapus list dengan del
del buah[0]
print(buah)

# Mengambil data akhir sekaligus menghapus (pop)
print(buah.pop())

# Mengetahui jumlah data len(data)
print(len(buah))

# Menyisipkan data sesuai dengan index insert()
buah.insert(0, "jeruk")
print(buah)

# Mengambil seluruh data list menggunkan for

for data in buah:
    print("buah",data)