from person import *


class dosen(person):
    gelar = ""
    jabatan = ""
    gaji = 0

    def __init__(self, nama, kelamin, umur, gelar, jabatan):
        super().__init__(nama, kelamin, umur)
        self.gelar = gelar
        self.jabatan = jabatan

    def setGaji(self, uang):
        self.gaji += uang

    def cetak(self):
        super().cetak()
        print("Gelar :", self.gelar)
        print("Jabatan :", self.jabatan)
        print("Gaji :", self.gaji)
        print(5*("-"))
