import pygame
import random

class Enemy(object):

    def __init__(self, x, y):
        ## sets coordinates, loads image, sets dimensions of the image and generates random speed
        self.x = 210
        self.y = 250
        self.image = pygame.image.load("enemy.png")
        self.d = 30
        s = [-80., -60., 60., 80.]
        self.speed_x, self.speed_y = random.choice(s), random.choice(s)
        self.reversed = False
        self.error = False
        self.alive = True

    def moves(self, time):
        ## manages the movement using as differential distance = speed*time
        self.dx = self.speed_x * time
        self.dy = self.speed_y * time
        self.x += self.dx
        self.y += self.dy
        if self.reversed == True:
            self.speed_x = self.speed_x/5
            self.speed_y = self.speed_y/5
            self.reversed = False

    def bounces(self, background):
        ## checks if the background is black (walls) and manages an error can occur (the enemy goes out of the window - pixel out of range)
        try:
            if background.get_at((int(self.x) + self.d/2, int(self.y))) != (0, 0, 0):
                self.y -= 1
                self.speed_y = -self.speed_y

            if background.get_at((int(self.x) + self.d/2, int(self.y) + self.d)) != (0, 0, 0):
                self.y += 1
                self.speed_y = -self.speed_y

            if background.get_at((int(self.x), int(self.y) + self.d/2)) != (0, 0, 0):
                self.x -= 1
                self.speed_x = -self.speed_x

            if background.get_at((int(self.x) + self.d, int(self.y) + self.d/2)) != (0, 0, 0):
                self.x += 1
                self.speed_x = -self.speed_x
        except IndexError:
            self.error = True
            

    def reverse(self):
        ## manages the speed when an enemy hits the player
        self.speed_x = -self.speed_x*5
        self.speed_y = -self.speed_y*5
        self.moves(0.05)
        self.reversed = True

    
