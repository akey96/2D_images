#!/usr/bin/python
# -*- coding: utf-8 -*-


import pygame
class Caja(pygame.sprite.Sprite):

    def __init__(self,ruta, posX, posY):

        # Super Clase que nos da pygame para las imagenes
        pygame.sprite.Sprite.__init__(self)


        self.posX = posX
        self.posY = posY
        # ruta del directorio de las imagenes
        self.ruta = ruta

        # cargamos la imagen de la caja
        self.imagen = pygame.image.load(ruta)

        # atributp de tipo Rect  que nos indica la posicion del la imagen sobre la ventana
        self.rect = self.imagen.get_rect()

        self.rect.left = posX
        self.rect.top = posY

        # bool que nos indica si este objeto esta siendo alzado por el robot
        self.alzada = False


    # dibuja la caja sobre la ventana
    def dibujar(self, superficie):
        superficie.blit(self.imagen, self.rect)



