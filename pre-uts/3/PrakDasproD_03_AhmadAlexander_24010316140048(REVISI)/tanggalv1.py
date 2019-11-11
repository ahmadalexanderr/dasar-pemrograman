# Nama file: tanggalv1.py
# Pembuat: Ahmad Alexander
# Tanggal: 9 September 2019
# Deskripsi : tanpa memperhitungkan kabisat

# Definisi dan Spesifikasi
# Harike1900 : integer[1...31], integer[1...12], integer[0..99] --> integer[1..366]
# {Harike1900(d,m,y) dari suatu tanggal <d,m,y> adalah hari 'absolut' dihitung mulai 1 Januari 1900+y: 1 Januari tahun 1900+y adalah hari ke 1}
# dpm : integer[1..12] --> integer[1..36]
# {dpm(B) adalah jumlah hari pada tahun ybs pada tanggal 1 bulan B terhitung mulai sati januari: kumulatif jumlah hari dari tanggal 1 Januari s/d tanggal 1 bulan B, tanpa memperhitungkan tahun kabisat }

# Realisasi {Tanpa Kabisat}
def Harike1900(d, m, y):
    return dpm(m) + d - 1


def dpm(B):
    if B == 1:
        return 1
    elif B == 2:
        return 32
    elif B == 3:
        return 60
    elif B == 4:
        return 91
    elif B == 5:
        return 121
    elif B == 6:
        return 152
    elif B == 7:
        return 182
    elif B == 8:
        return 213
    elif B == 9:
        return 244
    elif B == 10:
        return 274
    elif B == 11:
        return 305
    else:
        return 335


inputD = int(raw_input("Masukan tanggal: \n"))
inputM = int(raw_input("Masukan bulan: \n"))
inputY = int(raw_input("Masukan tahun dari 1900 s/d 1999: \n"))

print(Harike1900(inputD, inputM, inputY))

