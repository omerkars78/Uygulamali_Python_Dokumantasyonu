#***************************** K A L I T I M *********************************

#Bütün Araçlarda ortak olan özellikler vardır.
#Ancak çeşitli motorlu taşıt türlerinin kendilerine ait farklı özellikleride bulunmaktadır.
#Bu sebepten dolayı diğer araç türleri üzerinden oluşturacağımız classlar için ayrı ayrı
#  (classlar ve Objeler için)
# Metod tanımlamaya gerek yoktur.
# Ortak Özellikte olanları zaten Araç classına tanımlamak yeterlidir.

# ATA => ÇOCUK => TORUN
# PARENT => CHİLD

#ÇALIŞIR , MARKASI , MODELİ , 
class Arac():
    
    tur = "Motorlu Taşıt"
    arac_sayisi = 0

    def __init__(self,marka,model,var):
        self.marka = marka
        self.model = model 
        self.kasko = var

    @classmethod
    def arac_sayisi_arttir(cls):
        Arac.arac_sayisi += 1

    def calistir(self):
        print("Araç çalıştı")

    def kapat(self):
        print("Kontak kapandı.")

    def sigorta(self):
        if self.kasko == True:
            print("Araç kaskolu")
        else:
            print("Araç kaskosuz.")

class Otomobil(Arac):
    def __init__(self,marka,model,var):
        Arac.__init__(self,marka,model,var)
        self.kapasite = "4"

arac_1 = Arac("Mercedes",2009,True)
arac_2 = Otomobil("Audi",2020,False)



class Otobüs(Arac):
    def __init__(self,marka,model,var,kapasite):
        super().__init__(marka,model,var)
        self.kapasite = kapasite
    def calistir(self):
        print("Otobüs çalıştı")
        
    


arac_3 = Otobüs("BMW",2021,True,50)

arac_1.calistir() #Araç parent classına ait bir nesne
arac_3.calistir() #Otobüs child classına ait bir nesne
print(arac_3.kapasite)
# print(arac_1.kapasite)
print(arac_2.kapasite)

# print(arac_3)
# arac_3.calistir()
# arac_3.kapat()
# Otobüs.arac_sayisi_arttir()
# print(Otobüs.arac_sayisi)


# print(arac_2)
# arac_2.calistir()
# arac_2.kapat()
# print(Otomobil.tur)
# arac_2.arac_sayisi_arttir()
# print(Otomobil.arac_sayisi)
# print(arac_1)
# arac_1.calistir()
# print(arac_1.model)

class Kisi():
    def __init__(self,ad,soyad,id):
        self.kisi_adi = ad 
        self.kisi_soyadi = soyad 
        self.__kisi_id = id
    def get_id_show(self):
        return self.__kisi_id
    def set_id(self,new_id):
        self.__kisi_id = new_id
    
    @property
    def id_gor(self):
        return self.__kisi_id

    @id_gor.setter
    def id_gor(self,yeni_id):
        self.__kisi_id = yeni_id

    @id_gor.deleter
    def id_gor(self):
        del self.__kisi_id
    
        
        
kisi_1 = Kisi("Ömer","Kars",12345)

print(kisi_1.set_id(54321))
print(kisi_1.get_id_show())

kisi_1.id_gor = 345
kisi_1.id_gor()