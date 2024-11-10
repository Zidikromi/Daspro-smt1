#Muhammad Nawwaf Yazid Ikromi
#NIM: 2405186
#Kelas: RPL 1A
student_info = {
  "Alice" : {"age" : 20, "major" : "Computer Science"},
  "Bob" : {"age" : 21, "major" : "Mathematics"},
  "Charlie" : {"age" : 19, "major" : "Physics"},
}

name = input("Masukkan nama: ")

info = student_info.get(name)
age = info["age"]
major = info["major"]

print(f"umur {name} adalah {age} tahun dan Prodi nya adalah {major}")