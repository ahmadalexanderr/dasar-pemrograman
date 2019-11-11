# Nama file : max2.py
# Pembuat : Ahmad Alexander
# Tanggal : 9 September 2019
# Deskripsi : menentukan nilai maksimum dari 2 bilangan integer

# Definisi dan spesifikasi dari fungsi max2 bernama max(a,b) adalah:
# max2 : 2 integer --> integer
#   max2(a,b) menentukan nilai maksimum dari 2 bilangan integer a dan b menggunakan short-hand if

# Realisasi
def max2(a, b):
    return a if a >= b else b

# Aplikasi
print(max2(4, 9))
print(max2(100, -20))
print(max2(10, 10))

