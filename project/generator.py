import pygame

class Generator(object):

    def __init__(self, player_x, player_y, player_d):
        ## sets coordinates, loads images, creates list of images and sets dimensions of images
        pygame.init()
        self.x = player_x + (player_d/2)
        self.y = player_y + (player_d/2)
        self.image_up = pygame.image.load("generator_up.png")
        self.image_right = pygame.image.load("generator_right.png")
        self.image_down = pygame.image.load("generator_down.png")
        self.image_left = pygame.image.load("generator_left.png")
        self.images = [ self.image_up, self.image_right, self.image_down, self.image_left ]
        self.index = 0
        self.d = 60

    def moves(self, player_x, player_y, player_d):
        ## manages movement, imports coordinates from player and modifies them according to the dimensions of the image
        if self.images[self.index] == self.image_up:
            self.w = 50
            self.h = 14
            self.x = player_x - 5
            self.y = player_y - 14
        elif self.images[self.index] == self.image_right:
            self.w = 14
            self.h = 50
            self.x = player_x + player_d
            self.y = player_y - 5
        elif self.images[self.index] == self.image_down:
            self.w = 50
            self.h = 14
            self.x = player_x - 5
            self.y = player_y + player_d
        elif self.images[self.index] == self.image_left:
            self.w = 14
            self.h = 50
            self.x = player_x - 14
            self.y = player_y - 5
