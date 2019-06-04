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
    if (posY(pecesillo) > alto):
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






def moveCerca(fish, vecinos):
    if len(vecinos) > 1:

        avgX = 0
        avgY = 0

        for boid in vecinos:

            if pezx == velx and pezy == vely:
                continue

            avgX += (velx - pezx)
            avgY += (vely - pezy)

            avgX /= len(vecinos)
            avgY /= len(vecinos)


            vecinos = math.sqrt((largoX * largoX) + (largoY * largoY)) * -1.0

            veloX -= (largoX / 100)
            veloY -= (largoY / 100)# COHESION

    return fish

