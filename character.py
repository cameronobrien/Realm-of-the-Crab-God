import pygame

from constants import WINDOW_HEIGHT, WINDOW_WIDTH, WHITE, FILE_PATH_CHAR


class Character(pygame.sprite.Sprite):
    def __init__(self, role, position, dimensions):
        """
        :param role: role instance giving character attributes
        :param position: (x, y) position on screen
        :param dimensions: dimensions of the sprite for creating image
        """
        super().__init__()
        # Call the sprite constructor
        # Pass in the type of the character, and its x and y position, width and height.
        # Set the background color and set it to be transparent.
        self.image = pygame.Surface(dimensions)
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.image = pygame.image.load(FILE_PATH_CHAR + role.title + ".png").convert_alpha()

        # Draw the character itself
        # position is the tuple (x, y)
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = position

        self.attack = role.attack
        self.health = role.health
        self.title = role.title

    def move(self, x, y):
        if self.rect.x >= WINDOW_WIDTH - 65:
            self.rect.x = 10
            pass
        elif self.rect.x <= WINDOW_WIDTH - 1275:
            self.rect.x = 1215
            pass
        else:
            self.rect.x += x
            pass
        if self.rect.y == WINDOW_HEIGHT - 70:
            self.rect.y = 10
            pass
        elif self.rect.y == WINDOW_HEIGHT - 715:
            self.rect.y = 640
            pass
        else:
            self.rect.y += y
            pass
