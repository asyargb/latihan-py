print("PROGRAM MENCARI ANGKA MAKSIMAL")

a = int(input("Masukkan angka pertama: "))
b = int(input("Masukkan angka kedua: "))

if a > b:
    print("Angka maksimal adalah:", a)
elif b > a:
    print("Angka maksimal adalah:", b)
else:
    print("Kedua angka sama besar")