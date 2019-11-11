def is_empty(x):
    return x == []


def first_element(x):
    if not (is_empty(x)):
        return x[0]


def tail(x):
    if not (is_empty(x)):
        return x[1:]


def konso(x, L):
    if is_empty(L):
        return [x]
    else:
        return [x] + L


# DefSpek
# {Insert: integer, list of, integer tidak kosong, terurut membesar --> list of integer terurut membesar}
# {Insert(x, Li) melakikan insert x ke Li menghasilkan list terurut membesar
# Basis 0: list kosong, insert sebuah elemen x ke list kosong: [x]
# Rekurens:
# e o Tail(Li)
# x <= x o Li
# x > e o Insert(x, Tail(Li))
# Catatam: insert tidak pernah "merusak" keterurutan elemen list!}
def insert(x, Li):
    if is_empty(Li):
        return [x]
    else:
        if x <= first_element(Li):
            return konso(x, Li)
        else:
            return konso(first_element(Li), insert(x, tail(Li)))


# DefSpek
# {Insort(Li) menghasilkan list integer yang terurut dengan metoda insertion sort}
# { Basis 0 : list kosong sudah terurut, hasilnya list kosong
#  Rekurens: Insort(Li)
# e o Tail(Li)
# Hasil: insert e ke Tail(Li) yang sudah terurut dg Insertion sort}
def insort(Li):
    if is_empty(Li):
        return []
    else:
        return insert(first_element(Li), insort(tail(Li)))


L2 = [10, 2, 7, 8, -1, 4, 5, 9, -100]
print(insort(L2))
