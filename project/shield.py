import pygame

class Shield(object):

    def __init__(self, player_x, player_y, player_d):
        ## sets coordinates, loads images, creates list of images with initial index equal to zero
        pygame.init()
        self.x = player_x + (player_d/2)
        self.y = player_y + (player_d/2)
        self.image_up = pygame.image.load("shield_up.png")
        self.image_right = pygame.image.load("shield_right.png")
        self.image_down = pygame.image.load("shield_down.png")
        self.image_left = pygame.image.load("shield_left.png")
        self.images = [ self.image_up, self.image_right, self.image_down, self.image_left ]
        self.index = 0

    def moves(self, player_x, player_y, player_d):
        ## manages the rotation of the shield, sets coordinates of the image according to the index
        if self.images[self.index] == self.image_up:
            self.w = 66
            self.h = 20
            self.x = player_x - 13
            self.y = player_y - 24
        elif self.images[self.index] == self.image_right:
            self.w = 20
            self.h = 66
            self.x = player_x + player_d + 5
            self.y = player_y - 13
        elif self.images[self.index] == self.image_down:
            self.w = 66
            self.h = 20
            self.x = player_x - 13
            self.y = player_y + player_d + 5
        elif self.images[self.index] == self.image_left:
            self.w = 20
            self.h = 66
            self.x = player_x - 24
            self.y = player_y - 13

