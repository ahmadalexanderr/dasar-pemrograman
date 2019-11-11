# Nama : Ahmad Alexander
# File : MakeUnion.py
# DEFINISI
# MakeUnion: 2 set --> set
# {MakeUnion (H1,H2) membuat union H1 dengan H2: yaitu set baru dengan semua anggota elemen H1 dan anggota H2}
# {Base : Jika salah satu kosong, hasilnya adalah himpunan yang tidak kosong
# Kedua set kosong, hasilnya sebuah set yang kosong
# Rekurens:
# H1 [e1] o [Tail(H1)]
# H2 [H2]
# e1 adalah Member dari H2: buang e1, MakeUnion(Tail(H1), H2)
# e1 bukan Member dari H2 : e1 o MakeUnion(Tail(H1), H2)}
# REALISASI
def MakeUnion(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return []
    elif not IsEmpty(H1) and IsEmpty(H2):
        return H1
    elif IsEmpty(H1) and not IsEmpty(H2):
        return H2
    else:
        if IsMember(FirstElmt(H1), H2):
            return MakeUnion(Tail(H1), H2)
        else:
            return Konso(FirstElmt(H1), MakeUnion(Tail(H1), Tail(H2)))


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


a = [-1, 2, 3, 4, 5, 6, 10]
b = [-2, 1, 3, 5, 6, 100, 104]
print(MakeUnion(a, b))
