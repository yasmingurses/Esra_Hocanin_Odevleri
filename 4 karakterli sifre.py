#Guncelleme
#Rakamlardan olusup olusmadıgını da kontrol ediyor

#4 karakterli sifre olusup olusmadıgını kontrol etme

x = str(input("Dört karakterli bir şifre giriniz: "))
while len(x) != 4 or x.isdigit() == False :
    print("4 karakterli ve rakamlardan oluşan bir şifre olmalı")
    x = str(input("Dört karakterli bir şifre giriniz: "))

else:
    print("Girilen şifre: " , x)
    
    
