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

# - Dictionary Metodları

# - keys()(Anahatarları liste olarak sıralar)

# - values()(Value değerlerini liste olarak sıralar)

# - items()(key ve valueları aynı anda sıralar)

# - get()(sözlük elemanını alırız)

# - pop()(istenilen anahtarı siler)

# - copy()(sözlüğün kopyasını alır bununla alının kopya aslını etkilemez)

# - update()(Verileri güncellememize yarar)








#****************************************** OPERATÖRLER *************************************************************
# 1-) Artimetik Operatörler 
# (+),(-),(*),(/),(%),(**)

# 2-) Atama Operatörleri
# - Eşittir Operatörü(=)

# - Artı Eşittir Operatörü(+=)

# - Eksi Eşittir Operatörü(-=)

# - Çarpı Eşittir Operatörü(*=)

# - Bölü Eşittir Operatörü(/=)

# - Mod Eşittir Operatörü(%=)

# 3-) Karşılaştırma Operatörleri(Sonucun True veya False değerlerini Aldığımız Operatörler)
# - Eşittir Operatörü(==)

# - Eşit Değildir Operatörü(!=)

# - Büyüktür Operatörü(>)

# - Küçüktür Operatörü(<)

# - Büyük Eşittir Operatörü(>=)

# - Küçük Eşittir Operatörü(<=)

# 4-) Mantıksal Operatörler(Sonucunda True veya False Değer Aldığımız Operatörlerdir)
# - And Operatörü

# And operatöründe True bir sonuç almak için her iki ifadeninde doğru olması gerekir.
# - Or Operatörü

# Or operatöründe True bir sonuç almak için her iki ifadenin veya yanlızca birinin doğru olması yeterlidir.





#****************************************** KOŞULLU İFADELER *************************************************************
# 1-) If ve ELse Nedir Nasıl ve Nerelerde Kullanılır ?

# 2-) Elif Bloğu Nedir Hangi durumlarda Kullanılır ?

# 3-) Uygulama 
# Bir üniversitede vize notunun %40 ı Final Notunun %60 ı alınarak geçme notu hesaplanmaktadır.
# Buna göre 85 ve üzeri için harf notu AA, 70 ve 85 arası için BA, 60 ve 70 arası için BB,
# Eğer 45 ve 60 arasındaysa CB , eğer 45 ten düşükse FF olacak şekildedir.
# Bu koşullara göre geçme notu hesaplayan ve harf notu olarak karşılık veren python kodunu yazınız.






#****************************************** DÖNGÜLER *************************************************************
# 1-) For Döngüleri Nedir? Ne İşe Yarar? Nasıl Tanımlanır ?



# 2-) While Döngüleri Nedir ve Nasıl Tanımlanır?

# -) While İle Neler Yapabiliriz?

# -) While Bloğu İçinde İf ve Else 
    
# -) Break ve Continue Nedir Ne İşe Yarar?








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
# Maaşı 5000 TL olan bir kişinin harcamalarına yönelik bir program yazınız. 
# Geliştirilecek programda harcamalar değişken olarak tanımlanacak ve maaş limitine göre
#  "... miktarında alış veriş daha yapabilirsiniz" veya ".. limiti .... kadar aştınız, 
#  bazı harcamaları çıkarmanız gerekli..." vb uyarıları da kapsamalı.
# Eğer limit aşımı varsa değişkenleri tekrar isteyen bir uygulama olsun
#fonksiyon , döngüler , koşul ifadeleri , operatörler




#****************************************** NESNE TABANLI PROGRAMLAMA *************************************************************
# 1-) Class Tanımlanması 
# from pyexpat import model


# class Ogrenci():
    
#     okul_adi = "Celal Bayar"
#     tahsil_duzeyi = "Lisans"
#     ogrenci_sayisi = 0
    

#     def __init__(self,name,number,orgun):
#         self.ogrenci_adi = name
#         self.ogrenci_numarasi = int(number)
#         self.devamsizlik = 0 
#         self.orgunluk = orgun 
#         Ogrenci.ogrenci_sayisi_arttir()
        
    
#     def devamsizlik_kontrol(self):
#         self.devamsizlik += 1 
    
#     def ogrenim_sekli(self):
#         if(self.orgunluk == True):
#             print("Öğrenci Örgündür")
#         else:
#             print("Öğrenci Açık Öğretimdedir")

#     def bilgi(self):
#         print(f"Öğrencinin adı:{self.ogrenci_adi}")
#         print(f"Öğrencinin numarası:{self.ogrenci_numarasi}")
#         print(f"Öğrencinin devansızlık:{self.devamsizlik}")
    
#     @classmethod
#     def ogrenci_sayisi_arttir(cls):
#         Ogrenci.ogrenci_sayisi += 1 


# omer = Ogrenci("Ömer","1234",True)
# furkan = Ogrenci("Ömer","1234",True)
# ahmet = Ogrenci("Ömer","1234",True)


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
#     tur = "Motorlu Taşıt"
#     arac_sayisi = 0

#     def __init__(self,marka,model,var):
#         self.marka = marka 
#         self.model = model
#         self.kasko = var
    
#     @classmethod
#     def arac_sayisi_arttir(cls):
#         Arac.arac_sayisi += 1

#     def calistir(self):
#         print("Araç Çalıştı")
#     def kapat(self):
#         print("Kontak Kapandı")
#     def sigorta(self):
#         if(self.kasko == True):
#             print("Araç Kaskolu")
#         else:
#             print("Kasko Yok")
    
# class Otomobil(Arac):
#     def __init__(self,marka,model,var,kapasite):
#         Arac.__init__(self,marka,model,var)
#         self.kapasite = kapasite


# class Otobus():
#     def __init__(self,marka,model,var,kapasite):
#         super().__init__(self,marka,model,var)
#         self.kapasite = kapasite
#     def calistir():
#         print("Otobüs Çalıştı")
         



# arac_1 = Arac("Mercedes","e200",True,5)

# arac_2 = Otomobil("BMW","500d",True,5)

# arac_3 = Otobus("Audi","Setra",True,50)
  
# class Kisi():
#     def __init__(self,ad,soyad,tc):
#         self.ad = ad
#         self.soyad = soyad
#         self.__tc = tc 
#     # değeri görmek için get ile alamız gerekir
#     # def get_tc(self):
#     #     return self.__tc
#     # değeri değiştirmek için set metodu kullanmamız gerekir
#     # def set_tc(self,yenitc):
#     #     self.__tc = yenitc 

#     @property
#     def tc(self):
#         return self.__tc

#     @tc.setter
#     def tc(self,yenitc):
#         self.__tc = yenitc

#     @tc.deleter
#     def tc(self):
#         del self.__tc 
# kisi_1 = Kisi("Ahmet","Yılmaz",12345)

# kisi_1.tc = 23455

# print(kisi_1.tc)




#****************************************** MODÜLLER *************************************************************
# bilgi = "bu bir modül dosyasıdır"
# def bilgilerigoster(ad,soyad,yas):
#     print(f"""
#             Ad: {ad}
#             Soyad: {soyad}
#             Yaş: {yas}
#     """)

# class Bilgi():
#     bilgi= "bilgi"
#     def __init__(self):
#         self.bilgler = "bu bir bilgi"


# liste = [1,2,3,4]


# bilgi_1 = Bilgi()
# 2-) İmport Yöntemleri 

# 1. Yöntem (import)


# 2. Yöntem (from import)


# 3. Yöntem  (from modül import *)
 


# 4. Yöntem (as)


# 5. Yöntem (from iee import bilgi as bg)
 

# 3-) BUİLT-İN MODULES

# 1. Random Modülü 
# 2. Datetime Modülü 

