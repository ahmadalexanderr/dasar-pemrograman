# Nama file: absolutv1.py
# Pembuat: Ahmad Alexander
# Tanggal: 9 September 2019
# Deskripsi : menentukan nilai absolut dari sebuah bilangan integer

# Definisi dan spesifikasi dari fungsi absolut bernama absolut(x) adalah:
#   absolut(x) menentukan nilai absolut dari sebuah bilangan integer x

# Realisasi
def absolut(x):
    return x if x > 0 else 0 if x == 0 else -x


# Aplikasi
print(absolut(10))
print(absolut(0))
print(absolut(-10))
