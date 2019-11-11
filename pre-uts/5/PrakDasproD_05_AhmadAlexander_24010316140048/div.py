# Nama file: div.py
# Deskripsi: pembagian dua bilangan bulat
# Pembuat: Ahmad Alexander
# Tanggal: 23 September 2019

# DEFINISI DAN SPESIFIKASI
# div : 2 integer >= 0  --> integer
# {div(x,y) x dibagi y
# div(x,y) = x / y}

# REALISASI
def div(x, y):
    if y == 0:
        return 0
    elif x - y == 0:
        return 1
    elif x < y:
        return 0
    else:
        return div(x - y, y) + 1


# APLIKASI
print(div(4, 0))
print(div(4, 1))
print(div(5, 5))
print(div(36, 6))

