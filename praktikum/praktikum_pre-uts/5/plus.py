# Nama file: plus.py
# Deskripsi: pejumlahan dua bilangan bulat
# Pembuat: Ahmad Alexander
# Tanggal: 23 September 2019

# DEFINISI DAN SPESIFIKASI
# plus : 2 integer > 0 --> integer > 0
# plus(x,y) menjumlahkan x dan y
# plus(x,y) = x + y
#           = x + 1 + y(-1)


def plus(x, y):
    if y == 0:  # basis 0
        return x
    else:  # rekurensi
        return 1 + plus(x, y - 1)

# APLIKASI
print(plus(4, 0))
print(plus(4, 1))
print(plus(5, 5))

