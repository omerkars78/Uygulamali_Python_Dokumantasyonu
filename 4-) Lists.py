#************************************** LİSTELER *************************************
# 1-) Liste Nedir Nasıl Tanımlanır ?
# liste1 = [int(1),float(1.1),str("String"),True,False]
# print(liste1)
# liste2 = [1,2,3,4,5,1.5,45.5]
# liste3 = ["name","surname","age"]
#  - Liste İşlemleri (index)
# print(liste1[1])
# print(liste1[0:4])
# print(liste3[-2:])
# print(liste2[:])
# liste4 = liste2[:]
# print(liste4)
#  - İç İçe Liste
# liste5 = [1,2,3,["name","surname","age"],True,[1,2,[3,4,[5,6,7,8]]],9]
# print(liste5[0])
# print(liste5[3])
# print(liste5[3][1])
# print(liste5[5])
# print(liste5[5][2])
# print(liste5[5][2][2])
# print(liste5[5][2][2][1])
#  - Liste Birleştirme
# liste6 = liste3+liste4+liste5+liste1
# print(liste6)

# 2-) Liste Metodları Nelerdir Nasıl Kullanılır?
# Sadece listerde kullanırız
# İşlerimiz kolaylaştırır
#  - Append (ekleme)
# list1 = [0,1,2,3,4,5,6,7,8,9]
# list1.append(10)
# print(list1)
#  - İnsert (indekse göre ekleme)
# list1.insert(0,5)
# print(list1)
#  - Pop (Son elemanı çıkarma)
# list1.pop()
# print(list1)
#  - Remove (Seçili elemanı çıkarma)
# list1.remove(1)
# print(list1)
#  - Del (İstenilen yerleri silme)
# del list1[0:5]
# print(list1)
#  - Count (İstenilen Elemanın Kaç Adet olduğunu bulma)
# kac_adet = list1.count(5)
# kac_adet = list1.count(2)
# print(kac_adet)
#  - İndex(İstenilen Elemanın İndexini Bulma)
# hangi_index = list1.index(4)
# print(hangi_index)
#  - Reverse(Tersine Çevirme)
# list1.reverse()
# print(list1)
#  - Sort(Harf Sırasına Göre Sıralama)
# list2 = ["w","x","f","e","k","p"]
# list2.sort()
# print(list2)

# 3-) TUPLES 
# tuples_1 = (1,2,"üç",3.5,True)
# list_1 = [1,2,"üç",3.5,True]
# print(type(list_1))
# print(type(tuples_1))
# Öğelere Erişim Ortaktır
# print(list_1[0])
# print(tuples_1[2])
# Len Fonksiyonu Ortaktır
# print(len(tuples_1))
# print(len(list_1))
# Count Metodu Ortaktır
# kac_tane1 = tuples_1.count(3.5)
# kac_tane2 = list_1.count("üç")
# print(kac_tane1)
# print(kac_tane2)
# İndex Metodu Ortaktır
# kac_tane1 = tuples_1.index(3.5)
# kac_tane2 = list_1.index("üç")
# print(kac_tane1)
# print(kac_tane2)
# Tuple Birleştirme
# tuples_2 = 1,2,3,4,5
# tuples_3 = tuples_1+tuples_2
# print(tuples_3)
# Listeyi Tuple'a Çevirme
# list_1 = tuple(list_1)
# print(type(list_1))
# print(list_1)

# 4-) Dictionary
# - Dictionary Nedir? Nasıl Tanımlanır? 
# plaka_kodu = {
#     "Karabük":78,
#     "Kastamonu":37,
#     "Bartın": 74
# }
# # print(type(plaka_kodu))

# plaka_kodu["artvin"] = 9
# plaka_kodu["artvin"] = 8
# print(plaka_kodu)
personel = {
    300 : {
        "Ad" : "Ömer",
        "Birim" : "Bilgi İşlem",
        "Cinsiyet" : "Erkek",
        "Maaş" : [1000,1200,1400]
    },
    301 : {
        "Ad" : "Şevket",
        "Birim" : "Teknik Servis",
        "Cinsiyet" : "Erkek",
        "Maaş" : [1000,1200,1400]
    },
    302 : {
        "Ad" : "Ayşe",
        "Birim" : "Muhasebe",
        "Cinsiyet" : "Kız",
        "Maaş" : [1000,1200,1400]
    }
}
# print(personel)
# print(personel[300])
# print(personel[301]["Ad"])
# print(personel[301]["Maaş"][1])
# maas_ort_301 = (personel[301]["Maaş"][0]+personel[301]["Maaş"][1]+personel[301]["Maaş"][2])/3
# print(f"301 nolu personelin 3 aylık maaş ortalamsı:{maas_ort_301}")


# - Dictionary Metodları
bilgi = {
    "ad":"Ömer",
    "soyad":"Kars",
    "Yaş": 20
}
# - keys()(Anahatarları liste olarak sıralar)
# print(bilgi.keys())
# - values()(Value değerlerini liste olarak sıralar)
# print(bilgi.values())
# - items()(key ve valueları aynı anda sıralar)
# print(bilgi.items())
# - get()(sözlük elemanını alırız)
# print(bilgi["ad"])
# print(bilgi.get("ad"))
# - pop()(istenilen anahtarı siler)
# bilgi.pop("soyad")
# print(bilgi)
# - copy()(sözlüğün kopyasını alır bununla alının kopya aslını etkilemez)
# kopya = bilgi.copy()
# print(kopya)
# - update()(Verileri güncellememize yarar)
bilgi.update({
    "ad":"Hüseyin",
    "memleket":"Kastamonu"
})
print(bilgi)