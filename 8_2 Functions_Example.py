#Vücut kitle indeksinin hesaplandığı bir program yazınız
# Kullanıcıdan kilo ve boy değerleri alınız
#Vücut kitle indeksi hesaplama formlü kg/m2
#vki değeri 18.5 tan altı zayıf 30 a kadar normal 30-40 arası obez 40-50 arası morid obez 
# 50 ve üzeri süper obezdir
def vki():
    while True:
        boy = float(input("Lütfen metre cinsinden boyunuzu giriniz: "))
        kilo = int(input("Lütfen kilogram cinsinden kilonuzu giriniz: "))
        sonuc = (kilo)/(boy**2)
        if (sonuc < 18.5):
            print(f"Vücut kitle endeksiniz {sonuc}. Zayıf kategorisindesiniz.")
        elif(sonuc < 30):
            print(f"Vücut kitle endeksiniz {sonuc}. Normal kategorisindesiniz.") 
        elif(sonuc < 40):
            print(f"Vücut kitle endeksiniz {sonuc}. Obez kategorisindesiniz.")       
        elif(sonuc < 50 ):
             print(f"Vücut kitle endeksiniz {sonuc}. Morid Obez kategorisindesiniz.") 
        elif(sonuc > 50 ):
             print(f"Vücut kitle endeksiniz {sonuc}. Süper Obez kategorisindesiniz.")      
vki()             