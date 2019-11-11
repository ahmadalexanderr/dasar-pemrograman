#RESPONSI DASPRO LAB B
#Nama	: Ahmad Alexander
#NIM	: 24010316140048
#Tanggal: 14 Oktober 2019

#1. Buatlah fungsi untuk menentukan ongkos kirim dari suatu barang berdasarkan grand total dan negara pengirimnya.
#defSpek
#shipping: integer,string --> integer
#shipping(X,Y) menghasilkan biaya ongkir dari barang bernilai X dan dari negara Y.
#ketentuan:
#Pembagian harga dengan ketentuan sbb:
#Pembelian <50000, ongkirnya 26000 (US), 28000 (UK)
#Pembelian 50001-100000, ongkirnya 38000 (US), 45000 (UK)
#Pembelian 100001-150000, ongkirnya 50000 (US), 65000 (UK)
#Pembelian >150000 ongkirnya gratis (0)
#contoh: shipping(120000,"UK") --> 65000
#realisasi
def shipping(x,y):
	if x == 50000:
		if y == "US":
			return 26000
		elif y == "UK":
			return 28000
		else:
			return "Masukan tidak valid"
	elif x > 50000 and x <= 100000:
		if y == "US":
			return 38000
		elif y == "UK":
			return 45000
		else:
			return "Masukan tidak valid"   
	elif x > 100000 and x <= 150000:
		 if y == "US":
			return 50000
		elif y == "UK":
			return 65000
		else:
			return "Masukan tidak valid" 
	elif x > 150000:
		if y == "US" or y == "UK":
			return "ongkirnya gratis (0)"
#aplikasi
print(shipping(120000,"UK"))

# 2. Buatlah tipe bentukan mahasiswa dengan isi NIM dan Nama
# constructor:
# MakeMhs: integer,string --> Mhs
# MakeMhs(NIM,Nama) merupakan konstruktor tipe bentukan Mahasiswa dari tipe integer dan string

# MakeStat: integer, 3 string --> Stat
# MakeStat(NIM,Nama,Jenjang,Status) merupakan konstruktor tipe bentukan Status dari 1 integer dan 3 string.

# Buat pula fungsi untuk menentukan status mahasiswa
# StatusMhs : Mhs --> Stat
# Status mahasiswa berdasarkan NIM:
# 24060119130001
# 1 digit paling kiri: 1 untuk D3, 2 untuk S1, 3 untuk S2, 4 untuk S3
# Digit ke 6 dan 5 dari paling kanan: 
# 10 untuk SBUB, 11 untuk Afirmasi, 12 untuk SNMPTN, 13 untuk SBMPTN, 14 untuk Seleksi Mandiri.

# Contoh aplikasi:
# MakeMhs(24060119130001,"Alexander Sutjipto") --> Mhs
# StatusMhs(Mhs) --> Stat<24060119130001, "Alexander Sutjipto", "S1", "SBMPTN">

# diberikan fungsi: left(txt,jmlkar), right(txt,jmlkar), dan mid(txt,mulai,jmlkar)
# fungsi-fungsi berikut mengembalikan angka dalam bentuk string, bukan integer.

def left(txt, jmlkar):
	if (mulai<0): return ''; else return txt[:jmlkar]

def right(txt, jmlkar):
	if (mulai<0): return ''; else return txt[jmlkar:]

def mid(txt,mulai,jmlkar):
	if (mulai<0): return ''; else return txt[mulai:mulai+jmlkar]

# 3. Cari bilangan ke-n di deret bilangan berpola lucu
# bilanganLucu : integer -> integer
# bilanganLucu(n) menghasilkan bilangan ke-n dari deret 1 3 2 5 3 7 4 ....
# Contoh aplikasi:
# bilanganLucu(3) --> 2
