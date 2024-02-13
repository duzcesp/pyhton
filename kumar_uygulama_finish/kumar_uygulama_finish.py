import random
import numpy as np
import sys

max_para_yatirma=1000
min_para_yatirma=100
min_bet=10



def spin_ekrani():
    spin_simgeleri={3:"B",4:"C",5:"D",6:"E",7:"F",8:"G",9:"H",10:"K",11:"L"}
    spin_kendisi=np.random.randint(3,12,(3,3))
    harf_matris=np.vectorize(spin_simgeleri.get)(spin_kendisi)
    return harf_matris


def kullanici_para_miktari():
    while True:
        kullanici_para_miktari_1=input(f"Kaç Para Yatirmak İstiyorsunuz ? {min_para_yatirma}-{max_para_yatirma}$    $ ")
        if kullanici_para_miktari_1.isdigit():
            kullanici_para_miktari_1 = int(kullanici_para_miktari_1)
            if min_para_yatirma<=kullanici_para_miktari_1<=max_para_yatirma:
               print(f"{kullanici_para_miktari_1}$ Paraniz Yatirilmiştir...")
               break
            elif kullanici_para_miktari_1==0:
                print("Çikiş Yapiliyor...")
                break
            else:
                print("Doğru Değerlerde Bir Miktar Yatiriniz...")
                continue
        else:
            print("Lütfen Rakamlarla Bir Para Değeri Girmeyi Deneyiniz")
            continue
    return kullanici_para_miktari_1

def spin_işlemi():
    ayni_satir_sutun=0
    for satir in ggwp:
        if all(satir[0]==eleman for eleman in satir):
            ayni_satir_sutun += 1
    return ayni_satir_sutun



def kullanici_bet():
    while True:
        kullanici_bet_1=input(f"1 Döndürme İçin Oynicağiniz Bet {min_bet}-{kullanici_money}$     $ ")
        if kullanici_bet_1.isdigit():
            kullanici_bet_1 = int(kullanici_bet_1)
            if min_bet<=kullanici_bet_1<=kullanici_money:
                print(f"Betiniz {kullanici_bet_1}$")
                break
            elif kullanici_bet_1==0:
                print("Bet Yapmadiniz Oynamak İçin Bi Daha Kayit Olun...")
                break
            else:
                print("Doğru Araliklarda Bir Bet Giriniz...")
                continue
        else:
            print("Sayi Girmeyi Deneyiniz...")
            continue
    return kullanici_bet_1


ggwp=spin_ekrani()
ggwp_kazandin=spin_işlemi()
kullanici_money=kullanici_para_miktari()
if kullanici_money==0:
    exit()   
kullanici_bet_xd=kullanici_bet()
if kullanici_bet_xd==0:
    exit()

while True:
    ggwp=spin_ekrani()
    ggwp_kazandin=spin_işlemi()
    spin_başlatma_butonu=input("Spin İçin Enter Tuşuna Basiniz...")
    if spin_başlatma_butonu=="":
        kullanici_money=kullanici_money-kullanici_bet_xd
        print(ggwp)
        print(ggwp_kazandin)
        if ggwp_kazandin==1:
            kullanici_money += kullanici_bet_xd*ggwp_kazandin*5
        elif ggwp_kazandin==2:
            kullanici_money += kullanici_bet_xd*ggwp_kazandin*10
        elif ggwp_kazandin==3:
            kullanici_money += kullanici_bet_xd*ggwp_kazandin*15
        print(f"Kalan Para = ${kullanici_money}")
    if kullanici_money==0 or kullanici_money<kullanici_bet_xd:
        print("Bet İçin Paraniz Yetersiz...")
        break
    elif spin_başlatma_butonu=="q":
        exit()
    


    