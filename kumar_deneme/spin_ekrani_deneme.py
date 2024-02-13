import random
import numpy as np

def spin():
    spin_simgeleri={3:"B",4:"C",5:"D",6:"E",7:"F",8:"G"}
    spin_kendisi=np.random.randint(3,9,(3,3))
    harf_matris=np.vectorize(spin_simgeleri.get)(spin_kendisi)
    return harf_matris

def spin_islem():
    ayni_satir=0
    ayni_sutun=0

    for satir in ggwp:
        if all(satir[0]==eleman for eleman in satir):
            ayni_satir += 1
    return ayni_satir,ayni_sutun

ggwp=spin()
print(ggwp)
ggwp1,ggwp2=spin_islem()
print(ggwp1)
print(ggwp2)

