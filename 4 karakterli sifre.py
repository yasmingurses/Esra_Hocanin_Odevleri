#4 karakterli sifre olusup olusmadıgını kontrol etme

x = str(input("Dört karakterli bir şifre giriniz: "))
while len(x) != 4 :
    print("4 karakterli bir şifre olmalı")
    x = str(input("Dört karakterli bir şifre giriniz: "))


print("Girilen şifre: " , x)
    
    
