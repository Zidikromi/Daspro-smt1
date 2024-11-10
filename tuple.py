#Muhammad Nawwaf Yazid Ikromi
#NIM: 2405186
#Kelas: RPL 1A

buah = ("apel","jeruk","ceri","durian","apel","mangga")
print(buah[2:6])

x = list(buah)
x.pop(3)
buah = tuple(x)
print(buah)

buah = ("apel","jeruk","ceri","durian","apel","mangga")
x = list(buah)
x.insert(2,"manggis")
buah = tuple(x)

print(buah)