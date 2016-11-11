"""
main

Handles the core game loop

:author: Cameron O'Brien
"""

import pygame
import random
from character import Character
width, height = 640, 480
background_color = (255, 255, 255)
bg = pygame.image.load("background_image.png")


class Game:

    def __init__(self):
        pygame.display.set_caption('Cameron\'s Practice Game')
        clock = pygame.time.Clock()
        self.all_sprites_list = pygame.sprite.Group()
        screen = pygame.display.set_mode((width, height))
        sprite = Character("warrior", 0, 0, 64, 64)
        sprite.rect.x = 200
        sprite.rect.y = 300
        self.all_sprites_list.add(sprite)
        running = True
        while running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
            screen.blit(bg, (0, 0))
            self.all_sprites_list.update()  # Game Logic
            self.all_sprites_list.draw(screen)  # Draw sprites
            self.handles_keys(0)
            pygame.display.flip()  # Refresh screen
            clock.tick(60)  # Number of frames per second

    def handles_keys(self, index):
        index = list(self.all_sprites_list)[0]
        key = pygame.key.get_pressed()
        if key[pygame.K_DOWN]:  # down key
            self.screen.blit(sprite.rect.x, (sprite.rect.y -5))  # move down
        elif key[pygame.K_UP]:  # up key
            self.screen.blit(sprite.rect.x, (sprite.rect.y +5))  # move up
        if key[pygame.K_RIGHT]:  # right key
            self.screen.blit(sprite.rect.x+5, sprite.rect.y + 5)  # move right
        elif key[pygame.K_LEFT]:  # left key
            self.screen.blit(sprite.rect.x-5, sprite.rect.y + 5) # move left


g = Game()
