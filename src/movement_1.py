'''
Explicacion de como funciona el motor de pygame sobre la imagenes

ejemplo blit
'''
import pygame as py
from pygame.locals import *

py.init()

# Dibujando un fondo
screen = [1, 1, 2, 2, 2, 1]
print('Pintando fondo:      ' + str(screen))

#Agregando un personaje(8) a la posicion 3
screen[3] = 8
print('Aad player:          ' + str(screen))


# Definiendo la posicion(3) del personaje(8)
playerpos = 3
screen[playerpos] = 8
print('Posicion jugador     ' + str(screen))

# Moviendo el personaje(8): -1 lugar
playerpos -= 1
screen[playerpos] = 8
print('Mover jugador:       ' + str(screen) + '\n')


# Crear un mapa 
background = [1, 1, 2, 2, 2, 1]
screen = [0]*6

for i in range(6):
	screen[i] = background[i]

print('\nCopiar fondo:        ' + str(screen))
playerpos = 3
screen[playerpos] = 8
print('screen w player      ' + str(screen))

screen[playerpos] = background[playerpos]
playerpos -= 1
screen[playerpos] = 8
print('screen limp mov1     ' + str(screen))

screen[playerpos] = background[playerpos]
playerpos -= 1
screen[playerpos] = 8
print('pantalla limpiada:   ' + str(screen))

terrain1 = py.image.load('./img/pnj/player.png')
terrain2 = py.image.load('./img/pnj/player.png')
background = [terrain1, terrain1, terrain2, terrain2, terrain2, terrain1]


for i in range(6):
	screen.blit(background[i], (i*10, 0))
	playerpos = 3
	screen.blit(terrain1, (playerpos*10, 0))


