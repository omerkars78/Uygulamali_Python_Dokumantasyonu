#***************************** DEĞİŞKENLER *********************************

# 1-) Değişken Nedir?
sayi1 = 1
name = "Michael"
print(sayi1)
print(name)

# 2-) Değişken tanımlama Kuralları Nelerdir? 

# - Sayı ile Başlayamaz
#sayi1 , sayi2 # 1sayi => yanlış gösterim
# - Boşluk İçeremez
ilk_degisken = 10
print(ilk_degisken)
# - Büyük Küçük Harf Farklılığı Vardır
age = 15
AGE = 20
print(AGE)
# - Yan Yana Değer Ataması Yapılabilir
x,y,z = 9,"Ömer","20.2"
print(x,y,z)

# - Türkçe Karakter İçermese Güzel Olur
# sonuç sonuc Değişken degisken 

# 3-) Değişkenlerle İlgili Uygulamalar
sayi1 = 15
sayi2 = 33
sonuc1 = (sayi1 + sayi2) * (sayi1 - sayi2)
sonuc2 = (sayi1 + sayi2) / (sayi1 - sayi2)
sonuc3 = sonuc1 + sonuc2 
print(sonuc3)

isim = "Ömer"
soyisim = "Kars"
yas = "20"
sehir = "İzmir"
omer_bilgi = isim +" "+soyisim+" " + yas+ " " + sehir
print(omer_bilgi)
