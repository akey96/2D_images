#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame, time


class Robot(pygame.sprite.Sprite):

    def __init__(self,ruta, posX, posY, velocidad, ancho, largo):

        pygame.sprite.Sprite.__init__(self)

        self.posX = posX
        self.posY = posY
        self.ruta = ruta

        self.reloj = pygame.time.Clock()
        self.listaRobot = [ pygame.image.load("{}/{}.png".format(self.ruta,i)) for i in range(1,9)]
        #self.listaRobotCajas = [ pygame.image.load("{}/{}C.png".format(self.ruta,i)) for i in range(1,9)]
        self.tieneCaja = False

        self.velociadad = velocidad
        self.orientacion = "sur"
        self.ancho = ancho
        self.largo = largo

        self.imagen = pygame.image.load("{}/1.png".format(self.ruta))
        self.rect = self.imagen.get_rect()
        self.rect.left = posX
        self.rect.top = posY
        self.l = False
        self.r = False
        self.t = False
        self.d = False



    def dibuja(self, superficie):
        superficie.blit(self.imagen, self.rect)


    def mvLeff(self):
        #self.monitor()


        self.imagen = self.listaRobot[2]
        if self.rect.left < 10:
            self.rect.left = 0
        else:
            #self.rect.left-=self.velociadad
            self.rect.move_ip( -self.velociadad, 0)


    def mvRight(self):
        #self.monitor()

        self.imagen = self.listaRobot[6]
        if self.rect.left > self.ancho-130:
            self.rect.left = self.ancho-120

        else:
            #self.rect.left += self.velociadad
            self.rect.move_ip(self.velociadad, 0)

    def mvtop(self):

        #self.monitor()

        self.imagen = self.listaRobot[4]
        if self.rect.top < 20:
            self.rect.top = 10
        else:
            #self.rect.top-=self.velociadad
            self.rect.move_ip(0,- self.velociadad)

    def mvdown(self):
        #self.monitor()

        # cambiamos de imagenes
        self.imagen = self.listaRobot[0]



        # controlamos para que no se salga del cuadro
        if self.rect.top > self.largo - 120:
            self.rect.top = self.largo - 110
        else:
            #self.rect.top += self.velociadad
            self.rect.move_ip(0,  self.velociadad)

    def monitor(self):

        print "izq : ",self.l
        print "der : ",self.r
        print "top : ",self.t
        print "dow : ",self.d




    def girar0_90(self):
        for i in range(6,3,-1):
            time.sleep(0.005)
            self.imagen = self.listaRobot[i]


    def alzarCaja(self):
        pass
    def soltarCaja(self):
        pass

    def girar360(self,superficie, timer):
        pass
        # hacer con hilos , para que en otro proceso solo se cambie la imagen, ojo, solo la imagen, ya que tiene
        # que rotar sobre su propio eje


