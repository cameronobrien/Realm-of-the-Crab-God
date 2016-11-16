"""
enemy

Handles the creation of an enemy sprite and how it is drawn to the scene

:author: Cameron O'Brien
"""
import pygame
WHITE = (255, 255, 255)  # Constant


class Enemy(pygame.sprite.Sprite):
    # This class represents the types of an enemy possible to be rendered to the scene

    def __init__(self, enemy_type, x, y, width, height):
        super.__init__()  # Call sprite constructor
        # Pass in the type of enemy, x/y pos, and width/height (64x64)
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.x = 0
        self.y = 0

        self.image = pygame.image.load("sprites/" + enemy_type + ".png").convert_alpha()
        self.rect = self.image.get_rect()
