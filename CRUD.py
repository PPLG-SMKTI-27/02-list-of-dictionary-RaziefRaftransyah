produk1 ={"barang":"Mie","stok":6,"harga":2500}
produk2 ={"barang":"Clean","stok":7,"harga":32500}
produk3 ={"barang":"Masako","stok":10,"harga":9200}
produk4 ={"barang":"Aice","stok":1,"harga":5000}
produk5 ={"barang":"Gulaku","stok":12,"harga":25000}
produkproduk = [produk1,produk2,produk3,produk4,produk5]

def read():
    for i in range(len(produkproduk)):
        print("Nama Produk \t Jumlah Stock \t Harga Barang")
        print(produkproduk[i]["barang"],"\t","\t",produkproduk[i]["stok"],"\t","\t",produkproduk[i]["harga"],"\t")

def create():
    barang = (input())
    stok = int(input())
    harga = int(input())
    produk6 = {"barang":barang,"stok":stok,"harga":harga}
    produkproduk.append(produk6)

def menu():
    print("""
Menu WareHouse
1.Tampilkan Barang
2.Input Barang""")
    pilihan = input("Masukkan Pilihan : ")
    if pilihan == "1":
        read()
        menu()
    elif pilihan =="2":
        create()
        menu()
    else:
        print("pilihan tidak valid")
        menu()
menu()
