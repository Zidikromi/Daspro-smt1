#Muhammad Nawwaf Yazid Ikromi
#NIM: 2405186
#Kelas: RPL 1A

def cekpassword(a,b):
    user = "Daspro2023"
    pw = "Latihan"
    coba = 3
    while coba > 0:
        if b == pw:
            print("Selamat Datang di aplikasi Prodi RPL.")
            break
        else: 
            print(f"Login Salah! Kesempatan anda {coba} x lagi")
            coba -= 1
            b = input("Password : ")
        if coba == 0:
            print("Anda keluar dari menu login")

username = input("Username : ")
password = input("Password : ")
cekpassword(username,password)