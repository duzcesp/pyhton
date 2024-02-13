import pygame
import random

pygame.init() #paketlerimizi başlattık
genislik,yukseklik=600,600


#penceremizi oluşturduk 
pencere=pygame.display.set_mode((genislik,yukseklik))

#fps ayarlama

HIZ=10 
saat=pygame.time.Clock()
FPS=30

#karakter ve yem tanımlama
canavar=pygame.image.load("halloween.png")
canavar_kordinant=canavar.get_rect()
canavar_kordinant.topleft=(600/2,600/2)

yem=pygame.image.load("eye.png")
yem_kordinant=yem.get_rect()
yem_kordinant.topleft=(600/3,600/3)


#Font ayarı

font=pygame.font.SysFont("consolas",40)

#skor
skor=0

#oyun döngüsü
durum=True

while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum=False
    pencere.blit(canavar,canavar_kordinant)
    pencere.blit(yem,yem_kordinant)
    yazi=font.render("Score:"+str(skor),True,(255,0,0),(0,255,0))
    yazi_kordinant=yazi.get_rect()
    yazi_kordinant.topleft=(20,20)
    pygame.draw.line(pencere,(255,0,255),(0,90),(600,90),3)
    

    pygame.display.update()