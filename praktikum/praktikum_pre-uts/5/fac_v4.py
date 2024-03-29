# Nama file : fac_v4.py
# Deskripsi : menghitung factorial dari sebuah bilangan integer versi iteratif
# Pembuat : Ahmad Alexander
# Tanggal: 23 September 2019

# DEFINISI DAN SPESIFIKASI
# faciter : 3 integer > 0 --> integer > 0
# faciter(n,count,hasil) menghitung n! sesuai dengan definisi: fac(n) = 1*2*3*...*n = hasil
# jika n = count : hasil (sebelumnya) * count
# jika n < count : faciter(n,count+1,hasil*count)

# fac : integer > 0 --> integer > 0
#   fac(n) menghitung n! versi iteratif menggunakan fungsi antara faciter(n,count,hasil)

# REALISASI
def faciter(n, count, hasil):
    if n == count:
        return hasil * count
    else:
        return faciter(n, count + 1, hasil * count)


def fac(n):
    return faciter(n, 1, 1)


# APLIKASI
print(fac(1))
print(fac(3))
print(fac(6))
