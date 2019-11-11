# soal RESPONSI TIPE BENTUKAN
# Nama : Ahmad Alexander
# NIM : 24010316140048
# Lab : E Dalam / Kelas D


# definisi TYPE
# type mahasiswa : <nama:string, NIM:string>
# nama bisa kalian isi terserah, untuk NIM isi sesuaikan format NIM kalian


class Mahasiswa:
    def __init__(self, nama, NIM):
        self.nama = nama
        self.NIM = NIM


# DEf SPEK Selektor

# Nama : string --> string
# nama(mhs) memberikan nama dari mahasiswa
def nama(mhs):
    return mhs.nama


# NIM : string --> string
# NIM(mhs) memberikan NIM dari mahasiswa
def NIM(mhs):
    return mhs.NIM


# angkatan : string --> string
# angkatan(mhs) memberikan angkatan dari mahasiswa
# angkatan didapat dari NIM
# format nim : 24060117130078,
# (indeks mulai dari 0) indeks nim untuk angkatan adalah indeks ke 6-7
# gunakan operasi range slice untuk mengambil indeks ke 6-7 tersebut
# dari contoh terlihat angkatan 17, buatlah supaya angkatan(mhs) memberikan keluaran 2017
# gunakan operasi (+) untuk menggabungkan string 20 dan angkatan(mhs)
def angkatan(mhs):
    # lengkapi
    return "20" + mhs.NIM[6:8]


# jalur_masuk : string --> string
# jalur_masuk(mhs) memberikan jalur masuk dari mahasiswa
# jalur masuk didapat dari NIM
# format nim : 24060117130078,
# (indeks mulai dari 0) indeks nim untuk jalur masuk adalah indeks ke 9
# gunakan operasi range slice untuk mengambil indeks ke 9 tersebut
# jalur masuk = '2' --> SNMPTN, '3' --> SBMPTN, '4' --> UMPTN/Mandiri, jalur lainya --> 'Khusus"
# dari contoh terlihat jalur masuk '3', buatlah supaya jalur_masuk(mhs) memberikan keluaran SBMPTN
# gunakan ekspresi Kondisional  untuk mendapatkan hasil tsb.
def jalur_masuk(mhs):
    # lengkapi
    if mhs.NIM[9] == "2":
        return "SNMPT"
    elif mhs.NIM[9] == "3":
        return "SBMPTN"
    elif mhs.NIM[9] == "4":
        return "UMPTN/Mandiri"
    else:
        return "Khusus"


# Aplikasi
mhs1 = Mahasiswa("Eugeo Minerva", "24060117130078")
mhs2 = Mahasiswa("Norman", "24060116110069")
print(
    "Mahasiswa bernama "
    + (nama(mhs1))
    + " NIM "
    + (NIM(mhs1))
    + " , Angkatan "
    + (angkatan(mhs1))
)
print("Diterima lewat jalur " + (jalur_masuk(mhs1)))

print(
    "Mahasiswa bernama "
    + (nama(mhs2))
    + " NIM "
    + (NIM(mhs2))
    + " , Angkatan "
    + (angkatan(mhs2))
)
print("Diterima lewat jalur " + (jalur_masuk(mhs2)))

