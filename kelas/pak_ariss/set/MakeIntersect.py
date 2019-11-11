# Nama: Ahmad Alexander
# File: MakeIntersect.py
# DEFINISI
# MakeIntersect: 2 set --> set
# {Intersect(H1,H2) membuat interseksi H1 dengan H2: yaitu set baru dengan anggota elemen yang merupakan anggota H1 dan juga anggota H2}
# {Base  : Jika salah satu kosong, hasilnya set kosong
# Rekurens  :
# H1 [e1] o [Tail(H1)]
# H2 [H2]
# e1 adalah Member dari H2: e 1 o MakeIntersect(Tail(H1), H2)
# e1 bukan Member daru H2: MakeIntersect(Tail(H1)m H2)}
# REALISASI
def MakeIntersect(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif not IsEmpty(H1) and IsEmpty(H2):
        return []
    elif IsEmpty(H1) and not IsEmpty(H2):
        return []
    else:
        if IsMember(FirstElmt(H1), H2):
            return Konso(FirstElmt(H1), MakeIntersect(Tail(H1), H2))
        else:
            return MakeIntersect(Tail(H1), H2)


def IsEmpty(x):
    return x == []


def IsMember(x, L):
    if len(L) == 0:
        return False
    if L[0] == x:
        return True
    else:
        return IsMember(x, L[1:])


def FirstElmt(x):
    if not (IsEmpty(x)):
        return x[0]


def Tail(x):
    if not (IsEmpty(x)):
        return x[1:]


def Konso(x, L):
    if IsEmpty(L):
        return [x]
    else:
        return [x] + L


a = [1, 2, 3, 4, 5, 6]
b = [9, 2, 1, 3, 5, 6]
print(MakeIntersect(a, b))
