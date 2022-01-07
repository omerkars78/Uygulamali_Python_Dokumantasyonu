#****************************** STRİNG VERİ TİPİ ***********************************
# 1-) String Veri Tipi Nedir
# sayi1 = "5" # string verileri tanımlarken parantez içine alırız
# sayi2 =  str(6)  #  veya başına str getiririz
# sonuc = sayi1 + sayi2 
# print(sonuc)
# 2-) String İşlemleri Nelerdir (İndeks Kavramı)
# "veri",'veri'
# print("veri tipi'nin ")
# name = 'Ömer'
# surname = " Kars "
# age = str(20)
# info = name + surname + age+ " " + "yaşında"
# print(info[:10])

# 3-) Stringle İlgili Fonksiyonlar
knowledge = "String Veriler Sayısal Bir Değere Sahip Değildir"
#  - Len (Uzunluk Fonksiyonu)
print(len(knowledge))
#  - Upper ve Lower Fonksiyonları 
print(knowledge.upper())
print(knowledge.lower())
#  - Find Fonksiyonu
print(knowledge.find("Veriler"))
#  - Startswith ve Endswith Fonksiyonları
print(knowledge.startswith("ab"))
print(knowledge.endswith("p"))
#  - Split Fonksiyonu (Ayrıma)
ayirilmis = knowledge.split()
print(ayirilmis)
#  - Replace Fonksiyonu (Cümle Değiştirme)
print(knowledge)
degistirme = knowledge.replace("String","İnteger")
print(degistirme)
degistirme_2 = degistirme.replace("Sahip Değildir","Sahiptir")
print(degistirme_2)
for sayi in range(10,0,-1):
    print('sıradaki sayı',sayi)