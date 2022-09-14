#**************************** KOŞUL İFADELERİ (if,else,elif) ************************************
a,b,c = 1,2,1
# print(a==c)
# print(a<b)
# print(a>b)
# if(a==c):
#     print("işlem doğru")
# if(a<b):
#     print("işlem doğru")
# if(a>b):
#     print("işlem doğru")
# else:
#     print("işlem yanlış") # Eğer a, b'den büyükse işlem doğru yazdır. Eğer a, b'den büyük değilse işlem yanlış yazdır. 
# Eğer doğru bir önerme varsa if bloğu çalışır. Eğer önerme yanlışsa çalışmaz.
# kullanci_adi = input("Lütfen Kullanıcı Adı Giriniz:")
# parola = input("Lütfen Parolanızı Giriniz:")
# if (kullanci_adi == "Ömer"):
#     print("Tebrikler Kullanıcı Adı Doğru")
# else:
#     print("Kullanıcı Adı Yanlış")
# if (parola == "omer123"):
#     print("Tebrikler parola doğru") 
# else:
#     print("Maalesef parola yanlış")
# 2-) Elif Bloğu Nedir Hangi durumlarda Kullanılır

# animal = input("bir hayvan ismi giriniz: ")
# if(animal == "Kuş"):
#     print(f"evet {animal} gerçekten bir hayvandır.")
# elif(animal == "Köpek"):
#     print(f"evet {animal} gerçekten bir hayvandır.")    
# elif(animal == "Kedi"):
#     print(f"evet {animal} gerçekten bir hayvandır.")      
# else:
#     print(f"{animal} gerçekten bir hayvan mı?")     


# 3-) Uygulama 
# Bir üniversitede vize notunun %40 ı Final Notunun %60 ı alınarak geçme notu hesaplanmaktadır.
# Buna göre 85 ve üzeri için harf notu AA, 70 ve 85 arası için BA, 60 ve 70 arası için BB,
# Eğer 45 ve 60 arasındaysa CB , eğer 45 ten düşükse FF olacak şekildedir.
# Bu koşullara göre geçme notu hesaplayan ve harf notu olarak karşılık veren python kodunu yazınız.

vize_notu = int(input("Vize Notu Giriniz: ")) 
final_notu = int(input("Final Notu Giriniz: ")) 
gecme_notu = (vize_notu*0.4) + (final_notu*0.6) 

if (gecme_notu > 85 ):
    print(f"Geçme notunuz: {gecme_notu} Harf notunuz AA") 
elif (gecme_notu < 85 and gecme_notu >= 70 ):
    print(f"Geçme notunuz: {gecme_notu} Harf notunuz BA") 
elif (gecme_notu < 70 and gecme_notu >= 60 ):
    print(f"Geçme notunuz: {gecme_notu} Harf notunuz BB") 
elif (gecme_notu < 60 and gecme_notu >= 45 ):
    print(f"Geçme notunuz: {gecme_notu} Harf notunuz CB") 
elif (gecme_notu < 45):
    print(f"Geçme notunuz: {gecme_notu} Harf notunuz FF")



