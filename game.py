"""
main

Handles the core game loop

:author: Cameron O'Brien
"""
import pygame, random
from character import Character
width, height = 640, 480
background_color = (255, 255, 255)
bg = pygame.image.load("background_image.png")


class Game:
    screen = pygame.display.set_mode((width, height))
    all_sprites_list = pygame.sprite.Group()

    sprite = Character("warrior", 24, 24)
    sprite.rect.x = 200
    sprite.rect.y = 300

    # Add the sprite we have made to the list of sprites
    all_sprites_list.add(sprite)

    def __init__(self):
        pygame.display.set_caption('Cameron\'s Practice Game')
        clock = pygame.time.Clock()
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            Game.screen.blit(bg, (0, 0))
            Game.all_sprites_list.update()  # Game Logic
            Game.all_sprites_list.draw(Game.screen)  # Draw sprites
            pygame.display.flip()  # Refresh screen
            clock.tick(60)  # Number of frames per second

g = Game()
