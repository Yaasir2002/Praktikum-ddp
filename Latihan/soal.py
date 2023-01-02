# Soal Tuple
print("\nlatihan list")
makanan = [['bakwan', 'tempe', 'tahu'],
           ["nasi uduk", "nasi pecel", "sate padang"]]
print(makanan[1][1])
print(makanan[0][2])

for data in makanan[1]:
    print("makanan", data)

for inpput in makanan[0]:
    print("makanan", inpput)

for menu in makanan:
    for menu1 in menu:
        print("isi menu", menu1)
print("selesai\n")

print("latihan tuple")
gorengan = ("Bakwan", "Combro", "Misro")  # Index 0
sop = ("Sop Iga", "Sop Buntut", "Sop Kaki")  # Index 1
nasi = ("Nasi Uduk", "Nasi Goreng", "Nasi Remes")  # Index 2

paket1 = (("Bakwan", "Combro", "Misro"), ("Sop Iga", "Sop Buntut",
          "Sop Kaki"), ("Nasi Uduk", "Nasi Goreng", "Nasi Remes"))

print(paket1[0])
for i in paket1[1]:
    print(i)

print(paket1[1][1])
print(paket1[2][2])

print("")

for u in paket1:
    for o in u:
        print(o)
