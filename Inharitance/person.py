class person():
    nama = ""
    kelamin = ""
    umur = 0

    def __init__(self, nama, kelamin, umur):
        self.nama = nama
        self.kelamin = kelamin
        self.umur = umur

    def cetak(self):
        print("Nama :", self.nama)
        print("Kelamin :", self.kelamin)
        print("Umur :", self.umur)
