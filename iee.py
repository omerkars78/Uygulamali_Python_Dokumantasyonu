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
#print(sayi_1*sayi_2)
# print(3*4)
# 2-) Değişken tanımlama Kuralları Nelerdir? 

# - Sayı ile Başlayamaz
# degisken = 4
# # - Boşluk İçeremez
# birinciSayi = 1
# # - Büyük Küçük Harf Farklılığı Vardır
# age = 3
# AGE = 5
# aGe = 8 
# age = 10
# print(age)
# print(AGE)
# print(aGe)
# # - Yan Yana Değer Ataması Yapılabilir
# x,y,z = 1,2,3
# # - Türkçe Karakter İçermese Güzel Olur
# #ı,ü,ö,ğ
# # 3-) Değişkenlerle İlgili Uygulamalar(vize final notu )

# vize_notu = 70
# final_notu = 60 
# vize_etki = 0.5 
# final_etki = 0.5
# gecme_notu = int((vize_notu*vize_etki) + (final_notu*final_etki))
# print(gecme_notu)




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
# lower_1 = "merhaba bu bir mesajdır"
# lower_2 = "BU FARKLI BİR ŞEYDİR"
# print(lower_1.upper())
# print(lower_2.lower())
# #  - Startswith ve Endswith Fonksiyonları
# print(lower_1.startswith("merhaba"))
# print(lower_1.startswith("selam"))
# print(lower_1.endswith("mesajdır"))
# print(lower_1.endswith("selam"))
# #  - Split Fonksiyonu (Ayrıma)
# print(lower_1.split())
# liste_split = lower_1.split()
# print(liste_split)
# #  - Replace Fonksiyonu (Cümle Değiştirme)
# gunluk = "Ömer bugün okula gitti. Ömer okuldan geldi. Ömer uyudu"
# # print(gunluk.replace("Ö","O"))
# # Format Metodu 
# ad = "Ömer"
# soyad = "Kars"
# yas = 21 
# cumle = "{} {} {} Yaşındadır.".format(ad,soyad,yas)
# cumle = f"{ad} {soyad} {yas} Yaşındadır."
# print(cumle)



# #****************************************** LİSTELER *************************************************************
# # 1-) Liste Nedir Nasıl Tanımlanır ?
# ad = "Ömer"
# list_1 = [1,2,3,1.1,2.3,"ali",True,False,ad]
# print(list_1)
# #  - Liste İşlemleri (index)
# print(list_1[8])
# print(list_1[0:5])
# #  - İç İçe Liste
# list_2 = [1,2,3,[4,5,[6,[7,[8]]]],9]
# print(list_2)
# print(list_2[3])
# print(list_2[3][2])
# print(list_2[3][2])
# print(list_2[3][2][1])
# print(list_2[3][2][1][1])
# print(list_2[3][2][1][1][0])
# sekiz = list_2[3][2][1][1][0]
# print(sekiz+10)
# # 2-) Liste Metodları Nelerdir Nasıl Kullanılır?
# #https://python-istihza.yazbel.com/listelerin_ve_demetlerin_metotlari.html
# # * Sadece listerde kullanırız
# # * İşlerimiz kolaylaştırır
# list_3 = [1,2,3,4,5,5,5,True,5,5,1,1,1,1,1,1]
# #  - Append (ekleme)

# list_3.append(6)

# #  - İnsert (indekse göre ekleme)
# list_3.insert(0,"ali")
# print(list_3)
# #  - Pop (Son elemanı çıkarma)

# list_3.pop()
# print(list_3)
# #  - Remove (Seçili elemanı çıkarma)
# list_3.remove("ali")
# print(list_3)

# #  - Del (İstenilen yerleri silme)

# del list_3[0:2]
# print(list_3)
# #  - Count (İstenilen Elemanın Kaç Adet olduğunu bulma)
# print(list_3.count(1))
# #  - İndex(İstenilen Elemanın İndexini Bulma)
# print(list_3.index(True))
# #  - Reverse(Tersine Çevirme)

# list_3.reverse()
# print(list_3)
# #  - Sort(Harf Sırasına Göre Sıralama)
# list_4 = ["s","d","k","l","a"]
# list_4.sort()
# print(list_4)

# # 3-) TUPLES 
# tuple_1 = 1,2,3,4,"Ömer"
# tuple_1 = (1,2,3,4,"Ömer")
# print(type(tuple_1))
# # - Öğelere Erişim Ortaktır

# # - Len Metodu Ortaktır

# # - Count Metodu Ortaktır

# # - İndex Metodu Ortaktır

# # - Tuple Birleştirme


# # 4-) Dictionary
# # - Dictionary Nedir? Nasıl Tanımlanır? 
# omer = {
#     "Ad":"Ömer",
#     "Soyad":"Kars",
#     "Yas": 21 
# }
# calisan = {
#     301:{
#         "Ad":"Ömer",
#         "Soyad":"Kars",
#         "Yas": 21,
#         "Departman":"Muhasebe",
#         "Maas":1000
#     },
#     302:{
#         "Ad":"Furkan",
#         "Soyad":"Anter",
#         "Yas": 23,
#         "Departman":"Blockchain Developer",
#         "Maas":1000000
#     }
# }
# # print(type(omer))
# # print(omer["Ad"])
# # print(omer["Soyad"])
# print(calisan[301]["Maas"])
# print(calisan[302]["Maas"]) 
# ortalama = ((calisan[301]["Maas"]) + (calisan[302]["Maas"]))/2
# print(ortalama)
# # # - Dictionary Metodları

# # # - keys()(Anahatarları liste olarak sıralar)
# print(calisan.keys())
# # # - values()(Value değerlerini liste olarak sıralar)
# print(calisan.values())
# # # - items()(key ve valueları aynı anda sıralar)
# print(calisan.items())
# # # - get()(sözlük elemanını alırız)
# print(calisan.get(301))
# # # - pop()(istenilen keyi siler)
# print(calisan.pop(301))
# print(calisan)
# # # - copy()(sözlüğün kopyasını alır bununla alının kopya aslını etkilemez)
# calisan_2 = calisan.copy()
# print(calisan_2)
# # # - update()(Verileri güncellememize yarar)(({}))

# calisan_2.update({
#     302:{
#         "Ad":"Ali",
#         "Soyad":"Anter",
#         "Yas": 23,
#         "Departman":"Blockchain Developer",
#         "Maas":1000000
#     }
# })

# print(calisan_2)




# #****************************************** OPERATÖRLER *************************************************************
# # 1-) Artimetik Operatörler 
# # (+),(-),(*),(/),(%),(**)

# # 2-) Atama Operatörleri
# # - Eşittir Operatörü(=)
# deger =7
# # # - Artı Eşittir Operatörü(+=)
# deger += 1
# print(deger)
# # # - Eksi Eşittir Operatörü(-=)
# deger -= 1
# print(deger)
# # # - Çarpı Eşittir Operatörü(*=)
# deger *= 4
# print(deger)
# # # - Bölü Eşittir Operatörü(/=)
# deger /= 4
# print(deger)
# # # - Mod Eşittir Operatörü(%=)
# deger %= 4
# print(deger)
# # # 3-) Karşılaştırma Operatörleri(Sonucun True veya False değerlerini Aldığımız Operatörler)
# # # - Eşittir Operatörü(==)
# print("Ömer"=="Ömer")
# print("Ömer"=="Furkan")
# # # - Eşit Değildir Operatörü(!=)
# print("Ömer"!="Furkan")
# print("Ömer"!="Ömer")
# # # - Büyüktür Operatörü(>)
# print(4>3)
# # # - Küçüktür Operatörü(<)
# print(4<3)
# # # - Büyük Eşittir Operatörü(>=)
# print(2>=3)
# # # - Küçük Eşittir Operatörü(<=)
# print(2<=3)
# # # 4-) Mantıksal Operatörler(Sonucunda True veya False Değer Aldığımız Operatörlerdir)
# # # - And Operatörü
# print(3==3 and 4==5)
# # # And operatöründe True bir sonuç almak için her iki ifadeninde doğru olması gerekir.
# # # - Or Operatörü
# print(3==4 or 4==5)
# Or operatöründe True bir sonuç almak için her iki ifadenin veya yanlızca birinin doğru olması yeterlidir.





#****************************************** KOŞULLU İFADELER *************************************************************
# 1-) If ve ELse Nedir Nasıl ve Nerelerde Kullanılır ?
# a,b,c = 1,2,1
# if(a==b):
#     print("a b'ye eşittir")
#     print(a+b)
# else:
#     print("a b'ye eşit değil")
#     print(a+b+c)

# username = input("Kullanıcı Adı Giriniz: ")
# password = input("Şifre Giriniz: ") 
# if(username == "omer" and password=="123"):
#     print("Tebrikler Kullanıcı Adı ve Şifre doğru")
# else:
#     print("Kullanıcı Adı veya Şifre Hatalı")
# 2-) Elif Bloğu Nedir Hangi durumlarda Kullanılır ?
# animal_name = input("Bir hayvan adı giriniz: ")
# if(animal_name == "kuş"):
#     print("Evet Kuş Gerçekten bir hayvandır")
# elif(animal_name == "kedi"):
#     print("Evet Kedi Gerçekten bir hayvandır")
# elif(animal_name == "at"):
#     print("Evet at Gerçekten bir hayvandır")
# elif(animal_name == "köpek"):
#     print("Evet Köpek Gerçekten bir hayvandır")

# else:
#     print(f"{animal_name} gerçekten bir hayvan mıdır?")


# 4-) Elif Uygulaması




#****************************************** DÖNGÜLER *************************************************************
# 1-) For Döngüleri Nedir? Ne İşe Yarar? Nasıl Tanımlanır ?
list = [300,400,500]
# print(list[0]+50)
# print(list[1]+50)
# print(list[2]+50)

# for i in list: 
#     print(i+50)
# # 2-) While Döngüleri Nedir ve Nasıl Tanımlanır?

i = 0
# while (i<100): 
#     i += 1
#     if (i%2) == 1:
#         print("Sayı Tektir")
#     else:
#         print("Sayı Çifttir")
    


# while True:
#     esek_yolu = input("Eşek Nereden geldi: ")
#     if(esek_yolu == "Sudan"):
#         print("Eşek Sudan geldi Tebrikler")
#         break 
#     else:
#         print("maalesef eşek yanlış yoldan geldi")
#     continue
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
# def toplama():
#     a= 5
#     b=6 
#     print(a+b) 

# toplama()
# 2-) Fonksiyondan Değer Döndürme (Return)
# def topla():
#     a=6
#     b=7
#     return a+b
# topla()
# print(topla())
# def hesap_makinesi(a,b):
#     return a+b 

# print(hesap_makinesi(4,6))

# 3-) Fonksiyona Parametre Gönderme(Fonksiyonun temel bileşenleri = girdi işlem ve çıktı)

# 4-) İç İçe Fonksiyonlar

# 5-) Uygulama
# kisiler = [("Ömer","Kars",2005),("Furkan","Anter",1999),("Kadir","Hoca",1960)]
# def yas_hesapla(dogum_tarihi):
#     return 2022 - dogum_tarihi
# def ehliyet(isim,soyisim,dogum_tarihi):
#     yas = yas_hesapla(dogum_tarihi)
#     yas = int(yas) 
#     sure = 18 - yas 
#     if(yas < 18):
#         print(f"Sayın {isim} {soyisim} yaşınız {yas} ehliyet alamazsın. {sure} kadar yıl beklemelisin")
#     else:
#         print(f"Sayın {isim} {soyisim} yaşınız {yas} olduğu için ehliyet alabilirsin")

# for x,y,z in kisiler: 
#     ehliyet(x,y,z)




#****************************************** NESNE TABANLI PROGRAMLAMA *************************************************************
# 1-) Class Tanımlanması 
class Ogrenci():
    okul_adi = "Celal Bayar"
    tahsil_duzeyi = "Lisans"
    ogreci_sayisi = 0 

    def __init__(self,ad,soyad):
        self.ogrenci_adi = ad
        self.ogreci_soyadi = soyad
        self.devamsizlik = 0 

    def devamsizlik_kontrol(self):
        self.devamsizlik +=1 
        print("Öğrenci Devamsızlık Yaptı") 

    @classmethod
    def ogrenci_sayisi_arttir(cls):
        Ogrenci.ogreci_sayisi += 1 
    
furkan = Ogrenci("Furkan","Anter")
omer = Ogrenci("Ömer","Kars") 
omer.devamsizlik_kontrol()
omer.devamsizlik_kontrol()
omer.devamsizlik_kontrol()
Ogrenci.ogrenci_sayisi_arttir()
Ogrenci.ogrenci_sayisi_arttir()
Ogrenci.ogrenci_sayisi_arttir()
Ogrenci.ogrenci_sayisi_arttir()
print(Ogrenci.ogreci_sayisi)




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
 

