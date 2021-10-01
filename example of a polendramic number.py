sayı = input('Sayıyı Girin : \n')
ters=sayı[:: -1]
print('Girilen sayı= %s')
print('Girilen sayının tersi= %s' % (ters))

if ters == sayı:
    print('Girilen sayı polondirome değildir.')
else:
    print('Girilen sayı polondirome bir sayıdır.')

