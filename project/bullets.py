import pygame
from math import *
from gameobjects.vector2 import Vector2

class Bullet(object):
    
    def __init__(self, shooter_x, shooter_y, shooter_rotation):
        ## sets coordinates, loads image, sets dimensions of the image and sets rotation speed
        pygame.init()
        self.image = pygame.image.load("bullet.png")   
        self.x = shooter_x      
        self.y = shooter_y
        self.image_rotation = shooter_rotation     
        self.image_rotation_speed = 120.    
        self.rotate = True
        self.shot = False
        self.hits_bg = False

    def moves(self, shooter_x, shooter_y):
        ## moves and rotates together with the shooter
        if self.rotate == True:
            self.x = shooter_x
            self.y = shooter_y
        else:
            self.x += self.heading_x*10
            self.y += self.heading_y*10
            
    def rotates(self, time):
        ## manages rotation according to inputs (like shooter)
        self.rotation_direction = 0
        pygame.event.get()
        key = pygame.key.get_pressed()
        if key[pygame.K_d]:
            self.rotation_direction = +1
        if key[pygame.K_k]:
            self.rotation_direction = -1
        self.rotated_image = pygame.transform.rotate(self.image, self.image_rotation)
        x, y = self.rotated_image.get_size()
        self.image_draw_pos = Vector2(self.x-x/2, self.y-y/2)
        self.image_rotation += self.rotation_direction * self.image_rotation_speed * time
        self.heading_x = -sin(self.image_rotation*pi/180.)
        self.heading_y = -cos(self.image_rotation*pi/180.)

    def check_shot(self):
        ## checks the inputs for the shot and if true, stops the rotation
        key = pygame.key.get_pressed()
        if key[pygame.K_c] and key[pygame.K_n]:
            self.shot = True
            self.rotate = False

    def hits_borders(self, background):
        ## checks if the bullet hits the walls (coloured in black)
        if background.get_at((int(self.x), int(self.y))) == (0, 0, 0):
            self.hits_bg = True
        else:
            self.hits_bg = False
            
            


        
            
            
        
