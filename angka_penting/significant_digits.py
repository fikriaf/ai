import math

def hitung_angka_penting(angka):
    angka_str = str(angka).strip()
    if '.' in angka_str:
        bilangan_bulat, desimal = angka_str.split('.')
        if bilangan_bulat == '0':
            angka_penting = len(desimal.rstrip('0'))
        else:
            angka_penting = len(bilangan_bulat.lstrip('0')) + len(desimal.rstrip('0'))
    else:

        angka_penting = len(angka_str.rstrip('0'))
        
    print(f"Jumlah s.d = {angka_penting}")
    return angka_penting

def pembulatan_angka_penting(hasil, angka_penting):
    if angka_penting == 0:
        return hasil
    hasil_bulat = round(hasil, -int(math.floor(math.log10(abs(hasil)))) + (angka_penting - 1))
    return int(hasil_bulat) if hasil_bulat.is_integer() else hasil_bulat


def penjumlahan(a, b):
    hasil = float(a) + float(b)
    angka_penting = min(hitung_angka_penting(a), hitung_angka_penting(b))
    print(f"Maka, hasilnya harus berjumlah {angka_penting} s.p")
    return pembulatan_angka_penting(hasil, angka_penting)

def pengurangan(a, b):
    hasil = float(a) - float(b)
    angka_penting = min(hitung_angka_penting(a), hitung_angka_penting(b))
    print(f"Maka, hasilnya harus berjumlah {angka_penting} s.p")
    return pembulatan_angka_penting(hasil, angka_penting)

def perkalian(a, b):
    hasil = float(a) * float(b)
    angka_penting = min(hitung_angka_penting(a), hitung_angka_penting(b))
    print(f"Maka, hasilnya harus berjumlah {angka_penting} s.p")
    return pembulatan_angka_penting(hasil, angka_penting)

def pembagian(a, b):
    hasil = float(a) / float(b)
    angka_penting = min(hitung_angka_penting(a), hitung_angka_penting(b))
    print(f"Maka, hasilnya harus berjumlah {angka_penting} s.p")
    return pembulatan_angka_penting(hasil, angka_penting)

while(True):
    a = input("A : ")
    hitung = input("Operasi : ")
    b = input("B : ")

    if hitung == "+":
        print(f"\nHasil: {a} + {b} = {penjumlahan(a, b)}\n")
    elif hitung == "-":
        print(f"\nHasil: {a} - {b} = {pengurangan(a, b)}\n")
    elif hitung == "*" or hitung == "x":
        print(f"\nHasil: {a} * {b} = {perkalian(a, b)}\n")
    elif hitung == "/" or hitung == ":":
        print(f"\nHasil: {a} / {b} = {pembagian(a, b)}\n")
    else:
        print("Salah input operasi COKK")
