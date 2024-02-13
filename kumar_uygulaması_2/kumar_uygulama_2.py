import random
import typing
from PyQt5.QtWidgets import QWidget
import numpy as np
from PyQt5 import QtCore, QtWidgets
import sys

class kumar(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()

    def init_ui(self):
        self.spin=QtWidgets.QPushButton("Spin") #spin butonu
        self.oynancak_para_miktari=QtWidgets.QLineEdit() #oynancak_para_miktari
        self.kullanici_bet=QtWidgets.QLineEdit() # kullanici_bet
        self.spin_ekrani=QtWidgets.QTableWidget() #spin_ekrani
        self.spin_ekrani.setRowCount(4)
        self.spin_ekrani.setColumnCount(4)
        self.yatir=QtWidgets.QPushButton("Yatir") #yatir butonu
        self.kullanici_para_sorgu=QtWidgets.QLabel("") #kullanici_para_sorgu ekrani
        self.oynancak_para_miktari_1=QtWidgets.QLabel("Yatircağiniz Para...") 
        self.oynancak_bet=QtWidgets.QLabel("Oynicağiniz Bet... ")
        
        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.oynancak_para_miktari_1)
        v_box.addWidget(self.oynancak_para_miktari)
        v_box.addStretch()
        v_box.addWidget(self.yatir)
        v_box.addStretch()
        v_box.addStretch()
        v_box.addWidget(self.oynancak_bet)
        v_box.addWidget(self.kullanici_bet)
        v_box.addStretch()
        v_box.addWidget(self.spin_ekrani)
        v_box.addStretch()
        v_box.addWidget(self.spin)
        v_box.addStretch()
        v_box.addWidget(self.kullanici_para_sorgu)
        v_box.addStretch()


        self.setLayout(v_box)
        self.setWindowTitle("Spin Makinesi")
        self.spin.clicked.connect(self.spin_basildi)
        self.spin.clicked.connect(self.hit_hesaplama)
        self.yatir.clicked.connect(self.yatirma_islemi)
        self.yatir.clicked.connect(self.kullanici_bet_kontrol)
        self.show()

    def spin_basildi(self):
        matris=np.empty((4,4),dtype=str)
        harf_seçenekleri=["A","B","C","D"]
        for i in range(4):
            for j in range(4):
                harf=random.choice(harf_seçenekleri)
                matris[i][j]=harf
        for row in range(4):
            for col in range(4):
                item =QtWidgets.QTableWidgetItem(str(matris[row][col]))
                self.spin_ekrani.setItem(row,col,item)
        
        
    def yatirma_islemi(self):
        kullanicinin_parasi=self.oynancak_para_miktari.text()
        if kullanicinin_parasi.isdigit():
            self.kullanici_para_sorgu.setText(f"Oynamak İçin Kalan Paraniz: {kullanicinin_parasi} $")
            kullanicinin_parasi=int(kullanicinin_parasi)
        else:
            self.kullanici_para_sorgu.setText("Lütfen Paranizi Doğru Girin...")
    
    def kullanici_bet_kontrol(self):
        kullanici_bet_parasi=self.kullanici_bet.text()
        if kullanici_bet_parasi.isdigit():
            kullanici_bet_parasi=int(kullanici_bet_parasi)
        elif kullanici_bet_parasi>self.oynancak_para_miktari and kullanici_bet_parasi<10:
            self.kullanici_para_sorgu.setText("Düzgün Para Miktari Girin...")
        else:
            self.kullanici_para_sorgu.setText("düzgün gir ibne...")
            


    def hit_hesaplama(self):

        ilk_satir_elemanlari=[]
        for sutun in range(4):
            item=self.spin_ekrani.item(0,sutun)
            if item is not None:
                ilk_satir_elemanlari.append(item.text())


        ikinci_satir_elemanlari=[]
        for sutun1 in range(4):
            item1=self.spin_ekrani.item(1,sutun1)
            if item1 is not None:
                ikinci_satir_elemanlari.append(item1.text())
        

        ucuncu_satir_elemanlari=[]
        for sutun2 in range(4):
            item2=self.spin_ekrani.item(2,sutun2)
            if item2 is not None:
                ucuncu_satir_elemanlari.append(item2.text())
        

        dorduncu_satir_elemanlari=[]
        for sutun3 in range(4):
            item3=self.spin_ekrani.item(3,sutun3)
            if item3 is not None:
                dorduncu_satir_elemanlari.append(item3.text())
        ayni_mi=all(eleman==ilk_satir_elemanlari[0] for eleman in ilk_satir_elemanlari)
        if ayni_mi == True:
            self.oynancak_para_miktari = self.oynancak_para_miktari+(self.kullanici_bet*5)
            self.kullanici_para_sorgu.setText(self.oynancak_para_miktari)
        ayni_mi1=all(eleman==ikinci_satir_elemanlari[0] for eleman in ikinci_satir_elemanlari)
        if ayni_mi1 == True:
            self.oynancak_para_miktari = self.oynancak_para_miktari+(self.kullanici_bet*5)
            self.kullanici_para_sorgu.setText(self.oynancak_para_miktari)
        

     
    #en son terminal ekranina pencere arayüzünde yaptığın 4x4 lük matris elemanlarını eklemeyi başardın fakat oyuncunun girdiği para miktarini kullanicinin_bet yaptığı para miktari kadar arttıramiyorsun 
    #yani kullanici 10 tl bet oynuyor kazanıyor ama ana parasına eklenmiyor



        print(ilk_satir_elemanlari)
        print(ikinci_satir_elemanlari)
        print(ucuncu_satir_elemanlari)
        print(dorduncu_satir_elemanlari)
        

                


app=QtWidgets.QApplication(sys.argv)
oyun=kumar()
sys.exit(app.exec_())
        
