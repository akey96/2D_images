#!/usr/bin/python
# -*- coding: utf-8 -*-


# modulo threading para hilos

import  pygame, sys, threading
# modulo para generar numero aleatorios
from  random import randrange
from pygame.locals import  *
from clases.caja import Caja
from clases.robot import Robot

pygame.init()

# variables globales
# ancho y alto de la ventana
ancho = 1000
largo = 700
ventana = pygame.display.set_mode((ancho, largo))

# variable que nos informara sobre el tipo de robot
nroRobot = 0

# numero de pixles que se movera la imagen
velocidad = 10

# timer para controlar el tiempo
reloj = pygame.time.Clock()
timer = 20

# ruta de las imagenes, en este caso solo es del robot verde, falta editar las fotos para el otro robot
listRutas = ["imagenes3"]

# lista con instancias de la Clase Caja
listCajas = [Caja("{}/caja.png".format(listRutas[nroRobot]), randrange(100,900,1), randrange(100,600,1)) for i in range(2)]

# instancia de la clase Robot
robot = Robot("{}".format(listRutas[nroRobot]), ancho / 2, largo / 2, velocidad, ancho, largo)

# cargamos en una variable la imagen de fondo
fondo = pygame.image.load("imagenes/fondo.png")


# funcion que pinta la pantalla con el fondo definido
def pintarVentana():
    ventana.blit(fondo,(0,0))


# funcion que mueve el robot a la derecha
def moverRight():
    while True:

        reloj.tick(timer)
        if robot.r:
            # esto para las coliciones
            antesX, antesY = robot.rect.left, robot.rect.top
            #print antesX, antesY
            robot.mvRight()


# funcion que mueve el robot a la izquierda
def moverLeft():
    while True:

        reloj.tick(timer)
        if robot.l:
            # esto para las coliciones
            antesX, antesY = robot.rect.left, robot.rect.top

            robot.mvLeff()


# funcion que mueve el robot a la arriba
def moverTop():
    while True:
        reloj.tick(timer)
        if robot.t:
            # esto para las coliciones
            antesX, antesY = robot.rect.left, robot.rect.top

            robot.mvtop()


# funcion que mueve el robot a la abajo
def moverDown():
    while True:
        reloj.tick(timer)
        if robot.d:
            # esto para las coliciones
            antesX, antesY = robot.rect.left, robot.rect.top

            robot.mvdown()




# metodos que mueven las imagen en el sentido Sur Oeste,para dar la impresion que se gira
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
    # implemetar metodo que nos devuleve si existe colicion entre el rect1 y rect2
    pass

# funcion principal
def principal():

    #variable para saber la orientacion del robot
    ultimaLetra = ""

    # String que nos informara datos del tobot
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

    # ciclo que solo acaba cuando cerramos la ventana
    while True:
        # timer
        reloj.tick(timer)

        # recorremos los eventos de pygame para poder tomar acciones en base a estas
        for event in pygame.event.get():

            # evento q captura el cierre de la ventana (X)
            if event.type == pygame.QUIT:
                pygame.display.quit()
                sys.exit()

            # eventos que captura si presionamos una tecla
            if event.type == pygame.KEYDOWN:

                # evento que captura si precionamos el cursor izquierdo
                if event.key == pygame.K_LEFT:


                    if ultimaLetra == "t" :
                        NE()
                    elif ultimaLetra == "d":
                        SE()
                    elif ultimaLetra == "r":
                        NO()
                        reloj.tick(12)
                        NE()

                    # atributos del robot para saber en que sentido se encuentra,
                    # en este caso lo cambiamos l que indica que l robot esta en en sentido left
                    robot.l = True
                    robot.r = False
                    robot.d = False
                    robot.t = False

                # evento que captura si precionamos el cursor derecha
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


        # pintamos la ventana del fondo
        pintarVentana()



        # pintamos las cajas
        robot.dibuja(ventana)
        for caja in listCajas:
            caja.dibujar(ventana)

        # aqui esta el error, solucionar sobre las coliciones
        for x in listCajas:
            if x.rect.colliderect(robot.rect):
                #print "Existe colocico"
                pass
            else:
                #print "no hay"
                pass

        #actualizamos la ventana
        pygame.display.update()



# metodo main de python
if __name__ == "__main__":
    principal()
