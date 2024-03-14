class Dagangan:
  jumlah_barang = 0
  list_barang = []

  def __init__(self, nama, stok, harga):
    self.__nama = nama
    self.__stok = stok
    self.__harga = harga
    
    Dagangan.jumlah_barang += 1
    Dagangan.list_barang.append((nama, stok, harga))

  def lihat_barang():
    print(f"Jumlah barang dagangan pada toko: {Dagangan.jumlah_barang} buah")
    for i in range(Dagangan.jumlah_barang):
      print(f"{i+1}. {Dagangan.list_barang[i][0]} seharga Rp {Dagangan.list_barang[i][2]} (stok: {Dagangan.list_barang[i][1]})")

  def __del__(self):
    Dagangan.jumlah_barang -= 1
    Dagangan.list_barang.remove((self.__nama, self.__stok, self.__harga))
    print(f"{self.__nama} dihapus dari toko!")

dagangan1 = Dagangan("Galon Aqua 19L", 32, 17000)
dagangan2 = Dagangan("Gas LPG 5 kg", 22, 88000)
dagangan3 = Dagangan("Beras Ramos 5 kg", 13, 68000)
Dagangan.lihat_barang()
del dagangan1
Dagangan.lihat_barang()
