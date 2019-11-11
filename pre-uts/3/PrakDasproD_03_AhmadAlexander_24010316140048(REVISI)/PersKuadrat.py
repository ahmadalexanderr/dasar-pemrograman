import math

# Nama file: PersKuadrat.py
# Pembuat: Ahmad Alexander
# Tanggal: 9 September 2019

# DEFINISI DAN SPESIFIKASI
# PersKuadrat : real[1...], real[1...], real[1...] --> (real, real)
# persamaan kuadrat ax^2 + bx + c = 0 menggunakan rumus abc dng masukan berupa 3 buah koefisien, yaitu a, b, dan c.

# REALISASI
def PersKuadrat(a, b, c):
    D = (b ** 2) - (4 * a * c)
    if D < 0:
        return "Akar imajiner"
    elif D == 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = x1
        result = (x1, x2)
        return result
    elif D >= 0:
        x1 = (-b + math.sqrt(D)) / (2 * a)
        x2 = (-b - math.sqrt(D)) / (2 * a)
        result = (x1, x2)
        return result


# APLIKASI
inputA = float(raw_input("Berapa koefisien a?\n"))
inputB = float(raw_input("Berapa koefisien b?\n"))
inputC = float(raw_input("Berapa koefisien c?\n"))

print(PersKuadrat(inputA, inputB, inputC))

