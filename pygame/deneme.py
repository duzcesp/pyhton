import pygame
import random

pygame.init()

genislik,yukseklik=600,600


pencere=pygame.display.set_mode((genislik,yukseklik))

hiz=10
saat=pygame.time.Clock()
fps=60

yilan=pygame.draw.line(pencere,(255,0,0),5)
yilan_kordinant=yilan.get_rect()
yilan_kordinant.topleft(200,200)
yem=pygame.draw.circle(pencere,(255,255,0),(200,200),(5),(8))







durum=True
while durum:
    for etkinlik in pygame.event.get():
        if etkinlik.type==pygame.QUIT:
            durum=False
    yilan.move(105,150)
    if etkinlik.type==pygame.K_LEFT:
        pass

    pygame.display.update()
