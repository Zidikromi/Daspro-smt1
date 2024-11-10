#Muhammad Nawwaf Yazid Ikromi
#NIM: 2405186   
#RPL 1A
def volumetabung(r,t):
    v = 3.14 * r * r * t
    return v

r = float(input("Masukkan jari-jari: "))
t = float(input("Masukkan tinggi: "))

print(f"Volume Tabung adalah {volumetabung(r,t)} cm" )