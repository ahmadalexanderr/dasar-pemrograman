# soal RESPONSI TIPE BENTUKAN
# Nama : Ahmad Alexander
# NIM : 24010316140048
# Lab : E Dalam / Kelas D


def aritmatika(n):
    if n == 0:
        return 0
    elif n == 1:
        return 1
    else:
        return n * aritmatika(n - 1)


print(bin(aritmatika(1)))
print(bin(aritmatika(3)))
print(bin(aritmatika(6)))
