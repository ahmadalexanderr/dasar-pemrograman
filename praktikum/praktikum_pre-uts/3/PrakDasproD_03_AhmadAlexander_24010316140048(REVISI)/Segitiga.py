# Nama file: Segitiga.py
# Pembuat: Ahmad Alexander
# Tanggal: 9 September 2019

# DEFINISI DAN SPESIFIKASI
# Segitiga : integer[1..], integer[1..], integer[1..] --> string
# {Segitiga(x,y,z), fungsi yang menerima masukan berupa 3 buah bilangan integer lebih besar dari 0, yaitu a, b, dan c yang menyatakan panjang setiap sisi sebuah segitiga}

# REALISASI
def Segitiga(x, y, z):
    if x <= 0 or y <= 0 or z <= 0:
        return "Sisi invalid"
    elif x == y and y == z:
        return "Segitiga sama sisi"
    elif x == y:
        return "Segitiga sama kaki"
    else:
        return "Segitiga sembarang"


# APLIKASI
inputX = int(raw_input("Berapa sisi X?\n"))
inputY = int(raw_input("Berapa sisi Y?\n"))
inputZ = int(raw_input("Berapa sisi Z?\n"))

print(Segitiga(inputX, inputY, inputZ))
