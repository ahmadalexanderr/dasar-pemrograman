# Nama file: absolut.py
# Pembuat: Ahmad Alexander
# Tanggal: 9 September 2019
# Deskripsi : menentukan nilai absolut dari sebuah bilangan integer

# Definisi dan spesifikasi dari fungsi absolut bernama absolut(x) adalah:
#   absolut(x) menentukan nilai absolut dari sebuah bilangan integer x

# Realisasi
def absolut(x):
    if x > 0:
        return x
    elif x == 0:
        return 0
    else:
        return -x


print(absolut(10))
print(absolut(0))
print(absolut(-10))
