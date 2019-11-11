# Nama file: pecahan.py
# Deskripsi: membuat tipe bentukan pecahan beserta konstruktor dan selektornya
# Pembuat: Ahmad Alexander
# Tanggal: 16 September 2019
# COMPILE DENGAN Python3.7
from fractions import Fraction

# DEFINISI DAN SPESIFIKASI TYPE
# type pecahan: <n : integer >= 0, d: integer > 0 >
# {<n:integer >= 0, d: integer > 0> n adalah pembilang (numerator) dan d adalah penyebut (denumerator. Penyebut sebuah pecahan tidak boleh nol)}
# Realisasi dalam Python
class Pecahan:
    def __init__(self, a, b):
        a >= 0
        b > 0
        self.n = a
        self.d = b


# DEFINISI DAN SPESIFIKASI SELEKTOR DENGAN FUNGSI
# Pemb: pecahan --> integer >= 0
# {Pemb(p) memberikan numerator pembilang n dari pecahan tsb}
# Peny : pecahan --> integer > 0
# {Peny(p) memberikan denumerator penyebut d dari pecahan tsb}
def Pemb(P):
    return P.n


def Peny(P):
    return P.d


# DEFINISI DAN SPESIFIKASI KONSTRUKTOR
# MakeP: integer >= 0, integer > 0 --> pecahan
# {MakeP(x,y) membentuk sebuah pecahan dari pembilang x dan penyebut y, dengan x dan y integer}
def MakeP(x, y):
    return Fraction(x / y)


# DEFINISI DAN SPESIFIKASI OPERATOR TERHADAP PECAHAN
# {Operator Aritmatika Pecahan}
# AddP : 2 pecahan --> pecahan
# {AddP(P1,P2): Menambahkan dua buah pecahan P1 dan P2: n1/d1 + n2/d2 = (n1*d2+n2*d1)/d1*d2}
def AddP(P1, P2):
    return MakeP((Pemb(P1) * Peny(P2) + Pemb(P2) * Peny(P1)), (Peny(P1) * Peny(P2)))


# SubP : 2 pecahan --> pecahan
# {SubP(P1,P2) : mengurangkan dua buah pecahan P1 dan P2
#   Mengurangkan dua pecahan: n1/d1 - n2/d2 = (n1*d2-n2*d1)/d1*d2 }
def SubP(P1, P2):
    return MakeP((Pemb(P1) * Peny(P2) - Pemb(P2) * Peny(P1)), (Peny(P1) * Peny(P2)))


# MulP : 2 pecahan --> pecahan
# {MullP(P1,P2): Mengalikan dua pecahan P1 dan P2
#   Mengalikan dua pecahan: n1/d1 * n2/d2 = n1*n2/d1*d2
def MulP(P1, P2):
    return MakeP((Pemb(P1) * Pemb(P2)), (Peny(P1) * Peny(P2)))


# DivP : 2 pecahan --> pecahan
# {DivP(P1,P2): Membagi dua buah pecahan P1 dan P2
#   Membagi dua pecahan: (n1/d1)/(n2/d2) = n1*d2/d1*n2}
def DivP(P1, P2):
    return MakeP((Pemb(P1) * Peny(P2)), (Peny(P1) * Pemb(P2)))


# RealP : pecahan --> real
# Menuliskan bilangan pecahan dalam notasi desimal
def RealP(P):
    return Pemb(P) / Peny(P)


# DEFINISI DAN SPESIFIKASI PREDIKAT
# {Operator relasional Pecahan}
# IsEqP?: 2 pecahan --> boolean
# {IsEqP?(P1,P2) true jika p1 = p2
#   Membandingkan apakah dua buah pecahan sama nilainya: n1/d1 = n2/d2 jika dan hanya jika n1d2=n2d1}
def IsEqP(P1, P2):
    return Pemb(P1) * Peny(P2) == Peny(P1) * Pemb(P2)


# IsLtP?: 2 pecahan --> boolean
# {IsLtP?(P1,P2) true jika P1 < P2
#   Membandingkan dua buah pecahan, apakah p1 lebih kecil nilainya dari p2: n1/d1 < n2/d2 jika dan hanya jika n1d2<n2d1}
def IsLtP(P1, P2):
    return Pemb(P1) * Peny(P2) < Peny(P1) * Pemb(P2)


# IsGtP?: 2 pecahan --> boolean
# {IsGtP?(P1,P2) true jika P1>P2
#   Membandingkan nilai dua buah pecahan, apakah P1 lebih besar nilainya dari P2:n1/d1>n2/d2 jika dan hanya jika n1d2>n2d1}
def IsGtP(P1, P2):
    return Pemb(P1) * Peny(P2) > Peny(P1) * Pemb(P2)


# Aplikasi (Compile dengan Python3.7)
P = Pecahan(2, 3)
print(Pemb(P))
print(Peny(P))
print(MakeP(10, 20))
print(AddP(P, P))
print(SubP(P, Pecahan(9, 10)))
print(MulP(P, Pecahan(5, 9)))
print(DivP(P, Pecahan(5, 5)))
print(RealP(P))
print(IsEqP(P, Pecahan(4, 6)))
print(IsLtP(Pecahan(0, 5), P))
print(IsGtP(P, Pecahan(1, 2)))

