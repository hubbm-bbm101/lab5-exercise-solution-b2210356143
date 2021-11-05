import random
sayi = random.randint(0,999)
sonuc = False
while sonuc == False:
    tahmin = int(input("Lütfen tahmininizi giriniz: "))
    if tahmin > sayi:
        print("Lütfen sayinizi kücültün!")
    elif tahmin < sayi:
        print("Lütfen sayinizi büyültün!")
    else:
        print("Dogru tahmin!")
        sonuc = True