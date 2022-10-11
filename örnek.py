# kisiler = [("Ömer","Kars",2001),("Can","Yorulmaz",2005),("Çağrı","Açıkgöz",1998)]
# def yas_hesapla(dogum_tarihi):
#     return 2021 - dogum_tarihi      
# def ehliyet(isim,soyisim,dogum_tarihi):
#     yas = yas_hesapla(dogum_tarihi)
#     yas = int(yas) 
#     sure = 18 - yas
#     if (yas < 18):
#         print(f"Sayın {isim} {soyisim} yaşınız {yas} olduğu için ehliyet alamazsınız. ")
#         print(f"Ehliyet alabilmek için {sure} kadar sene sonra başvurabilirsiniz.")
#     else:
#         print(f"Sayın {isim} {soyisim} yaşınız uygundur ehliyet başvurusu yapabilirsiniz. ")    
# for x,y,z in kisiler:
#      ehliyet(x,y,z)

# class Ogrenci():
#     okul_adi = "Harvard"
#     tahsil_duzeyi = "Lisans"
#     ogrenci_sayisi = 0
    
#     def __init__(self,ad,bolum,orgun):
#         # Ogrenci.ogrenci_sayisi +=1 
#         Ogrenci.ogrenci_sayisi_arttir()
#         self.ogrenci_adi = ad
#         self.bolum = bolum
#         self.devamsizlik = 0
#         self.ogrenim_durumu = orgun
    
#     def devamsizlik_kontrol(self):    
#         self.devamsizlik += 1
#         print("Ogrenci Devamsızlık Yaptı")

#     def ogrenim_sekli(self):
#         if self.ogrenim_durumu == True:
#             print("Öğrenci örgün eğitime tabiidir.")
#         else:
#             print("Öğrenci uzaktan eğitime tabiidir")

#     def bilgileri_goster(self):
#         print("Öğrencinin adı: ",self.ogrenci_adi)
#         print("Öğrencinin bölümü: ",self.bolum)
#         print("Öğrencinin Okula Gelmediği Gün Sayısı: ",self.devamsizlik)

#     @classmethod
#     def ogrenci_sayisi_arttir(cls):
#         Ogrenci.ogrenci_sayisi +=1 

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
#         print("Araç çalıştı")

#     def kapat(self):
#         print("Kontak kapandı.")

#     def sigorta(self):
#         if self.kasko == True:
#             print("Araç kaskolu")
#         else:
#             print("Araç kaskosuz.")

# class Otomobil(Arac):
#     def __init__(self,marka,model,var):
#         Arac.__init__(self,marka,model,var)
#         self.kapasite = "4"


# class Otobüs(Arac):
#     def __init__(self,marka,model,var,kapasite):
#         super().__init__(marka,model,var)
#         self.kapasite = kapasite
#     def calistir(self):
#         print("Otobüs çalıştı")


# class Kisi():
#     def __init__(self,ad,soyad,id):
#         self.kisi_adi = ad 
#         self.kisi_soyadi = soyad 
#         self.__kisi_id = id
#     def get_id_show(self):
#         return self.__kisi_id
#     def set_id(self,new_id):
#         self.__kisi_id = new_id
    
#     @property
#     def id_gor(self):
#         return self.__kisi_id

#     @id_gor.setter
#     def id_gor(self,yeni_id):
#         self.__kisi_id = yeni_id

#     @id_gor.deleter
#     def id_gor(self):
#         del self.__kisi_id

# # kisi_1.id_gor = 345
# # kisi_1.id_gor()

# import random 
# rastgele_1 = random.random()
# rastgele_2 = random.randint(0,100) #int bir değer üretir
# rastgele_3 = random.uniform(0,100) #float bir değer üretir 
# liste_1 = range(100)
# liste_2 = [1,2,3,4.3,"Ali","Veli",True,False]
# random.shuffle(liste_2)
# rastgele_4 = random.sample(liste_1,3)
# rastgele_5 = random.choice(liste_2)



# from datetime import datetime,timedelta

# x = dir(datetime)
# print(x)
# from datetime import datetime,timedelta
# import locale 
# #locale.setlocale(locale.LC_ALL,"turkish") #sonradan

# tarih_1 = datetime.now() 
# tarih_2 = datetime.today()
# print(tarih_1)
# print(tarih_2)
# print(tarih_1.year)
# print(tarih_1.month)
# print(tarih_1.day)
# print(tarih_1.hour)
# print(tarih_1.minute)
# print(tarih_1.second)

# tarih_3 = datetime.ctime(tarih_1)
# print(tarih_3)

# #strftime
 
# istenilen = datetime.strftime(tarih_1,"%a")
# istenilen = datetime.strftime(tarih_1,"%A")
# istenilen = datetime.strftime(tarih_1,"%B")
# istenilen = datetime.strftime(tarih_1,"%b")
# istenilen = datetime.strftime(tarih_1,"%H")
# istenilen = datetime.strftime(tarih_1,"%j")
# istenilen = datetime.strftime(tarih_1,"%A")
# istenilen = datetime.strftime(tarih_1,"%B")
# istenilen = datetime.strftime(tarih_1,"%B %A %H %Y") 

# tarih_3 = datetime(1999,4,21,22,15,45)
# print(tarih_3)

# tarih_1_saniye = datetime.timestamp(tarih_1)
# tarih_3_saniye = datetime.timestamp(tarih_3)
# tarih_1_normal_tarih = datetime.fromtimestamp(tarih_1_saniye)
# tarih_3_normal_tarih = datetime.fromtimestamp(tarih_3_saniye)
# baslangic = datetime.fromtimestamp(0)


# tarih_hesabi = tarih_1 - tarih_3
# print(tarih_hesabi) 

# ileri_tarih = tarih_1 + timedelta(days=3000)
# geri_tarih = tarih_1 - timedelta(days=3000)
# print(ileri_tarih)
# print(geri_tarih)

# Integer 
# print(type(5))
from tarfile import GNUTYPE_LONGLINK
from typing import final


int(5) 
int(6)

# float 
# -1.1 , -56.02 , 7.000007653
# print(type(-1.1)) 
# float(1.1) 

# print(int(1.1))
# print(float(5)) 

# +,-,*,/,**,% 
# print(1+1)
# print(float(6-1))
# print(6*6)
# print(int(100/10)) # bölme sonuçları float gelir
# print(2**4)
# print(int(71/9))
# sayi_1 = 9 
# print(sayi_1)

# _sayi =5 
# print(_sayi)

# adSoyad  = "Ömer Kars"
# ad_soyad = "Ömer Kars"
# AdSoyad = "Ömer Kars"

# age = 20
# Age = 16 
# AGE = 17 
# age = 25
# print(age)
# print(Age)
# print(AGE)

# vize_notu = 50 
# final_notu = 60 
# vize_etki = 0.5
# final_etki = 0.6
# gecme_notu = int((vize_notu*vize_etki) + (final_notu* final_etki))
# print(gecme_notu)

# yazi_1 = "Bu bir stringtir" 
# yazi_1 = str("Bu bir stringtir" )
# sayi_1 = str(5)
# sayi_2 = str(6)
# print(sayi_1+sayi_2)
# print(type(yazi_1))

# yazi_1 = "Çift tırnaklı gösterim"
# yazi_2 = 'Tek tırnaklı gösterim'
# yazi_3 = "Bu bir 'ikili' gösterimdir "
# yazi_4 = 'Bu bir "ikili" gösterimdir '

# print(yazi_1)
# print(yazi_2)
# print(yazi_3)
# print(yazi_4) 

ad = "Ömer" 
soyad = " Kars"
yas = " 21"
cumle = ad + soyad + yas + " yaşındadır"
# print(cumle)
# print(ad[1])
# print(cumle[15])
# print(cumle[0:15])
# print(cumle[-10:-1])
# print(cumle[6::2])

# print(len(cumle))
# print(cumle.upper())
# print(cumle.lower())
# print(cumle.startswith("Hasan"))
# print(cumle.endswith("yaşındadır1212"))
# print(cumle.split())
# # cumle_list = cumle.split() 

# # print(cumle_list)
# # replace 
# gunluk = "Ömer bugün markete gitti. Ömer marketten süt aldı. Ömer okula gitti." 
# gunluk.replace("Ömer","Ahmet")
# print(gunluk.replace("Ö","o")) 
# print(gunluk.count("a"))

# format metodu 
# ad = "Ömer" 
# soyad = " Kars"
# yas = " 21"
# cumle = "{} {} {} yaşında bir gençtir.".format(ad,soyad,yas)
# cumle = f"{ad} {soyad} {yas} yaşında bir gençtir."
# print(cumle)  

list_1 = [1,2,3,2.1,"ali","veli",False,True,ad]
# print(list_1[0:5])
list_2 = [1,2,3,4,[6,7,8,[9,[10,[11]]]],12,13]
# print(list_2)
# print(list_2[4])
# print(list_2[4][3])
# print(list_2[4][3][1])
# print(list_2[4][3][1][1])
# print(list_2[4][3][1][1][0])
# list_3 = list_1 + list_2 

# print(list_3)

# list_3 = [1,2,3,4,5,1,1,1,1,1,1,2,3,3,3,2,3]

# list_3.append(6)
# list_3.insert(0,"ilk")
# list_3.insert(6,7)
# list_3.pop()
# list_3.remove("ilk")
# del list_3[0:2]
# # print(list_3.count(3))
# list_3.reverse()
# print(list_3)

list_3 = ["a","b","p","c","k","s"]
list_3.sort()
print(list_3)