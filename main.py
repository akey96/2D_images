#!/usr/bin/python
# -*- coding: utf-8 -*-


import  pygame, sys, threading
from  random import randrange
from pygame.locals import  *
from clases.caja import Caja
from clases.robot import Robot

pygame.init()

# variables globales
ancho = 1000
largo = 700
ventana = pygame.display.set_mode((ancho, largo))
nroRobot = 0
velocidad = 10
reloj = pygame.time.Clock()
timer = 20
listRutas = ["imagenes3"]
listCajas = [Caja("{}/caja.png".format(listRutas[nroRobot]), randrange(100,900,1), randrange(100,600,1)) for i in range(2)]
robot = Robot("{}".format(listRutas[nroRobot]), ancho / 2, largo / 2, velocidad, ancho, largo)


fondo = pygame.image.load("imagenes/fondo.png")


def pintarVentana():
    ventana.blit(fondo,(0,0))
    #ventana.fill((0,0,0))




def moverRight():
    while True:

        reloj.tick(timer)
        if robot.r:
            # esto para las coliciones
            antesX, antesY = robot.rect.left, robot.rect.top
            #print antesX, antesY
            robot.mvRight()


def moverLeft():
    while True:



        reloj.tick(timer)
        if robot.l:
            # esto para las coliciones
            antesX, antesY = robot.rect.left, robot.rect.top
            #print antesX, antesY
            robot.mvLeff()



def moverTop():
    while True:



        reloj.tick(timer)
        if robot.t:
            # esto para las coliciones
            antesX, antesY = robot.rect.left, robot.rect.top
            #print antesX, antesY
            robot.mvtop()


def moverDown():
    while True:



        reloj.tick(timer)
        if robot.d:
            # esto para las coliciones
            antesX, antesY = robot.rect.left, robot.rect.top
            #print antesX, antesY

            robot.mvdown()





def SO():
    reloj.tick(timer-15)
    robot.imagen = robot.listaRobot[7]

def NE():
    reloj.tick(timer-15)
    robot.imagen = robot.listaRobot[3]

def NO():
    reloj.tick(timer-15)
    robot.imagen = robot.listaRobot[5]


def SE():
    reloj.tick(timer-15)
    robot.imagen = robot.listaRobot[1]

def existeColicion(rect1,rect2):

    pass

def principal():

    ultimaLetra = ""

    datosR = "{}:{}:{}:{}".format(robot.posX, robot.posY, robot.orientacion, nroRobot)
    listDatosR = ":".join(datosR)

    # declaracion de demonios(Threads)

    derecha = threading.Thread(target=moverRight)
    derecha.setDaemon(True)
    derecha.start()

    izquierda = threading.Thread(target=moverLeft)
    izquierda.setDaemon(True)
    izquierda.start()

    abajo = threading.Thread(target=moverDown)
    abajo.setDaemon(True)
    abajo.start()

    arriba = threading.Thread(target=moverTop)
    arriba.setDaemon(True)
    arriba.start()

    while True:
        reloj.tick(timer)

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    if ultimaLetra == "t" :
                        NE()
                    elif ultimaLetra == "d":
                        SE()
                    elif ultimaLetra == "r":
                        NO()
                        reloj.tick(12)
                        NE()


                    robot.l = True
                    robot.r = False
                    robot.d = False
                    robot.t = False

                elif event.key == pygame.K_RIGHT:
                    if ultimaLetra == "d":
                        SO()
                    elif ultimaLetra == "t":
                        NO()
                    elif ultimaLetra == "l":
                        NE()
                        reloj.tick(12)
                        NO()

                    robot.r = True
                    robot.l = False
                    robot.d = False
                    robot.t = False

                elif event.key == pygame.K_UP:
                    if ultimaLetra == "r":
                        NO()
                    elif ultimaLetra == "l":
                        NE()
                    elif ultimaLetra == "d":
                        SE()
                        reloj.tick(12)
                        NE()
                    robot.t = True
                    robot.l = False
                    robot.d = False
                    robot.r = False

                elif event.key == pygame.K_DOWN:
                    if ultimaLetra == "l" :
                        SE()
                    elif ultimaLetra == "r":
                        SO()
                    elif ultimaLetra == "t":
                        NO()
                        reloj.tick(12)
                        SO()

                    robot.d = True
                    robot.l = False
                    robot.r = False
                    robot.t = False

            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT:
                    robot.l = False
                    ultimaLetra = "l"


                elif event.key == pygame.K_RIGHT:
                    robot.r = False
                    ultimaLetra = "r"


                elif event.key == pygame.K_UP:
                    robot.t = False
                    ultimaLetra = "t"


                elif event.key == pygame.K_DOWN:
                    robot.d = False
                    ultimaLetra = "d"



        pintarVentana()




        robot.dibuja(ventana)
        for caja in listCajas:
            caja.dibujar(ventana)


        for x in listCajas:
            if x.rect.colliderect(robot.rect):
                print "Existe colocico"
            else:
                print "no hay"

        pygame.display.update()



principal()
