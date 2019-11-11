# Nama file: WujudAir.py
# Pembuat: Ahmad Alexander
# Tanggal: 9 September 2019

# DEFINISI DAN SPESIFIKASI
# WujudAir : integer --> string
# {WujudAir(x), fungsi menentukan apakah air berwujud es (padat), cair, atau uap}

# REALISASI
def WujudAir(x):
    if x < 0:
        return "%s derajat celcius, air berwujud es (padat) " % x
    if x >= 0 and x <= 100:
        return "%s derajat celcius, air berwujud cair" % x
    if x > 100:
        return "%s derajat celcius, air berwujud uap" % x


# APLIKASI
inputX = int(raw_input("Berapa derajat celcius?\n"))

print(WujudAir(inputX))
