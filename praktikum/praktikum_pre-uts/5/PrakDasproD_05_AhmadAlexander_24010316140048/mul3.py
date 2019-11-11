# Nama file: mul3.py
# Deskripsi: perkalian bilangan dikalikan dengan 3
# Pembuat: Ahmad Alexander
# Tanggal: 23 September 2019

# DEFINISI DAN SPESIFIKASI
# mul : 1 integer >= 0 --> integer
# {mul(x,y) mengalikan x dan y
# mul(x,y) = x * 3
#          = 3 + 3 + 3 + 3 .... + 3
#          = 3 + 3 * (x - 1)}

# REALISASI
def mul3(x):
    if x == 0:
        return 0
    else:
        return mul3(x - 1) + 3


# APLIKASI
print(mul3(3))
print(mul3(4))
print(mul3(5))
