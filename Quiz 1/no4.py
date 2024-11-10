#Muhammad Nawwaf Yazid Ikromi
#NIM: 2405186
#Kelas: RPL 1A

barangjuli = ["Kerudung","Kemeja","Rok","Celana Panjang","Baju Renang","Topi","Tas","sepatu","Kacamata"]

print(f"Barang di bulan juli: {barangjuli}")
print("Jumlah barang bulan juli", len(barangjuli))

bulanini = barangjuli
bulanini[4] = "Piyama"
bulanini.append("Ikat Rambut")
bulanini.append("Sandal")

print(f"\nBarang di bulan ini: {bulanini}")
print("Jumlah barang bulan ini", len(bulanini))