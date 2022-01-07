#************************ FOR DÖNGÜLERİ ******************************
# 1-) For Döngüleri Nedir? Ne İşe Yarar? Nasıl Tanımlanır ?
# liste = [100,200,300]
# # print((liste[0])+5)
# # print((liste[1])+5)
# # print((liste[2])+5)
# for i in liste:# Listenin içerisini dön, elemanları tek tek işle ve bunları "geçici" i değişkenine ata
#     print(i+5) 
# liste_1 = (1,2.1,"Ömer",True)
# for a in liste_1:
#     print(a)
# isim = "Ömer Kars"
# for x in isim:
#     print(x)
# maaslar = {"a":1000,"b":2000}
# for i in maaslar.values():
#     print(i)
# for x in maaslar.items():
#     print(x)    

# *************************************** While Döngüleri ********************************************
# 1-) While Döngüleri Nedir ve Nasıl Tanımlanır?
# x = 0
# while x < 10:
#     x += 1
#     print("devam eder")
# 2-) While İle Neler Yapabiliriz?
# x = 0
# while x < 100:
#     x += 1
#     print(x%2)
# 3-) While Bloğu İçinde İf ve Else 
# x = 0
# while x < 100:
#     x += 1
#     if (x%2) == 1:
#         print(x,":Tek Sayı")
#     else:
#         print(x,": Çift Sayıdır")    
# 4-) Break ve Continue Nedir Ne İşe Yarar?
# while True:
#     esek_yolu = input("Eşek nereden geldi: ")
#     if esek_yolu == "Sudan":
#         print("TEBRİKLER EŞEK SUDAN GELDİ")
#         break
#     else:
#         continue
            
# def harcama():
#     while True:
#             sabit_gelir = 5000
#             faturalar = int(input("Bu ayki fatura toplamınız ne kadar: "))
#             gıda = int(input("Bu ayki gıda harcamlarınız ne kadar: "))
#             kredi_kartı = int(input("Bu ayki kredi kartı borcunuz ne kadar: "))
#             toplam_harcama = faturalar + gıda + kredi_kartı
#             kalan = sabit_gelir - toplam_harcama
#             if (toplam_harcama < sabit_gelir):
#                     print(f"Tebrikler! Bu ayki harcamanız {toplam_harcama} lira .")
#                     print(f"Bu ayki maaşınızdan {kalan} kadar miktarınız arttı ona göre harcamalarınızı yapabilirsiniz")
#                     break
#             else:
#                 print(f"UYARI! Bu ayki harcamanız {toplam_harcama} sabit gelirinizi aştı.") 
#                 print(f"Şu anda {kalan} değerindesiniz yani eksilerde :( ")
#                 print("Bazı harcamalarınızı kısmanızı öneririz.")   
#                 continue
# harcama()      

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

#     def sigorta(self):
#         if self.kasko == True:
#             print("Kaskosu Var")
#         else:
#             print("Kaskosu Yok")

# class Otomobil(Arac):
#     def __init__(self,marka,model,var):
#         Arac.__init__(self,marka,model,var)
#         self.kapasite = 4
#     def calistir(self):
#         print("otomobil Çalıştı")

# class Otobüs(Arac):
#     def __init__(self,marka,model,var):
#         super().__init__(marka,model,var)
#         self.kapasite = 50

# arac_1 = Arac("Mercedes",2005,True)
# arac_2 = Otomobil("Audi",2020,False)
# arac_3 = Otobüs("BMW",2021,True)
# # print(arac_1)
# # print(arac_2)
# # print(arac_3)
# # arac_2.calistir()
# # print(Otomobil.tur)
# # print(arac_3.kapasite)
# Otomobil.arac_sayisi_arttir()
# Otobüs.arac_sayisi_arttir()
# print(Otomobil.arac_sayisi)
# print(Arac.arac_sayisi)
# print(Otobüs.arac_sayisi)