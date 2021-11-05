# -*- coding: utf-8 -*-
x = int(input("Lütfen bir sayi giriniz: "))
odd=0
even=0
for i in range (1,x+1):
    if i%2==0:
        even+=i
    else:
        odd+=i
print("Tek sayilar toplami = " + str(odd))
print("Cift sayilarin ortalamasi = " + str(even/x))
    