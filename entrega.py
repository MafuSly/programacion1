import random
import math
from logger import *

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

def corregir(boid, width, height, border=25):
	return boid

def moveCloser(fish, boids): # COHESION
	return fish

def moveWith(fish, boids): # ALINEAMIENTO
	return fish

def moveAway(fish, boids, min_dist=20): # SEPARATION
	return fish

def move(fish, max_speed):
	return fish

def vecindad(pez_i, boids, max_distance):
	return boids
