# Nama file : max3v3b.py
# Pembuat : Ahmad Alexander
# Tanggal : 9 September 2019
# Deskripsi : menentukan nilai maksimum dari 3 bilangan integer

# Definisi dan spesifikasi dari fungsi max3 bernama max(a,b,c) adalah:
# max3 : 3 integer --> integer
#   max3(a,b,c) menentukan nilai maksimum dari 3 bilangan integer yang berlainan a, b, dan c, menggunakan ekspresi kondisional versi 3 dengan short-hand if

# Realisasi
def max3(a, b, c):
    if a > b:
        return a if a > c else c
    else:
        return b if b > c else c

# Aplikasi
print(max3(12, 7, 5))
print(max3(4, 9, -10))
print(max(100, -20, 300))

