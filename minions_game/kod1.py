kullanici_skor=0
tanimli_ifadeler=set()
import pwinput
girdi = pwinput.pwinput(prompt='admin giriş: ')
while True:
    kullanici=input("kullanici tahmini:")
    #kullanicinin girdiği kelimeleri tanimli_ifadeler kümesine ekle
    uzunluk=len(kullanici)
    for i in range(0,1):
        if kullanici in girdi:
            kullanici_skor+=uzunluk
            print("kullanici skor:{}".format(kullanici_skor))
        elif kullanici not in girdi:
            print("girdiğiniz tahmin keliminin içinde yoktur")
            kullanici_skor+=0
    if kullanici in tanimli_ifadeler:
        print("bu tahmini kullandiniz başka tahmin kullanin")
        kullanici_skor -= uzunluk
        continue
    else:
        tanimli_ifadeler.add(kullanici)
    if kullanici==girdi:
        print("cevabiniz doğrudur ve skorunuz",kullanici_skor)
        break






