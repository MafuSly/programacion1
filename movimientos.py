from logger import *
import random
def mover(pez, MAX_SPEED  = 10):
    # TODO ver que hacer con la velocidad ?
    pez[0][0] = posX(pez) + velX(pez)
    pez[0][1] = posY(pez) + velY(pez)
    return pez



def corregir(pecesillo, ancho, alto, border=25):
    if (posX(pecesillo) > ancho):
        pecesillo[0][0] = 0
    elif (posY(pecesillo) > alto):
        pecesillo[0][1] = 0
    return pecesillo



def vecindad(pez_i, boids, max_distance):
    pez = boids[pez_i]
    x_sup = posX(pez) + max_distance
    x_inf = posX(pez) - max_distance
    y_sup = posY(pez) + max_distance
    y_inf = posY(pez) - max_distance
    vecinos = []
    for otroPez in boids:
        if(otroPez != pez):
            if(posX(otroPez) > x_inf and posX(otroPez) < x_sup and posY(otroPez) > y_inf and posY(otroPez) < y_sup):
                vecinos.append(otroPez)
    return vecinos



def moveCerca(pez, vecindad):
    #if len(vecindad) < 1:
    #    return vecindad
    #promdistX = 0
    #promdistY = 0
    #if boid in boids
    return pez



def moveLejos(pez, vecinos, dist_min):
    if len(vecindad) > 0:
        return vecindad
    distanciaX = 0
    distanciaY = 0
    pezcerca = 0
    for i in vecindades:

        if distancia < dis_min:
            pezcerca += 1
            difx = (posX-pez)
            dify = (posY-pez)

            if difx >= 0:
                difx = math.sqrt(dist_min) - difx
            elif difx <= 0:
                dify = -math.sqrt(dist_min) - difx
            if dify >= 0:
                dify = math.sqrt(dist_min) - dify
            elif dify <= 0:
                dify = -math.sqrt(dist_min) - dify

            distanciaX += difx
            distanciaY += dify

    if pezcerca == 0:
            return pezcerca



