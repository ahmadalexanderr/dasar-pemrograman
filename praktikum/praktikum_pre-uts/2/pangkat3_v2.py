# Nama File: pangkat3_v2.py
# Pembuat : Ahmad Alexander
# Tanggal : 2 September 2019
# Deskripsi : menghitung nilai pangkat 3 dari sebuah masukan integer

# Definisi dan spesifikasi dari fungsi pangkat3 bernama fx3_v2 (x) adalah:
# fx3 : integer --> integer
#   fx3v2 (x) menghitung pangkat dua dari x, sebuah bilangan integer, menggunakan fungsi antara fx2(x)

# fx2 : integer --> integer
#   fx2 (x) menghitung pangkat dua dari x, sebuah bilangan integer

# Realisasi
def fx2(x):
    return x * x


def fx3v2(x):
    return x * fx2(x)


# Aplikasi
print(fx3v2(4))
print(fx3v2(4 + 2))

