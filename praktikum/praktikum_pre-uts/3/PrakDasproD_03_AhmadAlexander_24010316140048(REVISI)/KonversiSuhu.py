# Nama file: KonversiSuhu.py
# Pembuat: Ahmad Alexander
# Tanggal: 9 September 2019

# Definisi dan Spesifikasi
# KonversiSuhu : real, character --> real, string
# {KonversiSuhu(x, y), fungsi yang menerima suatu besaran dalam derajat celcius dan kode konversi ke derajat Reamur, Fahrenheit, atau Kelvin dan mengirimkan nilai derajat sesuai kode konversi}

# ToReamur : real --> real, string
# {ToReamur(x), fungsi konversi derajat celcius ke derajat reamur}

# ToFah : real --> real, string
# {ToFah(x), fungsi konversi derajat celcius ke derajat fahrenheit}

# ToKelvin : real --> real, string
# {ToKelvin, fungsi konversi derajat celcius ke derajat kelvin}

# Realisasi
def KonversiSuhu(x, y):
    y = y.lower()
    if y == "r":
        x = x * 4 / 5
        return "%s derajat Reamur" % x
    elif y == "f":
        x = (x * 9 / 5) + 32
        return "%s derajat Fahrenheit" % x
    elif y == "k":
        x = x + 273.15
        return "%s derajat Kelvin" % x
    elif y != "r" or y != "f" or y != "k":
        return "Konversi Invalid"


inputX = int(raw_input("Berapa derajat celcius?\n"))
inputY = str(raw_input("Konversi ke dalam derajat :\n"))

print(KonversiSuhu(inputX, inputY))
