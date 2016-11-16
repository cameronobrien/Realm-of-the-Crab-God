"""
main

Handles the core game loop

:author: Cameron O'Brien
"""

import pygame
import random
from character import Character
width, height = 1280, 720
background_color = (255, 255, 255)
bg = pygame.image.load("background_image.png")


class Game:

    def __init__(self):
        pygame.display.set_caption('Realm of the Crab God')
        clock = pygame.time.Clock()
        self.all_sprites_list = pygame.sprite.Group()
        screen = pygame.display.set_mode((width, height))
        sprite = Character("warrior", 0, 0, 64, 64)
        self.all_sprites_list.add(sprite)
        running = True
        pygame.key.set_repeat(10, 10)
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_LEFT:
                        sprite.rect.x -= 3.5
                    elif event.key == pygame.K_RIGHT:
                        sprite.rect.x += 3.5
                    elif event.key == pygame.K_UP:
                        sprite.rect.y -= 3.5
                    elif event.key == pygame.K_DOWN:
                        sprite.rect.y += 3.5

            screen.blit(bg, (0, 0))
            self.all_sprites_list.update()  # Game Logic
            self.all_sprites_list.draw(screen)  # Draw sprites
            pygame.display.flip()  # Refresh screen
            clock.tick(60)  # Number of frames per second


g = Game()
