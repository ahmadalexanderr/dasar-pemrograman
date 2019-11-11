# Nama                   : Ahmad Alexander
# NIM                    : 24010316140048
# tgl praktikum          : 4 November 2019
# Deskripsi dari file   :
#
# defspek
# mklist : kosong --> list
# #mklist() membuat list L
#
def mklist():
    return []


L1 = mklist()
L2 = [1, 2, 3, 4, 5, 6, 7]
L3 = [1, 2, 3, 2, 5, 2, 7]
L4 = [3, 2, 4, 90, 87, 6555, 32, 12, 5344, 51, 0]
L6 = []
L7 = ["a", "b", "c", "d", "e", "a", "1"]
L8 = ["apple", "banana", "avocado"]
print()

# defspek
# Konso : elemen, list --> list
# Konso(e,L) menghasilkan sebuah list dari L dengan menambahkan e


def Konso(e, L):
    Ls = list(L)
    Ls.reverse()
    Ls.append(e)
    Ls.reverse()
    return Ls


def Konso2(e, L):
    Ls = list(L)
    return [e] + Ls


# defspek
# Konso0 : list,elemen --> list
# Kons0(e,L) menghasilkan sebuah list dari L dengan menambahkan e sebagai elemen terakhir
def coba(L):
    L.reverse()
    return L


def coba2(L):
    Ls = list(L)
    Ls.reverse()
    return Ls


def Kons0(L, e):
    Ls = list(L)
    Ls.append(e)
    return Ls


# defspek:
# invers :
# invers(L) memberikan list yang urutannya terbalik dari aslinya


def inverse(Ls):
    # Ls = list(L)
    Ls.reverse()
    return Ls


def inverse2(Ls):
    # Ls = list(L)
    if len(Ls) == 0:
        return []
    else:
        return [Ls[len(Ls) - 1]] + list(inverse2(Ls[1 : len(Ls) - 1])) + [Ls[0]]


def inverse3(L):
    Ls = list(L)
    if Isempty(L):
        return []
    else:
        return [LastElemt(L)] + inverse3(Head(Ls))


# DefSpek
# Tail : list tidak kosong --> list
# Tail(L) menghasilkan elemem selain elemen pertama dari list L
def Tail(L):
    Ls = list(L)
    del Ls[0]
    return Ls


def Head(L):
    Ls = list(L)
    Ls.reverse()
    del Ls[0]
    Ls.reverse()
    return

