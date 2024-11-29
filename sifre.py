import random

karakterler = "+-/*!&$#?=@abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
kullanici = int(input("Parolanin uzunluğunu giriniz: "))

sifre = ""

for i in range(kullanici):
    sifre += random.choice(karakterler)
    
print("Oluşturulan şifre: ",sifre)

