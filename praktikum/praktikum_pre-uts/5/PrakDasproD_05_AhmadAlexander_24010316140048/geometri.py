# Nama file: geometri.py
# Deskripsi: Menghitung deret bilangan geometri
# Pembuat: Ahmad Alexander
# Tanggal: 23 September 2019

# DEFINISI DAN SPESIFIKASI
# deret : integer  --> integer
# {deret(x) menghitung deret bilangan aritmatika : 1 + 3 + 9 + 27 + ...
# }

# REALISASI
def geometri(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return 3 * geometri(n - 1) + 1


# APLIKASI
print(geometri(1))
print(geometri(2))
print(geometri(3))
print(geometri(4))
