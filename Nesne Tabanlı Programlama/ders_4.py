#****************************** PROPERTY **************************************
class Kisi():
    def __init__(self,ad,soyad,tc_no):
        self.ad = ad 
        self.soyad = soyad 
        self.__tc = tc_no 

    # def get_tc_gor(self):
    #     return self.__tc 

    # def set_tc(self,yeni_tc):
    #     if yeni_tc == 123:
    #         raise ValueError("Yeni tcnin numarası 123 olmaz")
    #     self.__tc = yeni_tc 

    @property 
    def tc(self):
        return self.__tc 

    @tc.setter 
    def tc(self,yeni_tc):
        if yeni_tc == 123:
            raise ValueError("Yeni tcnin numarası 123 olmaz")
        self.__tc = yeni_tc 

    @tc.deleter 
    def tc(self):
        del self.__tc
    

  

    


kisi_1 = Kisi("Ahmet","Yılmaz",12345) 
kisi_1.tc = 98765
del kisi_1.tc 
print(kisi_1.tc)