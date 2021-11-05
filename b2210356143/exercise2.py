sonuc = False
while sonuc == False:
    mail = input("Lütfen mail adresinizi giriniz: ")
    if "." in mail:
        if "@" in mail:
            print("Gecerli mail adresi!")
            sonuc = True
        else:
            print("Lütfen gecerli bir mail adresi giriniz!")
    else:
        print("Lütfen gecerli bir mail adresi giriniz!")
    