import pygame
import random
import math

class Ray(object):

    def __init__(self, w, h):
        ## loads image, sets dimension of image, sets four different generation points and sets speed
        pygame.init()
        self.image = pygame.image.load("ray2.png")
        self.d = 14
        self.coord_1 = [ 100, 100 ]
        self.coord_2 = [ w - 100, 100 ]
        self.coord_3 = [ 100, h - 100 ]
        self.coord_4 = [ w - 100, h - 100 ]
        self.coord = [ self.coord_1, self.coord_2, self.coord_3, self.coord_4]
        self.coordinates = random.choice(self.coord)
        self.x, self.y = self.coordinates
        s = [-49., 49.]
        self.speed_x, self.speed_y = random.choice(s), random.choice(s)
        self.absorbed = False
        self.reversed = False
        self.caught = False
        self.error = False

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

    def check_caught(self):
        ## checks for inputs and sets if a ray of energy is caught or not
        key = pygame.key.get_pressed()
        if key[pygame.K_r] and key[pygame.K_u]:
            self.caught = True

    def reverse(self):
        ## manages the speed when an enemy hits the player
        self.speed_x = -self.speed_x*5
        self.speed_y = -self.speed_y*5
        self.moves(0.05)
        self.reversed = True
            
       

    
