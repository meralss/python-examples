import datetime
ad=input("Adınızı Girin :")
dogum_yili_=int(input("Doğum Yılınızı Giriniz(YYYY) :"))
guncel_tarih = datetime.datetime.now()
guncel_yil=guncel_tarih.year
yas=guncel_yil-dogum_yili_
print("Merhaba {}, Yaşınız {}'dır" .format(ad,yas))


