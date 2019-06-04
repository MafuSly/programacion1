import random
import math
from movimientos import *
from logger import *
from distancia import *

def generarCardumen(numero, largo, alto, velocidad=10):
	cardumen = []
	for i in range(numero):
		x, y		= random.randint(1, largo), random.randint(1, alto)
		course		= random.uniform(-1, 1)
		vx, vy		= random.randint(1, velocidad)/velocidad, random.randint(1, velocidad)/velocidad
		pez = [
				[x, y],		# 0 [0, 1]
				[vx, vy],	# 1 [0, 1]
		]
		logPez( pez )
		cardumen.append(pez)
	return cardumen

def distancia(i, j):
	return i*j



def moveWith(fish, vecinos): # ALINEAMIENTO
	return fish

def moveAway(fish, vecinos, min_dist=20): # SEPARATION
	return fish

