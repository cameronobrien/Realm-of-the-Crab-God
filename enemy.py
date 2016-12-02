"""
enemy

Handles the creation of an enemy sprite and how it is drawn to the scene, as well as moving the enemy, and attacking,
health conditionals, and more

:author: Cameron O'Brien
"""
import pygame
import random

# Constants
WHITE = (255, 255, 255)
WIDTH = 1280
HEIGHT = 720


class Enemy(pygame.sprite.Sprite):
    # This class represents the types of an enemy possible to be rendered to the scene

    def __init__(self, enemy_type):
        super().__init__()  # Call sprite constructor
        # Pass in the type of enemy, x/y pos, and width/height (64x64)
        self.image = pygame.Surface([66, 66])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
        self.rect = self.image.get_rect()
        self.rect.x = random.randrange(10, 1150)  # random start
        self.rect.y = random.randrange(10, 590)   # random start
        self.speed = 2
        self.move = [None, None]  # x-y coords to move to
        self.image = pygame.image.load("sprites/enemies/" + enemy_type + ".png").convert_alpha()
        self.direction = None  # direction to move the sprite

    def roam(self):
        directions = {"S": ((-1, 2), (1, self.speed)), "SW": ((-self.speed, -1), (1, self.speed)),
                      "W": ((-self.speed, -1), (-1, 2)), "NW": ((-self.speed, -1), (-self.speed, -1)),
                      "N": ((-1, 2), (-self.speed, -1)), "NE": ((1, self.speed), (-self.speed, -1)),
                      "E": ((1, self.speed), (-1, 2)),
                      "SE": ((1, self.speed), (1, self.speed))}  # ((min x, max x)(min y, max y))
        directionsName = ("S", "SW", "W", "NW", "N", "NE", "E", "SE")  # possible directions
        if random.randrange(0, 15) == 2:  # move about once every 15 frames
            if self.direction == None:  # if no direction is set, set a random one
                self.direction = random.choice(directionsName)
            else:
                a = directionsName.index(self.direction)  # get the index of direction in directions list
                b = random.randrange(a - 1,
                                     a + 2)  # set the direction to be the same, or one next to the current direction
                if b > len(directionsName) - 1:  # if direction index is outside the list, move back to the start
                    b = 0
                self.direction = directionsName[b]

            smalloffset = random.random()+0.05  # Random floating-point number between 0 and 1.2 ("Tiny number")
            self.move[0] = random.randrange(directions[self.direction][0][0],
                                            directions[self.direction][0][1]) + smalloffset
            self.move[1] = random.randrange(directions[self.direction][1][0],
                                            directions[self.direction][1][1]) + smalloffset
        if self.rect.x < 5 or self.rect.x > WIDTH - 5 or self.rect.y < 5 or self.rect.y > HEIGHT - 32:
            if self.rect.x < 5:
                self.direction = "E"
            elif self.rect.x > WIDTH - 5:
                self.direction = "W"
            elif self.rect.y < 5:
                self.direction = "S"
            elif self.rect.y > HEIGHT - 32:
                self.direction = "N"
            self.move[0] = random.randrange(directions[self.direction][0][0], directions[self.direction][0][1])
            self.move[1] = random.randrange(directions[self.direction][1][0], directions[self.direction][1][1])
            # change relative x and relative y to a random number between min x and max x/y
        if self.move[0] is not None:  # add the relative coordinates to the sprite's coordinates
            self.rect.x += self.move[0]
            self.rect.y += self.move[1]


