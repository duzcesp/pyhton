import random
import numpy as np

MİN_GİRİLCEK_PARA=100
MAX_GİRİLCEK_PARA=1000
MİN_BET=10
MAX_BET=MAX_GİRİLCEK_PARA 

def Depozito():   #kullanicinin para miktarini girdiği fonksiyon ve return değeri kullanicinin girdiği para miktari
    while True:
        oynancak_para=input(f"Oynicağiniz Para Miktarini Girin= {MİN_GİRİLCEK_PARA}-{MAX_GİRİLCEK_PARA} Arasi $")
        if oynancak_para.isdigit():
            oynancak_para=int(oynancak_para)
            if oynancak_para>=100 and oynancak_para<=1000:
                break
            else:
                print("100$-1000$ arasinda yatirabilirsiniz...")
        else:
            print("Lütfen Para Miktarini Sayilarla Giriş Yapiniz...")
    return oynancak_para 

def Kullanici_Bet():
    while True:
        oynancak_bet=input("Spin İçin Bahis Miktarinizi Girin. - $")
        if oynancak_bet.isdigit():
            oynancak_bet=int(oynancak_bet)
            if oynancak_bet>=10 and oynancak_bet<=MAX_BET:
                break
            else:
                print("Lütfen Doğru Bet Yatirin...")
        else:
            print("Betinizi Sayi Şeklinde Girin...")
    return oynancak_bet

def Spin_Ekrani():
    while True:
        spin_kolu_çekme=input("-Spini Başlatmak İçin '+' tuşuna basiniz.-")
        if spin_kolu_çekme=="q":
            break
        if spin_kolu_çekme=="+":
            matris=np.empty((4,4),dtype=str)
            harf_seçenekleri=["A","B","C","D"]
            for i in range(4):
                for j in range(4):
                    harf=random.choice(harf_seçenekleri)
                    matris[i][j]=harf
            print(matris)
            satir_sayisi=0
            sütun_sayisi=0
            for i in range(4):
                satir=''.join(matris[i,:])
                sütun=''.join(matris[:,i])
                if "AAAA" in satir or "BBBB" in satir or "CCCC" in satir or "DDDD" in satir:
                    satir_sayisi +=1
                if "AAAA" in sütun or "BBBB" in sütun or "CCCC" in sütun or "DDDD" in sütun:
                    sütun_sayisi +=1
                continue
            print(satir_sayisi)
            print(sütun_sayisi)
    return satir_sayisi,sütun_sayisi

depozito=Depozito() #oynancak_para döndürüyo
kullanici_bet=Kullanici_Bet() #oynancak_bet döndürüyo
satir_sayisi,sütun_sayisi=Spin_Ekrani()
while depozito>0:
    print(satir_sayisi)
    print(sütun_sayisi)
    print("depozito",depozito)
    depozito = depozito-kullanici_bet
    if satir_sayisi>0:
        depozito=kullanici_bet*satir_sayisi*3
    elif sütun_sayisi>0:
        depozito=kullanici_bet*sütun_sayisi*3
    elif satir_sayisi>0 and sütun_sayisi>0:
        depozito=kullanici_bet*satir_sayisi*sütun_sayisi*3



        
    