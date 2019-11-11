# nama : Ahmad Alexander
# file : IsIntersect.py
# DEFINISI PREDIKAT
# IsIntersect: 2 set --> boolean
# {IsIntersect (H1,H2) true jika H1 berinteraksi dengan H2: minimal ada satu anggota yang sama. Himpunan kosong bukan merupakan himpunan yang berinteraksi dengan himpunan apapun}
# {Base  :   Salah satu kosong --> false
# Rekurens:
# H1 [e1] o [Tail(H1)]
# H2 [] o [Tail(H2)]
# e1 adalah Member dari H2: true
# e1 bukan Member dari H2: Intersect(Tail(H1), H2)}
# Realisasi
def IsIntersect(H1, H2):
    if IsEmpty(H1) and IsEmpty(H2):
        return False
    elif not IsEmpty(H1) and IsEmpty(H2):
        return False
    elif IsEmpty(H1) and not IsEmpty(H2):
        return False
    else:
        return IsMember(FirstElmt(H1), H2) or IsIntersect(Tail(H1), H2)


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
b = [10, -1, 3, 2, 1, 4]
print(IsIntersect(a, b))

