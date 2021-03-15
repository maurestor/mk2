import random, pygame, sys, time
from pygame.locals import *
from pygame import draw

# Stats de tiempo
class Status():
	def __init__(self):
		self.last = pygame.time.get_ticks()
		self.countDown = 1000

	def fire(self, mouse):
		self.mouse = mouse
		ahora = pygame.time.get_ticks()
		if ahora - self.last >= self.countDown:
			self.last = ahora
			print(self.mouse)

def doub_press(self, key):
	''' Al presionar doble una tecla'''
	self.key = key
	return "Se presiono dobe la tecla "+self.key
	pass

class PlayerMeca():
	''' set controls '''
	def __init__(self, name='', gender='', options=[], active='', multi=''):
		pass

	def playerDraw(self, direction):
		''' Personaje principal '''
		player = pygame.image.load('img/pnj/playerSprite.png')

		if direction == 'down':
			player = player.subsurface(0,0,32,64)
		elif direction == 'right':
			player = player.subsurface(32,0,32,64)
		elif direction == 'up':
			player = player.subsurface(64,0,32,64)
		elif direction == 'left':
			player = player.subsurface(96,0,32,64)
		return player


## Función principal del juego
# def main():
## Se inicializa el juego
pygame.init()


FPS = 60
fpsClock = pygame.time.Clock()

# resolucion
s_width = 800
s_heigh = 600

pygame.display.set_caption("Local Market")
screen = pygame.display.set_mode((s_width,s_heigh))

# Cargar fondo
fondo = pygame.image.load("img/backgrounds/fondo.png")

#Direccion personaje
direction = 'down'

player_speed = 2.0

player_x = s_width/2
player_y = s_heigh/2

#carga el tiempo
start_time = None
clock = pygame.time.Clock()

# Declaración de constantes y variables
WHITE = (255, 255, 255)

key_press = {"left": False, "right": False, "up": False, "down": False}


#Meca Menu inventario
''' 
TODO
Crear un rectangulo HW al 75%
Transparentar el rectangulo
Dibujar barra superior con titulo
distinguir con otro color

Dibujar pestanias
Inventario personaje | opciones
'''
menu = ''


player = PlayerMeca()
# Bucle principal
while True:
	
	# 1.- Se dibuja la pantalla
	screen.fill(WHITE)

	# Mostrar fondo
	screen.blit(fondo, (0,0))

	# Se dibuja el personaje
	screen.blit(player.playerDraw(direction), (player_x, player_y))
	# screen.blit(menu, s_width, s_heigh)
	#mouse localizando 
	mouse = pygame.mouse.get_pos()

	pygame.draw.rect(screen, WHITE, pygame.Rect(s_width/2, s_heigh/2, 60, 60))

	#Dibujando Menu
	# screen.blit(menu, (0, 0))

	# print("log!" + ' '+direction )

	# 2.- Se comprueban los eventos
	for event in pygame.event.get():
		if event.type == QUIT:
			pygame.quit()
			sys.exit(0)
		elif event.type == pygame.KEYDOWN:
			if event.key == K_LEFT or event.key == K_a:
				key_press["left"] = True
			if event.key == K_RIGHT or event.key == K_d:
				key_press["right"] = True
			if event.key == K_UP or event.key == K_w:
				key_press["up"] = True
			if event.key == K_DOWN or event.key == K_s:
				key_press["down"] = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT or event.key == K_a:
				key_press["left"] = False
			if event.key == pygame.K_RIGHT or event.key == K_d:
				key_press["right"] = False
			if event.key == pygame.K_UP or event.key == K_w:
				key_press["up"] = False
			if event.key == pygame.K_DOWN or event.key == K_s:
				key_press["down"] = False

	if key_press["left"]:# == True is implied here
		direction = 'left'
		player_x -= player_speed
	if key_press["right"]:
		direction = 'right'
		player_x += player_speed
	if key_press["up"]:
		direction = 'up'
		player_y -= player_speed
	if key_press["down"]:
		direction = 'down'
		player_y += player_speed

	
	# print(mouse)

	# 3.- Se actualiza la pantalla
	pygame.display.update()
	clock.tick(FPS)

# Este fichero es el que ejecuta el juego principal
# if __name__ == '__main__':
# 	main()