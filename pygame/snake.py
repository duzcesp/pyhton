import pygame
import random

pygame.init()

genislik,yukseklik=600,600


pencere=pygame.display.set_mode((genislik,yukseklik))

hiz=10
saat=pygame.time.Clock()
fps=30

yilan=pygame.image.load("halloween.png")
yilan_kordinant=yilan.get_rect()
yilan_kordinant.topleft=(100/2,100/2)



durum=True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum=False
        elif etkinlik.type==pygame.K_DOWN:
            print(etkinlik)
            yilan_kordinant.move_ip(20,20)
    pencere.blit(yilan,yilan_kordinant)
    
    pygame.display.update()
