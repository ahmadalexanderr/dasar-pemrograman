# defspek
# is_empty: L --> boolean
def is_empty(L):
    return L == []


def first_element(x):
    return x[0]


def tail(x):
    return x[1:]


def nba(x):
    if is_empty(x):
        return 0
    else:
        if first_element(x) == "a":
            return 1 + nba(tail(x))
        else:
            return nba(tail(x))


L1 = ["v", "a", "b", "semarang", "a", 2, 7, -1]
print(nba(L1))
