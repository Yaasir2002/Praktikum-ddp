# Fungsi

def Hello():
    print("Hello Word")


Hello()
print("")


def dataDiri(nama="Yaasir Aidil Fitrah", rombel="TI13", nim="0110222277"):
    print("Nama Lengkap : ", nama)
    print("Rombel Anda : ", rombel)
    print("NIM Anda :", nim)


dataDiri("Ucup", "SI06", "0110163430")
print("")
dataDiri()


def metode(cuaca):
    if cuaca == "cerah":
        print("Naik Motor")
    elif cuaca == "hujan":
        print("Naik GOCAR")
    else:
        print("Kiamat")


metode("hujan")
metode("cerah")
