# Nama file: aritmatika.py
# Deskripsi: Menghitung deret bilangan aritmatika
# Pembuat: Ahmad Alexander
# Tanggal: 23 September 2019

# DEFINISI DAN SPESIFIKASI
# deret : integer  --> integer
# {deret(x) menghitung deret bilangan aritmatika : 3 + 6 + 9 + 12 + ...
# }

# REALISASI
def aritmatika(n):
    if n == 0:
        return 0
    elif n == 1:
        return 3
    else:
        return (3 * n) + aritmatika(n - 1)


# APLIKASI
print(aritmatika(1))
print(aritmatika(2))
print(aritmatika(3))
print(aritmatika(4))
