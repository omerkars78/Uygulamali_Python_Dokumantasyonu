#******************************** SAYISAL VERİ TİPLERİ VE SAYISAL OPERATÖRLER ***************************************
# 1-) SAYISAL VERİ TİPLERİ

# - Integer (int)

# - Float 

# 2-) SAYISAL OPERATÖRLER

# - Toplama (+)

# - Çıkarma (-)

# - Çarpma  (*)

# - Bölme   (/)

# - Mod Alma (%)

# - Üs Alma (**)

# 3-) SAYISAL VERİ TİPLERİ ARASI İŞLEMLER





#****************************************** DEĞİŞKENLER *************************************************************
# 1-) Değişken Nedir?

# 2-) Değişken tanımlama Kuralları Nelerdir? 

# - Sayı ile Başlayamaz

# - Boşluk İçeremez

# - Büyük Küçük Harf Farklılığı Vardır

# - Yan Yana Değer Ataması Yapılabilir

# - Türkçe Karakter İçermese Güzel Olur

# 3-) Değişkenlerle İlgili Uygulamalar






#****************************************** STRİNGLER *************************************************************
# 1-) String Veri Tipi Nedir

# 2-) String İşlemleri Nelerdir (İndeks Kavramı)

# 3-) Stringle İlgili Fonksiyonlar

#  - Len (Uzunluk Fonksiyonu)

#  - Upper ve Lower Fonksiyonları 

#  - Find Fonksiyonu

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

# # - update()(Verileri güncellememize yarar)







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


    
# # -) While İle Neler Yapabiliriz?

# # -) While Bloğu İçinde İf ve Else 






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
bilgi = "bilgi"

#4. Yöntem (from iee import bilgi as bg)
 

# 3-) BUİLT-İN MODULES

# 1. Random Modülü 
# 2. Datetime Modülü 

