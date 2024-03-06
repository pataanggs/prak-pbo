def memiliki_buku(func):
    def wrapper(*args, **kwargs):
        print("Saya memiliki buku dengan detail sebagai berikut:")
        return func(*args, **kwargs)
    return wrapper

class Book:
    def __init__(self, judul, pengarang):
        self.judul = judul
        self.pengarang = pengarang
        print(f"Buku '{self.judul}' oleh {self.pengarang} telah ditambahkan ke koleksi.")

    @memiliki_buku
    def display_details(self):
        print(f"Judul: {self.judul}\nPengarang: {self.pengarang}")

    def __del__(self):
        print(f"Buku '{self.judul}' oleh {self.pengarang} telah dihapus dari koleksi.")

buku1 = Book("Jika Kita Tak Pernah Jadi Apa-Apa", "Alvi Syahrin")
buku1.display_details()

del buku1