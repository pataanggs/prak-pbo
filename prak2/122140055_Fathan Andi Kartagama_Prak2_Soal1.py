class Mahasiswa:

    def __init__(self, nim, nama, angkatan, is_mahasiswa=True):
        self.__nim = nim
        self.__nama = nama
        self.angkatan = angkatan
        self.is_mahasiswa = is_mahasiswa

    def method1(self):
        return f"Nama Mahasiswa/i: {self.__nama}\nNIM: {self.__nim}"

    def method2(self):
        return f"Mahasiswa/i {self.__nama} dengan NIM {self.__nim} merupakan mahasiswa/i Angkatan {self.angkatan}"

    def method3(self):
        return f"{self.__nama} {'merupakan seorang mahasiswa/i ITERA' if self.is_mahasiswa else 'bukan mahasiswa/i ITERA'}"

    @property
    def nim(self):
        return self.__nim

    @nim.setter
    def nim(self, new_nim):
        self.__nim = new_nim

    @property
    def nama(self):
        return self.__nama

    @nama.setter
    def nama(self, new_nama):
        self.__nama = new_nama


mhs1 = Mahasiswa(122140055, "Fathan Andi Kartagama", 2022, True)
mhs2 = Mahasiswa(123140666, "Budiono Siregar", 2023)

print(mhs1.method1())
print(mhs1.method2())
print(mhs1.method3())
print("\n")
print(mhs2.method1())
print(mhs2.method2())
print(mhs2.method3())
