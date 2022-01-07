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

#************************** FONKSİYONLARIN TANIMLANMASI ********************************
# 1-) Fonksiyonların Tanımlanması
# def birinci_fonksiyon():
#     print("Merhaba Dünya") 

# def topla():
#     a = 10
#     b = 20
#     print(a+b)
# topla()
# birinci_fonksiyon()
# 2-) Fonksiyondan Değer Döndürme (Return)
# def toplama():
#     a = 10
#     b = 30
#     return a + b
# sonuc = toplama()  
# print(sonuc) 

# def merhaba():
#     return "merhaba dünya"

# sonuc_1 = merhaba()
# print(sonuc_1)
# 3-) Fonksiyona Parametre Gönderme(Fonksiyonun temel bileşenleri = girdi işlem ve çıktı)
# def merhaba(isim):
#     return "Merhaba " + isim + " bugün nasılsın?"

# sonuc = merhaba("Ömer")
# print(sonuc)

# def topla(a,b):
#     return a+b  
# sonuc = topla(15,20)    
# print(sonuc)

# def hesap_makinesi(a,b):
#     a = int(a)
#     b = int(b)
#     toplama = a+b
#     cikarma = a-b
#     carpma = a*b
#     bolme = a/b
#     sonuc_toplama = f"a ve b sayılarının toplamı = {toplama}"
#     sonuc_cikarma = f"a ve b sayılarının farkı = {cikarma}"
#     sonuc_carpma = f"a ve b sayılarının çarpımı = {carpma}"
#     sonuc_bolme = f"a ve b sayılarının bölümü = {bolme}"
#     return sonuc_toplama , sonuc_cikarma , sonuc_carpma , sonuc_bolme
# sonuc = hesap_makinesi(576,371)    
# print(sonuc)

# 4-) İç İçe Fonksiyonlar
# Ehliyet almak için yaş uygunluğunu tespit eden bir uygulama yazınız.
# İki farklı fonksiyon kullanılsın.
# İf - else ve döngülerin kullanımıda uygulamaya dahil olsun.
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
# # for x,y,z in kisiler:
# #      ehliyet(x,y,z)

# # ehliyet("Ahmet","Yılmaz",2008)
# ehliyet("Ali","Kars",2013)








# Maaşı 5000 TL olan bir kişinin harcamalarına yönelik bir program yazınız. 
# Geliştirilecek programda harcamalar değişken olarak tanımlanacak ve maaş limitine göre
#  "... miktarında alış veriş daha yapabilirsiniz" veya ".. limiti .... kadar aştınız, 
#  bazı harcamaları çıkarmanız gerekli..." vb uyarıları da kapsamalı.
# Eğer limit aşımı varsa değişkenleri tekrar isteyen bir uygulama olsun
#fonksiyon , döngüler , koşul ifadeleri , operatörler

def harcama():
    while True:
        maas = 5000
        faturalar = int(input("Fatura miktarını giriniz: "))
        kredi_borcu = int(input("Kredi Borcu Giriniz: "))
        genel = int(input("Genel toplam harcamaları giriniz: "))
        toplam_gider = faturalar + kredi_borcu + genel
        kalan = maas - toplam_gider
        if (maas > toplam_gider):
            print(f"Tebrikler bu ayki gideriniz gelirinizden az {kalan} miktarınız ile harcamalarınıza devam edebilirsiniz")
            break
        else:
            print(f"Maalesef limit aşımına uğradınız bu ayki harcamanız {toplam_gider}")
            print(f"Bu ay eksilerdesiniz eksi değeriniz {kalan}")
            print("Harcamalarınıza daha dikkat ediniz.")
            continue    
harcama()        