# ********************************* BUİLT-İN MODULES ************************************** #
# *********************************  DAHİLİ MODÜLLER   ************************************ #
# PYPİ.ORG 

# 1-) Random Modülü 
import random 

# icerik = dir(random)
# icerik = help(random)
# print(icerik)
rastgele_1 = random.random()
rastgele_2 = random.randint(0,100) #int bir değer üretir
rastgele_3 = random.uniform(0,100) #float bir değer üretir 
liste_1 = range(100)
liste_2 = [1,2,3,4.3,"Ali","Veli",True,False]
random.shuffle(liste_2)
rastgele_4 = random.sample(liste_1,3)
rastgele_5 = random.choice(liste_2)
# print(rastgele_1)
# print(rastgele_2)
# print(rastgele_3)
# print(rastgele_4)
# print(liste_2)
# print(rastgele_5)

# 2-) Datetime Modülü 

# import datetime 

# x = dir(datetime)
# print(x)
from datetime import datetime,timedelta
import locale 
locale.setlocale(locale.LC_ALL,"turkish")

tarih_1 = datetime.now() 
tarih_2 = datetime.today()
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

#strftime
 
istenilen = datetime.strftime(tarih_1,"%a")
istenilen = datetime.strftime(tarih_1,"%A")
istenilen = datetime.strftime(tarih_1,"%B")
istenilen = datetime.strftime(tarih_1,"%b")
istenilen = datetime.strftime(tarih_1,"%H")
istenilen = datetime.strftime(tarih_1,"%j")
istenilen = datetime.strftime(tarih_1,"%A")
istenilen = datetime.strftime(tarih_1,"%B")
istenilen = datetime.strftime(tarih_1,"%B %A %H %Y") 

tarih_3 = datetime(1999,4,21,22,15,45)
print(tarih_3)

tarih_1_saniye = datetime.timestamp(tarih_1)
tarih_3_saniye = datetime.timestamp(tarih_3)
tarih_1_normal_tarih = datetime.fromtimestamp(tarih_1_saniye)
tarih_3_normal_tarih = datetime.fromtimestamp(tarih_3_saniye)
baslangic = datetime.fromtimestamp(0)
# print(tarih_1_saniye)
# print(tarih_3_saniye)
# print(tarih_1_normal_tarih)
# print(tarih_3_normal_tarih)
# print(baslangic)

# tarih_hesabi = tarih_1 - tarih_3
# print(tarih_hesabi) 

ileri_tarih = tarih_1 + timedelta(days=3000)
geri_tarih = tarih_1 - timedelta(days=3000)
print(ileri_tarih)
print(geri_tarih)

