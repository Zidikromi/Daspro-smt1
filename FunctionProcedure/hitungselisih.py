#Muhammad Nawwaf Yazid Ikromi
#NIM: 2405186
#Kelas: RPL 1A  

def selisih(jam1,menit1,detik1,jam2,menit2,detik2):
    selisihjam = jam2- jam1
    selisihmenit = menit2 - menit1
    selisihdetik = detik2 - detik1
    return selisihjam,selisihmenit,selisihdetik

print("Input Mulai")
jam1 = int(input("Jam: "))
menit1 = int(input("Menit: ")) 
detik1 = int(input("Detik: "))
print("Input Selesai")
jam2 = int(input("Jam: "))
menit2 = int(input("Menit: "))
detik2 = int(input("Detik: "))

selisihjam,selisihmenit,selisihdetik = selisih(jam1,menit1,detik1,jam2,menit2,detik2)
print(f"{selisihjam} jam - {selisihmenit} menit - {selisihdetik} detik")

