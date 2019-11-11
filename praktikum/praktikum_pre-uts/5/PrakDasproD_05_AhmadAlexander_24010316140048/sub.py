# Nama file: sub.py
# Deskripsi: pengurangan dua bilangan bulat
# Pembuat: Ahmad Alexander
# Tanggal: 23 September 2019

# DEFINISI DAN SPESIFIKASI
# sub : 2 integer >= 0  --> integer
# {sub(x,y) menjumlahkan x dan y
# sub(x,y) = x - y
#           = x + y(-1) - 1}

# REALISASI
def sub(x, y):
    if y == 0:  # basis 0
        return x
    else:  # rekurensi
        return sub(x, y - 1) - 1


# APLIKASI
print(sub(4, 0))
print(sub(4, 1))
print(sub(5, 5))
