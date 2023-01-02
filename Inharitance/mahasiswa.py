from person import *


class Mahasiswa(person):
    prodi = ""
    semester = 0

    def __init__(self, nama, kelamin, umur, prodi, semester):
        super().__init__(nama, kelamin, umur)
        self.prodi = prodi
        self.semester = semester

    def cetak(self):
        super().cetak()
        print("Prodi :", self.prodi)
        print("Semester :", self.semester)
        print(5*('-'))
