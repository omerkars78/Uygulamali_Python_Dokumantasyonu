class Turler():
    hayatta_olmak = True
    solunum_yapmak = True
    bosaltim_yapmak = True
    uremek = True

class Kopek(Turler):
   
    havlamak = True
    kosmak = True
    koklamak = True
    
    def __init__(self,isim,irk): 
        self.isim = isim
        self.irk = irk
    def iz_sur(self):    
        self.iz_surmek = True
    def av_cikar(self):    
        self.av_cikarmak = True  

max = Kopek("Max","Av Köpeği")   
print(max.isim) 
print(max.irk) 
max.iz_sur()
max.av_cikar()
print(max.iz_surmek)
print(max.av_cikarmak)
