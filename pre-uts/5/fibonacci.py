# Nama file: fibonacci.py
# Deskripsi: menghitung bilangan Fibonacci ke-n
# Pembuat: Ahmad Alexander
# Tanggal: 23 September

# DEFINISI DAN SPESIFIKASI
# fibonacci  :   integer >= 0 --> integer > 0
# fibonacci(n) menghitung bilangan fibonnaci ke-n, sesuai definisi barisan fibonacci 0,1,1,2,3,5,...
#   jika n = 0 : fibonacci(n) = 0
#   jika n = 1 : fibonacci(n) = 1
#   jika n > 1 : fibonacci(n) = fibonacci(n-1)+fibonacci(n-2)


def fibonacci(n):
    if n == 0:  # basis 0
        return 0
    elif n == 1:  # basis 1
        return 1
    else:  # rekurens
        return fibonacci(n - 1) + fibonacci(n - 2)


# APLIKASI
print(fibonacci(0))
print(fibonacci(1))
print(fibonacci(2))
