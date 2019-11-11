# Nama file: point.py
# Deskripsi: membuat tipe bentukan point beserta konstruktor dan selektornya
# Pembuat: Ahmad Alexander
# Tanggal: 16 September 2019

from math import sqrt
from pangkat2 import fx2

# DEFINISI TYPE
# type point : <x: real, y: real>
# {<x,y> adalah sebuah point, dengan x adalah absis dan y adalah ordinat}

# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakePoint: 2 real --> point
# MakePoint (x,y) membentuk sebuah point dari a dan b dengan a sebagai absis dan b sebagai ordinat
# Realisasi dalam Python
class Point:
    def __init__(self, a, b):
        self.x = a
        self.y = b


# DEFINISI DAN SPESIFIKASI SELEKTOR
# Absis : point --> real
# Absis(P) memberikan absis point P
# Realisasi dalam Python
def absis(P):
    return P.x


# Ordinat: point --> real
# Ordinat(P) memberikan ordinat point P
# Realisasi dalam Python
def ordinat(P):
    return P.y


# DEFINISI DAN SPESIFIKASI PREDIKAT
# IsOrigin?: point --> boolean
# IsOrigin?(P) benar jika P adalah titik origin <0,0>
# Realisasi dalam Python
def is_origin(P):
    return absis(P) == 0 and ordinat(P) == 0


# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP POINT
# jarak: 2 point --> real
# jarak(P1,P2) meng menghitung jarak antara 2 point P1 dan P2
def jarak(P1, P2):
    return sqrt(fx2(absis(P1) - absis(P2)) + fx2(ordinat(P1) - ordinat(P2)))


# jarak0: point --> real
# jarak(P) menghitung jarak antara point P dengan titik origin <0,0>
# Realisasi dalam Python
def jarak0(P):
    return sqrt(fx2(absis(P)) + fx2(ordinat(P)))


# kuadran: point --> integer
# kuadaran(P) mengembalikan kuadran dimana opint P berada, dengan syarat P bukan titik <0,0>, tidak terletak di sumbu X maupun sumbu Y
# Realisasi dalam Python
def kuadran(P):
    if (absis(P) > 0) and (ordinat(P) > 0):
        return 1
    elif (absis(P) < 0) and (ordinat(P) > 0):
        return 2
    elif (absis(P) < 0) and (ordinat(P) < 0):
        return 3
    elif (absis(P) > 0) and (ordinat(P) < 0):
        return 4


# Aplikasi
P = Point(2, 3)
print(absis(P))
print(ordinat(P))
print(is_origin(Point(-2, 3)))
print(jarak(P, Point(-1, 5)))
print(jarak0(P))
print(kuadran(P))
