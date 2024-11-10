#Muhammad Nawwaf Yazid Ikromi
#NIM: 2405186
#Kelas: RPL 1A

Mobil = {
    "Merk" : "Honda",
    "Tipe" : "HRV",
    "Tahun" : "2018",
    "Warna":  "Hitam",
    "No.Polisi": "D 1234 ABC",
    "Bensin": "Pertalite",
    "Transmisi": "Manual"
}

print("Mobil Lama Pak Oki adalah: ")
print("Merk: ",Mobil["Merk"])
print("Tipe: ",Mobil["Tipe"])
print("Warna: ",Mobil["Warna"])
print("Tahun: ",Mobil["Tahun"])

print("\nMasukkan informasi detail mobil baru")
Mobil["Merk"] = input("Merk: ")
Mobil["Tipe"] = input("Tipe: ")
Mobil["Tahun"] = input("Tahun: ")
Mobil["Warna"] = input("Warna: ")
Mobil["Bensin"] = input("Bensin: ")
Mobil["Transmisi"] = input("Transmisi: ")
Mobil["No.Polisi"] = input("No. Polisi: ")

print("\n============================")
print("Mobil Baru Pak Oki adalah: ")
print("Merk: ",Mobil["Merk"])
print("Tipe: ",Mobil["Tipe"])
print("Warna: ",Mobil["Warna"])
print("Tahun: ",Mobil["Tahun"])
print("============================")


