lst = []
adet = int(input('Kaç Sayı Girilecek: '))
for n in range(adet):
    sayi = int(input('Sayıyı gir: '))
    lst.append(sayi)
print("Liste İçindeki En Büyük Sayı :", max(lst), "\nListe içindeki En Küçük Sayı :", min(lst))