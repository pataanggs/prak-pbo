import math

class Bentuk:
    def hitungLuas(self):
        pass

class Persegi(Bentuk):
    def __init__(self, sisi):
        self.sisi = sisi

    def hitungLuas(self):
        return self.sisi ** 2

class Lingkaran(Bentuk):
    def __init__(self, radius):
        self.radius = radius

    def hitungLuas(self):
        return math.pi * self.radius ** 2

# Membuat objek persegi dan lingkaran
persegi = Persegi(5)
lingkaran = Lingkaran(3)

# Menghitung dan mencetak luas persegi dan lingkaran tanpa perlu memeriksa jenis objek secara eksplisit
print(f"Luas Persegi: {persegi.hitungLuas()}")       # Output: Luas Persegi: 25
print(f"Luas Lingkaran: {lingkaran.hitungLuas()}")   # Output: Luas Lingkaran: 28.274333882308138
