import pygame

class Player(object):

    def __init__(self, w, h, background):
        ## sets coordinates, loads images, sets dimensions of the images and creates a list of them with index equal to 0
        self.x = w/2 - 20
        self.y = h/2 - 20
        self.d = 40
        self.background = background
        self.speed = 100.
        image_up = pygame.image.load("tank_up.png")
        image_down = pygame.image.load("tank_down.png")
        image_left = pygame.image.load("tank_left.png")
        image_right = pygame.image.load("tank_right.png")
        self.images = [image_up, image_down, image_left, image_right]
        self.index = 0

    def moves_up(self, time):
        ## manages movement upwards checking for collision with walls
        self.d_speed = self.speed * time
        if self.background.get_at((int(self.x), int(self.y))) != (0, 0, 0) and \
           self.background.get_at((int(self.x) + self.d/2, int(self.y))) != (0, 0, 0) and \
           self.background.get_at((int(self.x) + self.d, int(self.y))) != (0, 0, 0):
            self.y -= self.d_speed
        elif self.background.get_at((int(self.x), int(self.y))) == (0, 0, 0) or \
             self.background.get_at((int(self.x) + self.d/2, int(self.y))) == (0, 0, 0) or \
             self.background.get_at((int(self.x) + self.d, int(self.y))) == (0, 0, 0):
            self.y += 5     
    
    def moves_down(self, time):
        ## manages movement downwards checking for collision with walls
        self.d_speed = self.speed * time
        if self.background.get_at((int(self.x), int(self.y) + self.d)) != (0, 0, 0) and \
           self.background.get_at((int(self.x) + self.d/2, int(self.y) + self.d)) != (0, 0, 0) and \
           self.background.get_at((int(self.x) + self.d, int(self.y) + self.d)) != (0, 0, 0):
            self.y += self.d_speed
        elif self.background.get_at((int(self.x), int(self.y) + self.d)) == (0, 0, 0) or \
             self.background.get_at((int(self.x) + self.d/2, int(self.y) + self.d)) == (0, 0, 0) or \
             self.background.get_at((int(self.x) + self.d, int(self.y) + self.d)) == (0, 0, 0):
            self.y -= 5

    def moves_left(self, time):
        ## manages movement leftwards checking for collsion with walls
        self.d_speed = self.speed * time
        if self.background.get_at((int(self.x), int(self.y))) != (0, 0, 0) and \
           self.background.get_at((int(self.x), int(self.y) + self.d/2)) != (0, 0, 0) and \
           self.background.get_at((int(self.x), int(self.y) + self.d)) != (0, 0, 0):
            self.x -= self.d_speed
        elif self.background.get_at((int(self.x), int(self.y))) == (0, 0, 0) or \
             self.background.get_at((int(self.x), int(self.y) + self.d/2)) == (0, 0, 0) or \
             self.background.get_at((int(self.x), int(self.y) + self.d)) == (0, 0, 0):
            self.x += 5
            
    def moves_right(self, time):
        ## manages movement rightwards checking for collision with walls
        self.d_speed = self.speed * time
        if self.background.get_at((int(self.x) + self.d, int(self.y))) != (0, 0, 0) and \
           self.background.get_at((int(self.x) + self.d, int(self.y) + self.d/2)) != (0, 0, 0) and \
           self.background.get_at((int(self.x) + self.d, int(self.y) + self.d)) != (0, 0, 0):
            self.x += self.d_speed
        elif self.background.get_at((int(self.x) + self.d, int(self.y))) == (0, 0, 0) or \
             self.background.get_at((int(self.x) + self.d, int(self.y) + self.d/2)) == (0, 0, 0) or \
             self.background.get_at((int(self.x) + self.d, int(self.y) + self.d)) == (0, 0, 0):
            self.x -= 5


        
        
        
