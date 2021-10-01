sayi = input('Sayıyı Girin : \n')
ters = sayi[::-1]
print('Girilen sayı = ',  (sayi))
print('Girilen sayının tersi = ', (ters))
if ters == sayi:
    print('Girilen sayı palindrome bir sayıdır.')
else:
    print('Girilen sayı palindrome bir sayı değildir.')

