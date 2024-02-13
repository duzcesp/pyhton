import sys
from PyQt5 import QtWidgets
import sqlite3

import sys
from PyQt5 import QtWidgets
class Pencere(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.baglanti_olustur()
    def baglanti_olustur(self):
        baglanti=sqlite3.connect("database.db")
        self.cursor=baglanti.cursor()
        self.cursor.execute("Create Table If not exists üyeler (kullanici_adi TEXT,parola TEXT)")
        baglanti.commit()
    def init_ui(self):
        self.kullanici_adi=QtWidgets.QLineEdit()
        self.parola=QtWidgets.QLineEdit()
        self.parola.setEchoMode(QtWidgets.QLineEdit.Password) #girdiğimiz karakteler gizli kalır şifre misali
        self.giris=QtWidgets.QPushButton("Giriş Yap")
        self.yazi_alani=QtWidgets.QLabel("")

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.kullanici_adi)
        v_box.addWidget(self.parola)
        v_box.addWidget(self.yazi_alani)
        v_box.addStretch()
        v_box.addWidget(self.giris)

        self.setLayout(v_box)
        self.setWindowTitle("KULLANICI GİRİŞİ")
        self.giris.clicked.connect(self.login)
        self.show()
    def login(self):
        adi=self.kullanici_adi.text()
        par=self.parola.text()
        self.cursor.execute("Select *From üyeler where kullanici_adi=? and parola=?",(adi,par))
        data = self.cursor.fetchall()
        if len(data)==0:
            self.yazi_alani.setText("hg bro" +adi)
        else:
            self.yazi_alani.setText("sq")

app=QtWidgets.QApplication(sys.argv)
pencere=Pencere()
sys.exit(app.exec_())
