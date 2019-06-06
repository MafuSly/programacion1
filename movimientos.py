from logger import *
import random
def mover(pez, MAX_SPEED):
    # TODO ver que hacer con la velocidad ?
    x_sup = posX(pez) + MAX_SPEED
    x_inf = posX(pez) - MAX_SPEED
    y_sup = posY(pez) + MAX_SPEED
    y_inf = posY(pez) - MAX_SPEED
    pez[0][0] = posX(pez) + velX(pez)
    pez[0][1] = posY(pez) + velY(pez)
    return pez



def corregir(pecesillo, ancho, alto, border=25):
    if (posX(pecesillo) > ancho):
        pecesillo[0][0] = 0
    elif (posY(pecesillo) > alto):
        pecesillo[0][1] = 0
    return pecesillo



def vecindad(pez_i, boids, MAX_DISTANCE):
    pez = boids[pez_i]
    x_sup = posX(pez) + MAX_DISTANCE
    x_inf = posX(pez) - MAX_DISTANCE
    y_sup = posY(pez) + MAX_DISTANCE
    y_inf = posY(pez) - MAX_DISTANCE
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



def moveLejos(pez, vecindad, min_dist):
    if len(vecindad) > 0:
        return vecindad
    distanciaX = 0
    distanciaY = 0
    pezcerca = 0
    for i in vecindades:

        if distancia < min_dist:
            pezcerca += 1
            difx = (posX - pez)
            dify = (posY - pez)

            if difx >= 0:
                difx = math.sqrt(dist_min)**0.5 - difx
            elif difx <= 0:
                dify = -math.sqrt(dist_min)**0.5 - difx
            if dify >= 0:
                dify = math.sqrt(dist_min)**0.5 - dify
            elif dify <= 0:
                dify = -math.sqrt(dist_min)**0.5 - dify

            distanciaX += difx
            distanciaY += dify

    if pezcerca != 0:
        return pezcerca

    pvelozx = pvelozx / len(vecindad)
    pvelozy = pvelozy / len(vecindad)

    return pezcerca



def moveWith(pez, vecindad):  # ALINEAMIENTO
    for v in vecindad:
        x = pvelozx
        y = pvelozy
    x = x/len(vecindad)
    y = y/len(vecindad)

    return pez



