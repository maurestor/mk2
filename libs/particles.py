from .pygamextras import *
import pygame, random
from pygame.locals import *
from .player import Player

class ParticlesPrinciple:
    def __init__(self):
        self.particles = []
        
    def emit(self, pos=[]):
        # pass #Mueve y dibuja la particulongas
        if self.particles:
            
            # Borrar los sobrantes..
            self.delete_particles()

            for particle in self.particles:
                #move
                particle[0][0] += particle[2][0]
                particle[0][1] += particle[2][1]
                
                #shrink
                particle[1] -= random.randrange(10, 100)/100
                #draw a circe arround the particle
                pygame.draw.circle(screen,'gold', particle[0], int(particle[1]))
    
    def add_particles(self, pos=[]):
        pos_x = pos[0]
        pos_y = pos[1]

        radius = random.randrange(2, 10)
        direction_x = random.randrange(-5, 5)
        direction_y = random.randrange(-5, 5)
        particle_circle = [[pos_x, pos_y], radius, [direction_x, direction_y]]

        self.particles.append(particle_circle)

        
    def delete_particles(self):
        particle_copy = [particle for particle in self.particles if particle[1] > 0]
        if self.particles:
            self.particles = particle_copy

