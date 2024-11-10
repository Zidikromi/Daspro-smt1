#Muhammad Nawwaf Yazid Ikromi
#NIM: 2405186
#Kelas: RPL 1A

a = int(input("Masukkan angka: "))
if(a > 0):
    if (a % 2 == 0):
        print(f"{a} adalah bilangan Positif dan termasuk bilangan Genap")
    else:
        print(f"{a} adalah bilangan Positif dan termasuk bilangan Ganjil")
elif(a < 0):
    if (a % 2 == 0):
        print(f"{a} adalah bilangan Negatif dan termasuk bilangan Genap")
    else:
        print(f"{a} adalah bilangan Negatif dan termasuk bilangan Ganjil")
else:
    print("Nilai Nol")