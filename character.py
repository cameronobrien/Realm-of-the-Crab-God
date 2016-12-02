"""
character

Handles the creation and drawing of new characters to the scene.

:author: Cameron O'Brien
"""
import pygame
WHITE = (255, 255, 255)  # Constant


class Character(pygame.sprite.Sprite):
    # This class represents one of the five characters, a warrior, rogue, archer, wizard, or paladin

    def __init__(self, character_type, x, y, width, height, health, attack_damage):
        super().__init__()
        # Call the sprite constructor
        # Pass in the type of the character, and its x and y position, width and height.
        # Set the background color and set it to be transparent.
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        # Draw the character itself
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.image = pygame.image.load("sprites/playables/" + character_type + ".png").convert_alpha()
        self.health = 100
        self.attack_damage = 0

    def move(self, x, y):
        if self.rect.x >= 1216:
            self.rect.x = 10
            pass
        elif self.rect.x <= 5:
            self.rect.x = 1215
            pass
        else:
            self.rect.x += x
            pass
        if self.rect.y == 650:
            self.rect.y = 10
            pass
        elif self.rect.y == 5:
            self.rect.y = 640
            pass
        else:
            self.rect.y += y
            pass

    def set_stats(self):
        if self.character_type == "warrior":
            self.attack_damage = 10
            self.health = 100
        elif self.character_type == "rogue":
            self.attack_damage = 15
            self.health = 75
        elif self.character_type == "mage":
            self.attack_damage = 15
            self.health = 90
        elif self.character_type == "paladin":
            self.attack_damage = 5
            self.health = 200




