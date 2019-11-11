# soal RESPONSI TIPE BENTUKAN
# Nama : Ahmad Alexander
# NIM : 24010316140048
# Lab : E Dalam / Kelas D
import datetime

# type Hr : integer[1...31]
# {definisi ini hanyalah untuk "menanamkan" type integer dengan nilai tertentu supaya mewakili hari, sehingga jika dipunyai suatu nilai integer, kita dapat memeriksa apakah nilai integer tersebut mewakili hari yang absah}
class Hr:
    def __init__(self, a):
        if a >= 1 and a <= 31:
            self.d = a


# type Bln: integer[1...12]
# {definisi ini hanyalah untuk "menanamkan type integer dengan daerah nilai tertentu supaya mewakili Bulan"}
class Bln:
    def __init__(self, b):
        if b >= 1 and b <= 12:
            self.m = b


# type Thn: integer > 0
# {definisi ini hanyalah untuk "Menanamkan" type integer dengan daerah nilai tertentur supaya mewakili Tahun}
class Thn:
    def __init__(self, c):
        if c > 0:
            self.y = c


# type date<d: Hr, m: Bln, y:Thn>
# {<d,m,y> adalah tanggal d bulan m tahun y}
class Date:
    def __init__(self, Hr, Bln, Thn):
        self.d = Hr
        self.m = Bln
        self.y = Thn


# DEFINISI DAN SPESIFIKASI SELEKTOR
# Day: date --> Hr
# {Day(D) memberikan hari d dari D yang terdiri dari <d,m,y>}
def Day(D):
    return D.d


# Month: date --> Bln
# {Month(D) memberikan bulan m dari D yang terdiri dari <d,m,y>}
def Month(D):
    return D.m


# Year: date --> Thn
# {Year(D) memberikan tahun y dari D yang terdiri dari <d,m,y>}
def Year(D):
    return D.y


# KONSTRUKTOR
# MakeDate: <Hr,Bln,Thn> --> date
# MakeDate (<h,b,t>) --> tgl pada hari,bulan,tahun yang bersangkutan
def MakeDate(h, b, t):
    D.d = h
    D.m = b
    D.y = t
    return D


# DEFINISI DAN SPESIFIKASI OPERATOR/FUNGSI LAIN TERHADAP DATE
# Nextday: date --> date
#   {Nextday(D): menghitung date yang merupakan keesokan hari dari date D yang diberikan:
#   Nextday(<1,1,80>) adalah (<2,1,80>)
#   Nextday(<31,1,80>) adalah (<1,2,80>)
#   Nextday(<30,4,80>) adalah (<1,5,80>)
#   Nextday(<31,12,80>) adalah (<1,1,81>)
#   Nextday(<28,2,80>) adalah (<29,2,80>)
#   Nextday(<28,2,81>) adalah (<1,3,82>)
# }
def Nextday(D):
    m = D.m
    if D.m == 1 or D.m == 3 or D.m == 5 or D.m == 7 or D.m == 8 or D.m == 10:
        if D.d < 31:
            MakeDate(D.d + 1, D.m, D.y)
        else:
            MakeDate(1, D.m + 1, D.y)
    elif D.m == 2:
        if D.d < 28:
            MakeDate(D.d + 1, D.m, D.y)
        else:
            if IsKabisat(D.y):
                if D.d == 28:
                    MakeDate(D.d + 1, D.m, D.y)
                else:
                    MakeDate(1, D.m + 1, D.y)
            else:
                MakeDate(1, D.m + 1, D.y)
    elif D.m == 4 or D.m == 6 or D.m == 9 or D.m == 11:
        if m < 30:
            MakeDate(1, D.m + 1, D.y)
        else:
            MakeDate(D.d + 1, D.m, D.y)
    elif D.m == 12:
        if m < 31:
            MakeDate(1, 1, D.y + 1)
        else:
            MakeDate(D.d, D.m + 1, D.y)
    return D.d, D.m, D.y


# Yesterday : date --> date
#   {Yesterday(D): Menghitung date yang merupakan 1 hari sebelum date D yang diberikan:
#   Yesterday(<1,1,80>) adalah <31,12,79>
#   Yesterday(<31,1,80>) adalah <30,1,80>
#   Yesterday (<1,5,80>) adalah <30,4,80>
#   Yesterday (<31,12,80>) adalah <30,12,80>
#   Yesterday (<29,2,80) adalah <28,2,80>
#   Yesterday (<1,3,80>) adalah <29,2,80>
#  }
def Yesterday(D):
    if D.d == 1:
        if D.m == 12 or D.m == 5 or D.m == 7 or D.m == 8 or D.m == 10:
            MakeDate(30, D.m - 1, D.y)
        elif D.m == 1:
            MakeDate(31, 12, D.y - 1)
        elif D.m == 3:
            if IsKabisat(D.y):
                MakeDate(29, 2, D.y)
            else:
                MakeDate(28, 2, D.y)
        elif D.m == 4 or D.m == 6 or D.m == 9 or D.m == 11:
            MakeDate(31, D.m, D.y)
    else:
        MakeDate(D.d - 1, D.m, D.y)
    return D.d, D.m, D.y


# HariKe1900: date --> integer[0..366]
# {HariKe1900(D): Menghitung jumlah hari terhadap 1 Januari pada tahun y, dengan memperhitungkan apakah y adalah tahub kabisat}
def HariKe1900(D):
    return dpm(D.m) + D.d - 1 + (1 if D.m > 2 and IsKabisat(D.y) else 0)


def dpm(B):
    if B == 1:
        return 1
    elif B == 2:
        return 32
    elif B == 3:
        return 60
    elif B == 4:
        return 91
    elif B == 5:
        return 121
    elif B == 6:
        return 152
    elif B == 7:
        return 182
    elif B == 8:
        return 213
    elif B == 9:
        return 244
    elif B == 10:
        return 274
    elif B == 11:
        return 305
    else:
        return 335


# NextNday : date,integer --> date
# {NextNDay(D,N): Menghitung date yang merupakan N hari (N adalah integer) sesudah dari date D yang diberikan}
def NextNDay(D, N):
    if D.m == 1 or D.m == 3 or D.m == 5 or D.m == 7 or D.m == 8 or D.m == 10:
        if D.d + N > 31:
            MakeDate(D.d + N - 31, D.m + 1, D.y)
        else:
            MakeDate(D.d + N, D.m, D.y)
    elif D.m == 4 or D.m == 6 or D.m == 9 or D.m == 11:
        if D.d + N > 30:
            MakeDate(D.d + N - 30, D.m + 1, D.y)
        else:
            MakeDate(D.d + N, D.m, D.y)
    elif D.m == 12:
        if D.d + N > 31:
            MakeDate(D.d + N - 31, 1, D.y + 1)
    elif D.m == 2:
        if IsKabisat(D.y):
            if D.d + N > 29:
                MakeDate(D.d + N - 29, D.m + 1, D.y)
            else:
                MakeDate(D.d + N, D.m, D.y)
        elif D.d + N > 28:
            MakeDate(D.d + N - 28, D.m + 1, D.y)
        else:
            MakeDate(D.d + N, D.m, D.y)
    return D.d, D.m, D.y


# PREDIKAT
# IsEqD?: 2 date --> boolean
# {IsEqD(d1,d2) benar jika d1=d2, mengirimkan true jika d1=d2 dan m1=m2 dan y1=y2
# Contoh: EqD(<1,1,90>,<1,1,90>) adalah true
#         EqD(<1,1,80>,<1,1,90>) adalah false}
def IsEqD(D1, D2):
    return HariKe1900(D1) == HariKe1900(D2)


# IsBefore?: 2 date --> boolean
# {IsBefore?(d1,d2) benar e jika d1 adalah sebelum d2 mengirimkan true jika D1 adalah "sebelum" D2:
# HariKe1900 dari D1 adalah lebih kecil dari HariKe1900 D2
# Contoh:   Before(<1,1,80>,<1,2,80>) adalah false
#           Before(<1,1,80>,<2,1,80>) adalah true}
def IsBefore(D1, D2):
    if D1.y != D2.y:
        return D1.y < D2.y
    else:
        if D1.m != D2.m:
            return D1.m < D2.m
        else:
            return D1.d < D2.d


# IsAfter?: 2 date --> boolean
# {IsAfter?(d1,d2) benar jika d1 adalah sesudah d2 mengirimkan true jika D1 adalah "sesudah" D2: HariKe1900 dari D1 adalah lebih besar dari HariKe1900 dari D2}.
# Contoh :   After(<1,11,80>,<1,2,80>) adalah true
#           After(<1,1,80>,<2,1,80>) adalah flase
#           After(<1,1,80>,<1,1,80>) adalah false}
def IsAfter(D1, D2):
    if D1.y != D2.y:
        return D1.y > D2.y
    else:
        return HariKe1900(D1) > HariKe1900(D2)


# IsKabisat?: integer --> boolean
# {IsKabisat?(a) true jika tahun 1900+a adalah tahun kabisat: habis dibagi 4 tetapi tidak habis dibagi 100, atau habis dibagi 400}
def IsKabisat(a):
    return ((a % 4 == 0) and (a % 100 != 0)) or (a / 400 == 0)  # jika format dd,mm,yyyy
    # return a % 4 == 0 jika format dd,mm,yy


def horoskop(D):
    if D.m == 12:
        return "Sagitarius" if (D.d < 22) else "Capricorn"
    elif D.m == 1:
        return "Capricorn" if (D.d < 20) else "Aquarius"
    elif D.m == 2:
        return "Aquarius" if (D.d < 19) else "Pisces"
    elif D.m == 3:
        return "Pisces" if (D.d < 21) else "Aries"
    elif D.m == 4:
        return "Aries" if (D.d < 20) else "Taurus"
    elif D.m == 5:
        return "Taurus" if (D.d < 21) else "Gemini"
    elif D.m == 6:
        return "Gemini" if (D.d < 21) else "Cancer"
    elif D.m == 7:
        return "Cancer" if (D.d < 23) else "Leo"
    elif D.m == 8:
        return "Leo" if (D.d < 23) else "Virgo"
    elif D.m == 9:
        return "Virgo" if (D.d < 23) else "Libra"
    elif D.m == 10:
        return "Libra" if (D.d < 23) else "Scorpio"
    elif D.m == 11:
        return "Scorpio" if (D.d < 22) else "Sagitarius"


# Aplikasi
D = Date(16, 9, 1997)
A = Date(9, 9, 1996)
P = Date(11, 11, 1961)
print(horoskop(D))
print(horoskop(A))
print(horoskop(P))

