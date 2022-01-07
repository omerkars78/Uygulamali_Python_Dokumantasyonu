class Ogrenci():
    okul_adi = "Harvard"
    tahsil_duzeyi = "Lisans"
    ogrenci_sayisi = 0
    
    def __init__(self,ad,bolum,orgun):
        # Ogrenci.ogrenci_sayisi +=1 
        Ogrenci.ogrenci_sayisi_arttir()
        self.ogrenci_adi = ad
        self.bolum = bolum
        self.devamsizlik = 0
        self.ogrenim_durumu = orgun
    
    def devamsizlik_kontrol(self):    
        self.devamsizlik += 1
        print("Ogrenci Devamsızlık Yaptı")

    def ogrenim_sekli(self):
        if self.ogrenim_durumu == True:
            print("Öğrenci örgün eğitime tabiidir.")
        else:
            print("Öğrenci uzaktan eğitime tabiidir")

    def bilgileri_goster(self):
        print("Öğrencinin adı: ",self.ogrenci_adi)
        print("Öğrencinin bölümü: ",self.bolum)
        print("Öğrencinin Okula Gelmediği Gün Sayısı: ",self.devamsizlik)

    @classmethod
    def ogrenci_sayisi_arttir(cls):
        Ogrenci.ogrenci_sayisi +=1 

# omer = Ogrenci("Ömer","Muhasebe",True)
# omer = Ogrenci("Ömer","Muhasebe",True)
# omer = Ogrenci("Ömer","Muhasebe",True)
# omer = Ogrenci("Ömer","Muhasebe",True)
Ogrenci.ogrenci_sayisi_arttir()
Ogrenci.ogrenci_sayisi_arttir()
Ogrenci.ogrenci_sayisi_arttir()
Ogrenci.ogrenci_sayisi_arttir()

Ogrenci.ogrenci_sayisi_arttir()
Ogrenci.ogrenci_sayisi_arttir()

print(Ogrenci.ogrenci_sayisi)
    






