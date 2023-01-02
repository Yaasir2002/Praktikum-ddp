class Mahasiswa:
    nim = ""
    nama = ""
    rombel = ""

    def __init__(self, nim, nama, rombel):
        self.nim = nim
        self.nama = nama
        self.rombel = rombel

    def lulus(self, nilai):
        if (nilai > 90):
            print("Lulus")
        else:
            print("Tidak Lulus")


msh1 = Mahasiswa("0110222277", "Yaasir Aidil Fitrah", "TI13")
# msh1.nama = "Yaasir"
# msh1.nim = "0110222277"
# msh1.rombel = "TI13"

print("Nama :", msh1.nama)
print("NIM :", msh1.nim)
print("Rombel :", msh1.rombel)
msh1.lulus(98)
