"""
main

Handles the core game loop

:author: Cameron O'Brien
"""

import pygame
from character import Character
from enemy import Enemy
from role import Role
from constants import TITLE
width, height = 1280, 720
background_color = (255, 255, 255)
bg = pygame.image.load("background_image.png")

warrior = Role(10, 100, "Warrior")
rogue = Role(75, 15, "Rogue")
mage = Role(90, 15, "Mage")
paladin = Role(200, 5, "Paladin")



class Game:

    def __init__(self):
        clock = pygame.time.Clock()
        self.all_sprites_list = pygame.sprite.Group()
        screen = pygame.display.set_mode((width, height))
        sprite = Character(warrior, (500,500), (64,64))
        enemies = []
        for i in range(5):
            enemy = Enemy("evilwizard")
            enemies.append(enemy)
            self.all_sprites_list.add(enemy)
        self.all_sprites_list.add(sprite)
        running = True
        pygame.key.set_repeat(10, 10)
        # file = 'music/background_music1.mp3'
        # pygame.mixer.init()  # Initialize background music
        # pygame.mixer.music.load(file)
        # pygame.mixer.music.play()
        while running:
            pygame.display.set_caption(TITLE)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:  # Quit conditional
                    running = False
                if event.type == pygame.KEYDOWN and not pygame.sprite.collide_rect(enemy, sprite):
                    if event.key == pygame.K_LEFT:
                        sprite.move(-5, 0)
                    elif event.key == pygame.K_RIGHT:
                        sprite.move(5, 0)
                    elif event.key == pygame.K_UP:
                        sprite.move(0, -5)
                    elif event.key == pygame.K_DOWN:
                        sprite.move(0, 5)
            screen.blit(bg, (0, 0))
            for i in enemies:
                i.roam()
            self.all_sprites_list.update()  # Update the position of the sprite
            self.all_sprites_list.draw(screen)  # Redraw sprite
            pygame.display.flip()  # Refresh screen
            clock.tick(60)  # Number of frames per second

g = Game()
