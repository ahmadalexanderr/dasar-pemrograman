# Nama file: isValid.py
# Pembuat : Ahmad Alexander
# Tanggal 2 September 2019

# Definisi dan Spesifikasi
# IsValid? : integer --> integer
# IsValid? (x) benar jika (x) bernilai lebih kecil 5 atau lebih besar dari 500

# Realisasi
def IsValid(x):
    return x < 5 or x > 500


# Aplikasi
print(IsValid(5))
print(IsValid(0))
print(IsValid(500))
print(IsValid(6000))
