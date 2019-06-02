from logger import *
def mover(pez, maxima_velocidad):
    # TODO ver que hacer con la velocidad ?
    pez[0][0] = posX(pez) + pez[1][0]
    pez[0][1] = posY(pez) + pez[1][1]
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

