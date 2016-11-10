"""
character

Handles the creation and drawing of new characters to the scene.

:author: Cameron O'Brien
"""
import pygame
WHITE = (255, 255, 255)  # Constant


class Character(pygame.sprite.Sprite):
    # This class represents one of the five characters, a warrior, rogue, archer, wizard, or paladin

    def __init__(self, character_type, width, height):
        super().__init__()
        # Call the sprite constructor

        # Pass in the type of the character, and its x and y position, width and height.
        # Set the background color and set it to be transparent.
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)

        # Draw the character itself
        self.image = pygame.image.load("sprites/" + character_type + ".png").convert_alpha()
        self.rect = self.image.get_rect()
