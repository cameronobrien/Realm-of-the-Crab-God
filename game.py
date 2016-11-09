"""
main

Handles the core game loop

:author: Cameron O'Brien
"""
import pygame
import random
import math
width, height = 1280, 720
background_color = (255, 255, 255)


class Game:
    screen = pygame.display.set_mode((width, height))

    def __init__(self):
        pygame.display.set_caption('Cameron\'s Practice Game')
        Game.screen.fill(background_color)
        particle = Game.Particle(150, 50, 15)
        particle.display()
        for x in range(10):
            self.create_particle()
        pygame.display.flip()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

    def create_particle(self):
        c = Game.Particle(int(random.uniform(0, 1200)), int(random.uniform(0, 700)), 15)
        c.display()
        c.move()


    class Particle:
        def __init__(self, x, y, size):
            self.x = x
            self.y = y
            self.size = size
            self.color = (0, 0, 255)
            self.thickness = 1
            self.speed = 0.05
            self.angle = 5

        def display(self):
            pygame.draw.circle(Game.screen, self.color, (self.x, self.y), self.size, self.thickness)

        def move(self):
            self.x += math.sin(self.angle) * self.speed
            self.y -= math.cos(self.angle) * self.speed
            self.angle = math.pi/2

g = Game()
