import random
import math

def generarCardumen(n, w, h, speed=10):
	boids = []
	for i in range(n):
		x, y		= random.randint(1, w), random.randint(1, h)
		course		= random.uniform(-1, 1)
		vx, vy		= random.randint(1, speed)/speed, random.randint(1, speed)/speed
		boids.append(
			[
				[x, y],		# 0 [0, 1]
				[vx, vy],	# 1 [0, 1]
			])
	return boids

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
