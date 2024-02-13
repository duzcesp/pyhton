from PyQt5 import QtWidgets
import sys


class Hesap_Makinesi(QtWidgets.QWidget):
    def __init__(self):
        super().__init__()
        self.init_ui()
    def init_ui(self):
        self.toplama_tuşu=QtWidgets.QPushButton("toplama")
        self.çikarma_tuşu=QtWidgets.QPushButton("çikarma")
        self.çarpma_tuşu=QtWidgets.QPushButton("çarpma")
        self.bölme_tuşu=QtWidgets.QPushButton("bölme")
        self.girdi=QtWidgets.QLineEdit(self)
        self.girdi1=QtWidgets.QLineEdit(self)
        self.çikti=QtWidgets.QLabel(self)

        v_box=QtWidgets.QVBoxLayout()
        v_box.addWidget(self.çikti)
        v_box.addStretch()
        v_box.addWidget(self.girdi)
        v_box.addWidget(self.girdi1)
        v_box.addStretch()
        v_box.addWidget(self.toplama_tuşu)
        v_box.addWidget(self.çikarma_tuşu)
        v_box.addWidget(self.bölme_tuşu)
        v_box.addWidget(self.çarpma_tuşu)
        
        self.toplama_tuşu.clicked.connect(self.clicked)
        self.çikarma_tuşu.clicked.connect(self.clicked)
        self.çarpma_tuşu.clicked.connect(self.clicked)
        self.bölme_tuşu.clicked.connect(self.clicked)

        

        self.setLayout(v_box)
        self.setWindowTitle("HESAP MAKİNESİ")
        self.show()
    def clicked(self):
        sender=self.sender()
        if sender.text() =="toplama":
            try:
                num1=float(self.girdi.text())
                num2=float(self.girdi1.text())
                çikti = num1 + num2
                self.çikti.setText("sonuş:{}".format(çikti))
            except ValueError:
                self.çikti.setText("geçerli sayi girin")
        elif sender.text()=="çikarma":
            try:
                num1=float(self.girdi.text())
                num2=float(self.girdi1.text())
                çikti=num1-num2
                self.çikti.setText("sonuş:{}".format(çikti))
            except ValueError:
                self.çikti.setText("geçerli sayi girin")
        elif sender.text()=="çarpma":
            try:
                num1=float(self.girdi.text())
                num2=float(self.girdi1.text())
                çikti=num1*num2
                self.çikti.setText("sonuş:{}".format(çikti))
            except ValueError:
                self.çikti.setText("geçerli sayi girin")
        elif sender.text()=="bölme":
            try:
                num1=float(self.girdi.text())
                num2=float(self.girdi1.text())
                çikti=num1/num2
                self.çikti.setText("sonuş:{}".format(çikti))
            except ValueError:
                self.çikti.setText("geçerli sayi girin")


    



app=QtWidgets.QApplication(sys.argv)
hesap_makinesi=Hesap_Makinesi()
hesap_makinesi.show()
sys.exit(app.exec_())
    