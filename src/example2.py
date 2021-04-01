import pygame, sys
from pygame.locals import *

class Character(object):
	''' Jugador '''
	def __init__(self, x=0, y=0, speed=0):
		''' medidas largo y alto, carga absoluta del sprite'''
		self.x = x
		self.y = y
		self.speed = speed
		self.image = pygame.image.load('img/pnj/playerSprite.png')
		self.rect = pygame.image.load('img/pnj/playerSprite.png')


	def get_size(self):
		return self.image.get_size()


	def draw(self, direc):
		self.direc = direc
		# self.weight, self.width = self.image.get_rect()

		# display.blit(self.image, (self.x, self.y))
		self.width, self.heigth = self.image.get_size()

		if direc == 'down':
			self.image = self.image.subsurface(0,0,32,64)
		elif direc == 'right':
			self.image = self.image.subsurface(32,0,32,64)
		elif direc == 'up':
			self.image = self.image.subsurface(64,0,32,64)
		elif direc == 'left':
			self.image = self.image.subsurface(0,0,32,64)

		print(self.direc)
		print(self.image)
		print(self.image.get_rect())
		# return self.image

		display.blit(self.image, (self.x, self.y))


pygame.init()
(width, height) = (800, 600)
display = pygame.display.set_mode((width, height))
pygame.display.set_caption('Platforms')
clock = pygame.time.Clock()

direc = 'down'
pressed_keys = {"left": False, "right": False, "up": False, "down": False}

hero = Character(speed=5)
hero_width, hero_height = hero.get_size()
hero.x = width/2.0 - hero_width/2.0
hero.y = height/2.0 - hero_height/2.0

black = (0,0,0)
white = (150,150,150)

while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		elif event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				pressed_keys["left"] = True
			if event.key == pygame.K_RIGHT:
				pressed_keys["right"] = True
			if event.key == pygame.K_UP:
				pressed_keys["up"] = True
			if event.key == pygame.K_DOWN:
				pressed_keys["down"] = True
		elif event.type == pygame.KEYUP:
			if event.key == pygame.K_LEFT:
				pressed_keys["left"] = False
			if event.key == pygame.K_RIGHT:
				pressed_keys["right"] = False
			if event.key == pygame.K_UP:
				pressed_keys["up"] = False
			if event.key == pygame.K_DOWN:
				pressed_keys["down"] = False

	
	if pressed_keys["left"]:# == True is implied here
		direc = 'left'
		hero.x -= hero.speed
	if pressed_keys["right"]:
		direc = 'right'
		hero.x += hero.speed
	if pressed_keys["up"]:
		direc = 'up'
		hero.y -= hero.speed
	if pressed_keys["down"]:
		direc = 'down'
		hero.y += hero.speed

	
	display.fill(white)
	print('afuera '+direc)
	hero.draw(direc)
	hero.get_size()

	pygame.display.update()
	clock.tick(60)

