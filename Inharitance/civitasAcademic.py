from mahasiswa import *
from dosen import *

print("\n", 5*('-'), "Civitas Akademik", 5*('-'), "\n")
msh1 = Mahasiswa("Yaasir Aidil Fitrah", "Laki - Laki",
                 19, "Teknik Informatika", 1)
msh1.cetak()

dsn1 = dosen("Puan Maharani", "Perempuan", 24, "SD", "OB Dirumah")
dsn1.setGaji(1000)
dsn1.cetak()


print("\n", 5*('-'), "Selesai", 5*('-'), "\n")
