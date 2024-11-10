#Muhammad Nawwaf Yazid Ikromi
#NIM: 2405186
#Kelas: RPL 1A

students = {
    "Alice": "Computer Science",
    "Bob": "Mathematics",
    "Charlie": "Physics",
    "David": "Computer Science",
    "Eva": "Mathematics"
}
a = list(students.values())


hasil = {
    "Computer Science": a.count("Computer Science"),
    "Mathematics": a.count("Mathematics"),
    "Physics": a.count("Physics")
}

for key, values in hasil.items():
    print(f"Prodi {key} sebanyak {values}")