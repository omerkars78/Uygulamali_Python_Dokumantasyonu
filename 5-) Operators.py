#**************************** OPERATÖRLER ****************************
# 1-) Artimetik Operatörler 
# (+),(-),(*),(/),(%),(**)

# 2-) Atama Operatörleri
# - Eşittir Operatörü(=)
# a = 5
# print(a)
# - Artı Eşittir Operatörü(+=)
x = 10
x += 5
print(x)
# - Eksi Eşittir Operatörü(-=)
# x -= 3
# print(x)
# - Çarpı Eşittir Operatörü(*=)
# x *= 6
# print(x)
# - Bölü Eşittir Operatörü(/=)
# x /= 9
# print(int(x))
# - Mod Eşittir Operatörü(%=)
# x %= 5
# print(str(x))
# 3-) Karşılaştırma Operatörleri(Sonucun True veya False değerlerini Aldığımız Operatörler)
# - Eşittir Operatörü(==)
# print("Ömer"=="Ömer")# Ömer, Ömerdir
# print(5==6)
# - Eşit Değildir Operatörü(!=)
# print("Ömer"!="Can") #Ömer Can Değildir
# print("Ömer"!="Ömer")
# - Büyüktür Operatörü(>)
# print(7>5) # 7, 5'ten büyüktür
# print(7>8)
# - Küçüktür Operatörü(<)
# print(5<8) #5 küçüktür 8 ' den
# print(5<4)
# - Büyük Eşittir Operatörü(>=)
# print(5>=5) # 5 5'e Eşittir veya 5 ten büyüktür
# print(5>=4)
# print(5>=6)
# - Küçük Eşittir Operatörü(<=)
# print(4<=4) # 4 4 ' e eşittir veya daha büyüktür
# print(4<=5)
# print(4<=3)

# 4-) Mantıksal Operatörler(Sonucunda True veya False Değer Aldığımız Operatörlerdir)
# - And Operatörü
print(1<2 and 10>9)
print(1>3 and 10==11)
print(2>1 and 0!=0)
# And operatöründe True bir sonuç almak için her iki ifadeninde doğru olması gerekir.
# - Or Operatörü
print(1>0 or 10==10)
print(1<0 or 10==10)
print(1<0 or 10==11)
# Or operatöründe True bir sonuç almak için her iki ifadenin veya yanlızca birinin doğru olması yeterlidir.