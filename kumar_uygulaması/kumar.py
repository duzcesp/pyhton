import random
import numpy as np

MAX_GİRİLCEK_PARA=1000
MİN_GİRİLCEK_PARA=100
MİN_BET=10
MAX_BET=MAX_GİRİLCEK_PARA

def depozito():
    while True:
        oynancak_para=input(f"Oynicağiniz Para Miktarini Girin= {MİN_GİRİLCEK_PARA}-{MAX_GİRİLCEK_PARA} Arasi $")
        if oynancak_para.isdigit():
            oynancak_para=int(oynancak_para)
            if oynancak_para >=100 and oynancak_para<=1000:
                break
            else:
                print("Lütfen Para Yatirin...")
        else:
            print("Lütfen Yükleciğiniz Para Miktarini Giriniz")
    return oynancak_para
def oynancak_miktar():
    while True:
        oynancak_miktar_bet=input("1. Spin İçin Bahis Miktarinizi Giriniz: $")
        if oynancak_miktar_bet.isdigit():
            oynancak_miktar_bet=int(oynancak_miktar_bet)
            if oynancak_miktar_bet>0:
                break
            else:
                print("Lütfen Belirtilen değer araliklarinda para yatiriniz...")
        else:
            print("Sayi girmeye çalişiniz...")
    return oynancak_miktar_bet

def spin_oyunu():
    spin_simgeleri={2:"A",3:"B",4:"C",5:"D"}
    spin_kendisi=np.random.randint(2,5,(4,4))
    harf_matris=np.vectorize(spin_simgeleri.get)(spin_kendisi)
    spin_kolu_çekme=input("-Spini Başlatmak İçin '+' tuşuna basiniz.-")
    if spin_kolu_çekme=="+":
        spin_simgeleri={2:"A",3:"B",4:"C",5:"D"}
        spin_kendisi=np.random.randint(2,5,(4,4))
        harf_matris=np.vectorize(spin_simgeleri.get)(spin_kendisi)
        print(harf_matris)
    ayni_satir_sayisi=0
    ayni_sütün_sayisi=0
    for satir in harf_matris:
        if all(satir[0]==eleman for eleman in satir):
            ayni_satir_sayisi +=1
        
    for satir1 in harf_matris:
        if all(satir1[0]==eleman1 for eleman1 in satir1):
            ayni_sütün_sayisi +=1
            
    return ayni_sütün_sayisi,ayni_satir_sayisi
            
def main():
        balance=depozito() #balance=oynancak_miktar eşit
        miktar=oynancak_miktar() #miktar=oynancak_miktar_bet eşit
        ayni_sütün_sayisi,ayni_satir_sayisi=spin_oyunu()
        if miktar>balance:
            miktar=False
            print("Lütfen Paraniz Kadar Bahis Oynayin...")
        while True:
            spin_oyunu()
            balance = balance -miktar
            print("depozito",balance)
            if balance<=0:
                break
            else:
                if ayni_sütün_sayisi==1:
                    balance = miktar*ayni_sütün_sayisi*2
                elif ayni_sütün_sayisi==2:
                    balance = miktar*ayni_sütün_sayisi*3
                elif ayni_sütün_sayisi==3:
                    balance = miktar*ayni_sütün_sayisi*4
                elif ayni_sütün_sayisi==4:
                    balance = miktar*ayni_sütün_sayisi*10
                elif ayni_satir_sayisi==1:
                    balance=miktar*ayni_satir_sayisi*2
                elif ayni_satir_sayisi==2:
                    balance=miktar*ayni_satir_sayisi*3
                elif ayni_satir_sayisi==3:
                    balance=miktar*ayni_satir_sayisi*4

            



                

                
                    
                    
            
main()


    
    







        
        