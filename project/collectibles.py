import pygame
import random

class Collectible(object):

    def __init__(self, w, h):
        ## imports all the images of the collectibles and creates a list of them
        ## with the initial index equal to zero
        pygame.init()
        coll_1 = pygame.image.load("collectible1.png")
        coll_2 = pygame.image.load("collectible2.png")
        coll_3 = pygame.image.load("collectible3.png")
        coll_4 = pygame.image.load("collectible4.png")
        coll_5 = pygame.image.load("collectible5.png")
        coll_6 = pygame.image.load("collectible6.png")
        coll_7 = pygame.image.load("collectible7.png")
        coll_8 = pygame.image.load("collectible8.png")
        coll_9 = pygame.image.load("collectible9.png")
        coll_10 = pygame.image.load("collectible10.png")
        self.collectibles = [coll_1, coll_2, coll_3, coll_4, coll_5, coll_6, coll_7, coll_8, coll_9, coll_10]
        self.index = 0
        self.blit = False
        self.w = w
        self.h = h
        self.finished = False
        self.sound = pygame.mixer.Sound("blip.wav")

    def generate_coord(self):
        ## generates random coordinates whenever is colled
        self.x = random.randint(0, self.w)
        self.y = random.randint(0, self.h)

    def blit_check(self, background, timer):
        ## sets the time of the whole game and every 15 seconds tries to blit a collectible
        ## before blitting checks if the coordinates are on black (walls) or not
        ## if yes generates new coordinates
        ## when the index of the collectible list is 10 finishes the game
        if timer == 30*5 or timer == 30* 20 or timer == 30*35 \
           or timer == 30*50 or timer == 30*65 or timer == 30*80 \
           or timer == 30*95 or timer == 30*110 or timer == 30 * 125 \
           or timer == 30*140:
            if timer == 125:
                self.sound.play()
            self.generate_coord()
            while background.get_at((self.x, self.y))==(0,0,0) or \
                  background.get_at((self.x + 20, self.y)) == (0, 0, 0) or \
                  background.get_at((self.x, self.y + 20)) == (0, 0, 0) or \
                  background.get_at((self.x + 20, self.y + 20)) == (0, 0, 0):
                self.generate_coord()
            self.blit = True
            self.image = self.collectibles[self.index]
            self.index += 1
            if self.index == 10:
                self.finished = True

        
