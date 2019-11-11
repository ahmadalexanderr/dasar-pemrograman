import math

# Nama file: jarak2titik.py
# Pembuat : Ahmad Alexander
# Tanggal 2 September 2019

# Definisi dan Spesifikasi
# LS : 4 real -> real
# LS(x1,x2,y1,y2) adalah jarak antara dua buah titik (x1,x2) dengan (y1,y2)

# Definisi dan Spesifikasi Fungsi Antara
# dif2 : 2 real --> real
# dif(x,2) adalah kuadrat dari selisih antara x dan y
# FX2 : real --> real
# FX2(x) adalah hasil kuadrat dari x

# Realisasi


def LS(x1, y1, x2, y2):
    return math.sqrt(dif2(y2, y1) + dif2(x2, x1))


def FX2(x):
    return x * x


def dif2(x, y):
    return FX2(x - y)


# Aplikasi
print(LS(1, 3, 5, 6))

