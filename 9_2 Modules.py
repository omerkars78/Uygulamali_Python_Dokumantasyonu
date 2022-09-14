bilgi = "Bu dosya bir modül dosyasıdır."

def bilgileri_goster(ad,soyad,yas):
    print(f"""
        Ad: {ad}
        Soyad: {soyad}
        Yaş: {yas}
    """)

class Kisi():
    def __init__(self,ad,soyad,yas):
        self.ad = ad 
        self.soyad = soyad 
        self.yas = yas 

# bilgileri_goster("Ömer","Kars",21) 

kisi_1 = Kisi("Ahmet","Yılmaz",50)  

# print(kisi_1.ad)
# print(kisi_1.soyad)
# print(kisi_1.yas)
# print(bilgi)
