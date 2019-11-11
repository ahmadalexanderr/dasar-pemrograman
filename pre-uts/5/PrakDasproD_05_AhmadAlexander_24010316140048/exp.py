# Nama file: pangkat.py
# Deskripsi: perpangkatan bilangan bulat
# Pembuat: Ahmad Alexander
# Tanggal: 23 September 2019

# DEFINISI DAN SPESIFIKASI
# exp : 2 integer >= 0 --> integer
# {exp(x,y) menghasilkan x ^ y, x != 0}

# REALISASI
# {exp(x,y) = x ^ y
#   = x * x * x * ..... * x
#   = x * x^(y-1)}
def exp(x, y):
    if y == 0:
        return 1
    else:
        return x * exp(x, prec(y))


def prec(n):
    return n - 1


# APLIKASI
print(exp(4, 0))
print(exp(4, 1))
print(exp(2, 3))
print(exp(5, 5))
