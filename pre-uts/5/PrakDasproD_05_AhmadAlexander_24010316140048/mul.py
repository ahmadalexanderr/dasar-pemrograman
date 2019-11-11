# Nama file: mul.py
# Deskripsi: perkalian dua bilangan bulat
# Pembuat: Ahmad Alexander
# Tanggal: 23 September 2019

# DEFINISI DAN SPESIFIKASI
# mul : 2 integer >= 0 --> integer
# {mul(x,y) mengalikan x dan y
# mul(x,y) = x * y
#          = y + y + y + y .... + y
#          = y + y * (x - 1)}

# REALISASI
def mul(x, y):
    if x == 0:
        return 0
    else:
        return mul(x - 1, y) + y


# APLIKASI
print(mul(4, 0))
print(mul(4, 1))
print(mul(5, 5))
