# Toplama
def Topla(x, y):
    return x + y


# Çıkarma
def Cikar(x, y):
    return x - y


# Çarpma
def Carp(x, y):
    return x * y


# Bölme
def Bol(x, y):
    return x / y


print("Yapılacak İşlemi Seçin.")
print("1.Toplama")
print("2.Çıkarma")
print("3.Çarpma")
print("4.Bölme")


secim = input("Seçiminiz (1/2/3/4):")

sayi1 = int(input("1. Sayı: "))
sayi2 = int(input("2. Sayı: "))

if secim == "1":
    print("SONUÇ =", Topla(sayi1, sayi2))

if secim == "2":
    print("SONUÇ =", Cikar(sayi1, sayi2))

if secim == "3":
    print("SONUÇ =", Carp(sayi1, sayi2))

if secim == "4":
    print("SONUÇ =", Bol(sayi1, sayi2))
