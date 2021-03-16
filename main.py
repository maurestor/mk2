import random, pygame, sys, time
from pygame.locals import *
from pygame import draw


pygame.init()
# Iniciando pygame...

pygame.display.set_caption("Local Market")

## Función principal del juego
def main():

	# Declaración de constantes y variables
	WHITE = (255, 255, 255)
	FPS, fps = 60, 60

	# resolucion
	s_width = 800
	s_heigh = 600

	#Centro del jugador
	player_x = s_width/2
	player_y = s_heigh/2

	#Direccion velocidad del personaje
	player_speed = 4.0
	direction = 'down'

	# Cargar fondo
	fondo = pygame.image.load("img/backgrounds/fondo.png")
	screen = pygame.display.set_mode((s_width,s_heigh), pygame.DOUBLEBUF)

	#Fuente 
	font = pygame.font.SysFont('mono', 14, bold=True)
	text = font.render("Hello, World", True, (0, 128, 0), (255,255,255))

	#carga el tiempo
	start_time = None
	playtime = 0.0

	clock = pygame.time.Clock()

	key_press = {"left": False, "right": False, "up": False, "down": False}


	#Mostrando colores en consola
	for item in pygame.colordict.THECOLORS.items():
		print(item)

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
			# direction = 'down'
			None
			

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


	# def tiempito(playtime, clock, fps, player_x, player_y):
	# 	# if start_time:
	# 	# 	time_since_start = pygame.time.get_ticks() - start_time
	# 	# 	msg = 'Milisegundos desde el inicio: '+str(time_since_start)
	# 	# 	screen.blit(font.render(msg, True, (100,100,100)), (30, 30))

	# 	milliseconds = clock.tick(fps)
	# 	playtime += milliseconds / 1000.0
	# 	draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS\n\nPosPlayer: {}"
	# 		.format(clock.get_fps(), " "*5, playtime, str(player_x)+' '+str(player_y)))


	def draw_text(text):
		"""Center text in window"""
		fw, fh = font.size(text)
		surface = font.render(text, True, (0, 0, 0))
		screen.blit(surface, (5,15))


	def main_menu():
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
		while runing:
			screen.fill((0,0,0))
			draw_text('Menu MK2', font, (255,255,255), screen, (20, 20))

			for event in pygame.event.get():
				if event.type == QUIT:
					runing=False
				elif event.type == pygame.KEYDOWN:
					if event.key == K_ESCAPE:
						runing = False
				# 3.- Se actualiza la pantalla
			pygame.display.update()
			clock.tick(fps)

		# Salir cuando runing=False
		pygame.quit()
		sys.exit(0)
		
	
	# Bucle principal
	player = PlayerMeca()

	runing = True
	while runing:
		
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
				runing = False
			elif event.type == pygame.KEYDOWN:
				if event.key == K_ESCAPE:
					runing = False
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

		if key_press["left"]:# == Si left es verdadero
			if player_x <= 0:
				direction = 'left'
			else:
				direction = 'left'
				player_x -= player_speed
		if key_press["right"]:
			if  player_x+32 >= s_width:
				direction = 'right'
			else:
				direction = 'right'
				player_x += player_speed
		if key_press["up"]:
			if  player_y <= 0:
				direction = 'up'
			else:
				direction = 'up'
				player_y -= player_speed
		if key_press["down"]:
			if  player_y+265 >= s_width: ## Arregla la medida del sprite para que quede a 64
				direction = 'down'
			else:
				direction = 'down'
				player_y += player_speed

		# print(mouse)
		# tiempito(playtime, clock, fps, player_x, player_y)
		milliseconds = clock.tick(fps)
		playtime += milliseconds / 500.0
		draw_text("FPS: {:6.3}{}PLAYTIME: {:6.3} SECONDS\n\nPosPlayer: {}"
		.format(clock.get_fps(), " "*5, playtime, str(player_x)+' '+str(player_y)))

		# 3.- Se actualiza la pantalla
		pygame.display.update()
		clock.tick(fps)

	# Salir cuando runing=False
	pygame.quit()
	sys.exit(0)

# Este fichero es el que ejecuta el juego principal
if __name__ == '__main__':
	main()