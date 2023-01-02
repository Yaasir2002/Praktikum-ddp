class Mahasiswa:
    nim = ""
    nama = ""
    rombel = ""

    def lulus(self, nilai):
        if (nilai > 90):
            print("Lulus")
        else:
            print("Tidak Lulus")


msh1 = Mahasiswa()
msh1.nama = "Yaasir"
msh1.nim = "0110222277"
msh1.rombel = "TI13"

print(msh1.nama)
print(msh1.nim)
print(msh1.rombel)
msh1.lulus(98)
