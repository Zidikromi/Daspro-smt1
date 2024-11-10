# Union (|)
a = {"apel", "mangga", "pisang", "nanas"}
b = {"ceri", "nanas", "jeruk", "mangga"}
c = a.union(b)

print(c)

# Intersection (&) 
a = {"apel", "mangga", "pisang", "nanas"}
b = {"ceri", "nanas", "jeruk", "mangga"}
a.intersection_update(b)

print(a)

# Difference (-)
a = {"apel", "mangga", "pisang", "nanas"}
b = {"ceri", "nanas", "jeruk", "mangga"}
a.difference_update(b)

print(a)

# Symmetric Difference (^)
a = {"apel", "mangga", "pisang", "nanas"}
b = {"ceri", "nanas", "jeruk", "mangga"}
a.symmetric_difference_update(b)

print(a)

# Menambahkan item di set dari list
a = {"apel", "mangga", "pisang", "nanas"}
b = ["ceri", "nanas", "jeruk", "mangga"]
a.update(b)

print(a)

# Menambahkan item di set dari tuple
a = {"apel", "mangga", "pisang", "nanas"}
b = ("ceri", "nanas", "jeruk", "mangga")
a.update(b)

print(a)

data = {1, 2, 3, 2, 1, 4, 5, 3}
unique_data = list(data)
print(unique_data)  # Output: {1, 2, 3, 4, 5}

kucing = {
    "nama" : "Kuda Hitam",
    "umur" : "2",
    "ras" : "negro",
    "jantan":  True,
    "Hobi": ["sare", "makan"]
}

print(kucing)

kucing["umur"] = 20 #edit

print(kucing)

kucing["jomok"] = True
print(kucing) #menambah key baru

kucing.update({"umur": 1000, "nama":"reza"})
print(kucing) #update 
# print(kucing)
# print(kucing["nama"])
# print(kucing.get("nama"))
# print(kucing.keys())
# print(kucing.values())

a = dict(nama = "ambatakum",umur = 20, ras = "negro" )
# print(a)