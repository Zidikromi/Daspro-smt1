#Muhammad Nawwaf Yazid Ikromi
#NIM: 2405186
#Kelas: RPL 1A

def totalrata(*x):
    total = sum(x)
    rata = total / len(x)
    return total, rata

input1 = input("Masukkan angka dengan koma (contoh 1,2,3) :") 
angka = [int(i) for i in input1.split(",")]  

total, rata = totalrata(*angka) 
print(f"Total: {total}")
print(f"Rata-rata: {rata}")