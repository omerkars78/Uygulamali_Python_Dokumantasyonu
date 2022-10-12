#******************************** SAYISAL VERİ TİPLERİ VE SAYISAL OPERATÖRLER ***************************************
# 1-) SAYISAL VERİ TİPLERİ

# - Integer (int)
# 1,2,3,4,-3,-2
# print(type(4))
# 1,2,3,4
# int(2)
# # - Float 
# 1.1,2.5,-3.8938943 
# print(type(1.1))
# # 2-) SAYISAL OPERATÖRLER

# # - Toplama (+)
# print(1+1)
# # - Çıkarma (-)
# print(2-1)
# # - Çarpma  (*)
# print(5*5)
# # - Bölme   (/)
# print(int(36/6))
# # - Mod Alma (%)
# print(15%4)
# # - Üs Alma (**)
# print(2**4)
# 3-) SAYISAL VERİ TİPLERİ ARASI İŞLEMLER





#****************************************** DEĞİŞKENLER *************************************************************
# 1-) Değişken Nedir?
sayi_1 = 4 
sayi_2 = 8
print(sayi_1*sayi_2)
print(3*4)
# 2-) Değişken tanımlama Kuralları Nelerdir? 

# - Sayı ile Başlayamaz
degisken = 4
# - Boşluk İçeremez
birinciSayi = 1
# - Büyük Küçük Harf Farklılığı Vardır
age = 3
AGE = 5
aGe = 8 
age = 10
print(age)
print(AGE)
print(aGe)
# - Yan Yana Değer Ataması Yapılabilir
x,y,z = 1,2,3
# - Türkçe Karakter İçermese Güzel Olur
#ı,ü,ö,ğ
# 3-) Değişkenlerle İlgili Uygulamalar(vize final notu )

vize_notu = 70
final_notu = 60 
vize_etki = 0.5 
final_etki = 0.5
gecme_notu = int((vize_notu*vize_etki) + (final_notu*final_etki))
print(gecme_notu)




#****************************************** STRİNGLER *************************************************************
# 1-) String Veri Tipi Nedir
bilgi= "Bu bir string ifadedir"
bilgi= 'Bu bir string ifadedir' 
bilgi_2 = "Bu bir 'string' ifadedir"
bilgi_3 = 'Bu bir "string" ifadedir'
# sayi_1 = str(1)
# sayi_2 = str(2)
# sayi_1 = "1"
# sayi_2 = "     2"

# print(bilgi)
# print(sayi_1+sayi_2)
# print(bilgi_2)
# print(bilgi_3)
# 2-) String İşlemleri Nelerdir (İndeks Kavramı)
bilgi_4 = "Bu bir string ifadedir indexler tutar"
# print(bilgi_4[2])
# print(bilgi_4[5:19])
# print(bilgi_4[:-1])
# 3-) Stringle İlgili Fonksiyonlar

#  - Len (Uzunluk Fonksiyonu)
# print(len(bilgi_4))
# print(bilgi_4[36])
#  - Upper ve Lower Fonksiyonları 
lower_1 = "merhaba bu bir mesajdır"
lower_2 = "BU FARKLI BİR ŞEYDİR"
print(lower_1.upper())
print(lower_2.lower())
#  - Startswith ve Endswith Fonksiyonları

#  - Split Fonksiyonu (Ayrıma)

#  - Replace Fonksiyonu (Cümle Değiştirme)







#****************************************** LİSTELER *************************************************************
# 1-) Liste Nedir Nasıl Tanımlanır ?


#  - Liste İşlemleri (index)

#  - İç İçe Liste

# 2-) Liste Metodları Nelerdir Nasıl Kullanılır?

# * Sadece listerde kullanırız
# * İşlerimiz kolaylaştırır

#  - Append (ekleme)


#  - İnsert (indekse göre ekleme)


#  - Pop (Son elemanı çıkarma)


#  - Remove (Seçili elemanı çıkarma)


#  - Del (İstenilen yerleri silme)


#  - Count (İstenilen Elemanın Kaç Adet olduğunu bulma)

#  - İndex(İstenilen Elemanın İndexini Bulma)

#  - Reverse(Tersine Çevirme)


#  - Sort(Harf Sırasına Göre Sıralama)


# 3-) TUPLES 

# - Öğelere Erişim Ortaktır

# - Len Metodu Ortaktır

# - Count Metodu Ortaktır

# - İndex Metodu Ortaktır

# - Tuple Birleştirme


# 4-) Dictionary
# - Dictionary Nedir? Nasıl Tanımlanır? 

# # - Dictionary Metodları

# # - keys()(Anahatarları liste olarak sıralar)

# # - values()(Value değerlerini liste olarak sıralar)

# # - items()(key ve valueları aynı anda sıralar)

# # - get()(sözlük elemanını alırız)

# # - pop()(istenilen keyi siler)

# # - copy()(sözlüğün kopyasını alır bununla alının kopya aslını etkilemez)

# # - update()(Verileri güncellememize yarar)(({}))







#****************************************** OPERATÖRLER *************************************************************
# 1-) Artimetik Operatörler 
# (+),(-),(*),(/),(%),(**)

# 2-) Atama Operatörleri
# - Eşittir Operatörü(=)

# # - Artı Eşittir Operatörü(+=)

# # - Eksi Eşittir Operatörü(-=)

# # - Çarpı Eşittir Operatörü(*=)

# # - Bölü Eşittir Operatörü(/=)

# # - Mod Eşittir Operatörü(%=)

# # 3-) Karşılaştırma Operatörleri(Sonucun True veya False değerlerini Aldığımız Operatörler)
# # - Eşittir Operatörü(==)

# # - Eşit Değildir Operatörü(!=)

# # - Büyüktür Operatörü(>)

# # - Küçüktür Operatörü(<)

# # - Büyük Eşittir Operatörü(>=)

# # - Küçük Eşittir Operatörü(<=)

# # 4-) Mantıksal Operatörler(Sonucunda True veya False Değer Aldığımız Operatörlerdir)
# # - And Operatörü

# # And operatöründe True bir sonuç almak için her iki ifadeninde doğru olması gerekir.
# # - Or Operatörü

# Or operatöründe True bir sonuç almak için her iki ifadenin veya yanlızca birinin doğru olması yeterlidir.





#****************************************** KOŞULLU İFADELER *************************************************************
# 1-) If ve ELse Nedir Nasıl ve Nerelerde Kullanılır ?
# a,b,c = 1,2,1

# 2-) Elif Bloğu Nedir Hangi durumlarda Kullanılır ?


# 4-) Elif Uygulaması




#****************************************** DÖNGÜLER *************************************************************
# 1-) For Döngüleri Nedir? Ne İşe Yarar? Nasıl Tanımlanır ?



# 2-) While Döngüleri Nedir ve Nasıl Tanımlanır?


    
# # -) While İle Neler Yapabiliriz?(tam sayı çift sayı)

# # -) While Bloğu İçinde İf ve Else (break Continue)






#****************************************** FONKSİYONLAR *************************************************************
# def bolum_1(girdi_1):
#     return f"{girdi_1} işlendi ve iplik oldu."

# def bolum_2(girdi_2):
#     return f"{girdi_2} işlendi ve kumaş oldu."    

# def bolum_3(girdi_3):
#     return f"{girdi_3} işlendi ve giysi oldu."      

# def fabrika(girdi_1,girdi_2,girdi_3):
#     print(bolum_1(girdi_1) , bolum_2(girdi_2) , bolum_3(girdi_3),
#     "Sonuç olarak pamuk fabrikamıza girdi ve giysi olarak çıktı")


# fabrika("Pamuk","İplik","Kumaş")

# 1-) Fonksiyonların Tanımlanması

# 2-) Fonksiyondan Değer Döndürme (Return)

# 3-) Fonksiyona Parametre Gönderme(Fonksiyonun temel bileşenleri = girdi işlem ve çıktı)

# 4-) İç İçe Fonksiyonlar

# 5-) Uygulama





#****************************************** NESNE TABANLI PROGRAMLAMA *************************************************************
# 1-) Class Tanımlanması 



# 2-) Nesne Oluşturulması 



# 3-) __init__ Metodunun Tanımlanması



# 5-) Objeye ait Metodların Oluşturulması 


# 6-) Class Methodlarının Oluşturulması 


# 7-) Kalıtım

#Bütün Araçlarda ortak olan özellikler vardır.
#Ancak çeşitli motorlu taşıt türlerinin kendilerine ait farklı özellikleride bulunmaktadır.
#Bu sebepten dolayı diğer araç türleri üzerinden oluşturacağımız classlar için ayrı ayrı
#  (classlar ve Objeler için)
# Metod tanımlamaya gerek yoktur.
# Ortak Özellikte olanları zaten Araç classına tanımlamak yeterlidir.

# ATA => ÇOCUK => TORUN
# PARENT => CHİLD

#ÇALIŞIR , MARKASI , MODELİ ,

# class Arac():
#pass
    
# class Otomobil(Arac):
#pass

# class Otobus():
# pass
         






#****************************************** MODÜLLER *************************************************************
# bilgi = "bu bir modül dosyasıdır"

# 2-) İmport Yöntemleri 

# 1. Yöntem (import)(iee.bilgileri_goster)


# 2. Yöntem  (from modül import *)


# 3. Yöntem (as)


#4. Yöntem (from iee import bilgi as bg)
 

# 3-) BUİLT-İN MODULES

# 1. Random Modülü 
 

