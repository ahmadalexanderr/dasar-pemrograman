# Nama file : fac.py
# Deskripsi : menghitung factorial dari sebuah bilangan integer secara rekursif
# Pembuat : Ahmad Alexander
# Tanggal: 23 September 2019

# DEFINISI DAN SPESIFIKASI
# fac : integer > 0 --> integer > 0
#   fac(n) = n! sesuai dengan definisi rekursif factorial, versi 1 dengan basis=1

# REALISASI
# Realisasi dengan definisi factorial fac(n) = n! dimana
#   jika n = 1 : n! = 1
#   jika n > 1 : n! = n * (n-1)!
def fac(n):
    if n == 1:  # basis 1
        return 1
    else:  # rekurens: definisi factorial
        return n * fac(n - 1)


# APLIKASI
print(fac(1))
print(fac(3))
print(fac(6))
