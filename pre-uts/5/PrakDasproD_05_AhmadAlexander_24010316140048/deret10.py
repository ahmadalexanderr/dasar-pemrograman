# Nama file: deret10.py
# Deskripsi: Menghitung deret : 1 + 4 + 9 + 16 + ...
# Pembuat: Ahmad Alexander
# Tanggal: 23 September 2019

# DEFINISI DAN SPESIFIKASI
# deret : integer  --> integer
# {deret(x) menghitung deret : 1 + 4 + 9 + 16 + ...
# }

# REALISASI
def sum(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n ** 2 + sum(n - 1)


# APLIKASI
print(sum(1))
print(sum(2))
print(sum(3))
print(sum(4))
