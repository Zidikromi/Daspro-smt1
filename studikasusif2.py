#Muhammad Nawwaf Yazid Ikromi
#NIM: 2405186
#Kelas: RPL 1A

nama = input("Masukkan nama: ")
umur = int(input("Masukkan umur: "))
tinggi = int(input("Masukkan tinggi: "))
jk = input("Masukkan Jenis Kelamin (pria/wanita): ").lower()
iq = int(input("Masukkan IQ: "))

if (umur >= 18 and umur <= 25) and (iq >= 130):
   if(jk == "pria" and tinggi >=175):
       print(f"{nama} layak menjadi Model")
   elif(jk == "wanita" and tinggi >= 170):
       print(f"{nama} layak menjadi Model")
   else:
        print("Input tidak valid")
else:
    print("Anda bukan model")
