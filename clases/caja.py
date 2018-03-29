#!/usr/bin/python
# -*- coding: utf-8 -*-




import pygame
class Caja(pygame.sprite.Sprite):

    def __init__(self,ruta, posX, posY):

        pygame.sprite.Sprite.__init__(self)


        self.posX = posX
        self.posY = posY
        self.ruta = ruta


        self.imagen = pygame.image.load(ruta)

        self.rect = self.imagen.get_rect()
        self.rect.left = posX
        self.rect.top = posY

        self.alzada = False



    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)



