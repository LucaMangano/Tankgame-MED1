import pygame
from player import Player
from shooter import Shooter
from shield import Shield
from generator import Generator
from bullets import Bullet
from enemies import Enemy
from enemies_2 import Enemy_2
from collectibles import Collectible
from rays import Ray
import math

class Game(object):

    def __init__(self):
        ## sets dimension of the screen and the background
        pygame.init()
        self.w = 900
        self.h = 600
        self.screen = pygame.display.set_mode((self.w, self.h), pygame.FULLSCREEN)
        self.background = pygame.image.load("background.png")
        
        ## creates all the objects and lists needed for the game
        self.player = Player(self.w, self.h, self.background)
        self.shooter = Shooter(self.player.x, self.player.y, self.player.d)
        self.shield = Shield(self.player.x, self.player.y, self.player.d)
        self.generator = Generator(self.player.x, self.player.y, self.player.d)
        self.bullet = Bullet(self.shooter.x, self.shooter.y, self.shooter.image_rotation)
        self.enemies = [ Enemy(self.w, self.h) ]
        self.enemies_2 = []
        self.counter_enemies_2_dead = 0
        self.collectible = Collectible(self.w, self.h)
        self.ray = Ray(self.w, self.h)

        ## loads energy image and sets its default value
        self.energy_5 = pygame.image.load("energy_5.png")
        self.energy = 100

        ## sets all default values
        self.points = 0
        self.killed_big_enemies = 0
        self.killed_small_enemies = 0
        self.rays_collected = 0
        self.collectibles_collected = 0

        ## initializes fonts and creates the first text
        font = pygame.font.SysFont("comic",64)
        self.font = pygame.font.SysFont("arial", 10)
        text = font.render("Click to play", True, (255, 255, 255))

        ## loads sound
        self.sound = pygame.mixer.Sound("blip.wav")

        ## sets timer and default timer variables
        self.clock = pygame.time.Clock()
        self.timer = 0
        self.seconds = 0
        self.minutes = 0

        ## manages beginning screen and first inputs
        beginning = True
        while beginning:
            self.screen.fill((0, 0, 0))
            self.screen.blit(text, ((self.w/2)-150, (self.h/2)-64))
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                if event.type == pygame.MOUSEBUTTONUP:
                    beginning = False
                    self.screen.blit(self.background, (0, 0))
                    self.screen.blit(self.player.images[1], (self.player.x, self.player.y))
                    self.screen.blit(self.shooter.image, (self.shooter.x, self.shooter.y))                  
                    self.running()
            pygame.display.update()

    def running(self):
        while True:

            ## manages time
            time_passed = self.clock.tick(30)
            time_seconds = time_passed / 1000.
            self.timer += 1
            self.seconds += 0.03
            if self.seconds >= 60:
                self.minutes +=1
                self.seconds = 0

            ## gets all the inputs and calls function related to each input
            for event in pygame.event.get():
                if event.type == pygame.KEYUP:
                    if event.key == pygame.K_ESCAPE:
                        pygame.display.quit()
                    if event.key == pygame.K_a:
                        self.shield.index -= 1
                        if self.shield.index == -5:
                            self.shield.index = -1
                    elif event.key == pygame.K_j:
                        self.shield.index += 1
                        if self.shield.index == 4:
                            self.shield.index = 0
                    elif event.key == pygame.K_l:
                        self.generator.index += 1
                        if self.generator.index == 4:
                            self.generator.index = 0
                    elif event.key == pygame.K_s:
                        self.generator.index -= 1
                        if self.generator.index == -5:
                            self.generator.index = -1
            key = pygame.key.get_pressed()
            if key[pygame.K_UP]:     
                self.player.moves_up(time_seconds)
                self.player.index = 0
            if key[pygame.K_DOWN]:
                self.player.moves_down(time_seconds)
                self.player.index = 1
            if key[pygame.K_LEFT]:
                self.player.moves_left(time_seconds)
                self.player.index = 2
            if key[pygame.K_RIGHT]:
                self.player.moves_right(time_seconds)
                self.player.index = 3

            ## blits the background
            self.screen.blit(self.background, (0, 0))

            ## manages energy and prints it
            if self.energy >= 100:
                self.energy = 100
            if self.energy <= 10:
                self.sound.play()
            if self.energy <= 0:
                self.collectible.finished = True
            for n in xrange(0,self.energy/5):
                self.screen.blit(self.energy_5, (self.w - 35 - 10*n, 4))

            ## manages the text (points and time)
            text = self.font.render((str(self.minutes)+":"+str(self.seconds)), True, (255, 255, 255))
            self.screen.blit(text, (10, 10))
            text = self.font.render(("Points: "+str(self.points)), True, (255, 255, 255))
            self.screen.blit(text, (440, 10))

            ## manages collectibles
            self.collectible.blit_check(self.background, self.timer)
            if self.collectible.blit:
                self.screen.blit(self.collectible.image, (self.collectible.x, self.collectible.y))
                self.collectible_rect = pygame.Rect(self.collectible.x, self.collectible.y, 20, 20)

            ## manages player and collision with collectible
            self.screen.blit(self.player.images[self.player.index], (self.player.x, self.player.y))
            self.player_rect = pygame.Rect(self.player.x, self.player.y, 40, 40)
            if self.collectible.blit:
                if self.player_rect.colliderect(self.collectible_rect):
                    i = self.collectible.index
                    self.collectible = Collectible(self.w, self.h)
                    self.collectible.index = i
                    self.points += 100
                    self.collectibles_collected += 1

            ## manages bullet, checks hits with walls
            self.bullet.moves(self.shooter.x, self.shooter.y)
            if self.bullet.rotate:
                self.bullet.rotates(time_seconds)       
                self.screen.blit(self.bullet.rotated_image, self.bullet.image_draw_pos)
                self.bullet.check_shot()
                if self.bullet.shot:
                    self.energy -= 5
            if self.bullet.shot:
                self.screen.blit(self.bullet.rotated_image, (self.bullet.x, self.bullet.y))
                self.bullet.hits_borders(self.background)
            if self.bullet.hits_bg:
                self.bullet = Bullet(self.shooter.x, self.shooter.y, self.shooter.image_rotation)
            self.bullet_rect = pygame.Rect(self.bullet.x, self.bullet.y, 4, 10)

            ## manages generator
            self.generator.moves(self.player.x, self.player.y, self.player.d)
            self.screen.blit(self.generator.images[self.generator.index], (self.generator.x, self.generator.y))
            generator_rect = pygame.Rect(self.generator.x, self.generator.y, self.generator.w, self.generator.h)

            ## manages shooter
            self.shooter.moves(self.player.x, self.player.y, self.player.d)
            self.shooter.rotates(time_seconds)
            self.screen.blit(self.shooter.rotated_image, self.shooter.image_draw_pos)

            ## manages shield
            self.shield.moves(self.player.x, self.player.y, self.player.d)
            self.screen.blit(self.shield.images[self.shield.index], (self.shield.x, self.shield.y))
            shield_rect = pygame.Rect(self.shield.x, self.shield.y, self.shield.w, self.shield.h)

            ## manages big enemies one by one, checks collisions with bullets, shield and tank
            for n in xrange(0, len(self.enemies)):
                enemy = self.enemies[n]
                enemy.moves(time_seconds)
                enemy.bounces(self.background)
                if enemy.error:
                    self.enemies[n] = Enemy(self.w, self.h)
                self.screen.blit(enemy.image, (enemy.x, enemy.y))
                enemy_rect = pygame.Rect(enemy.x, enemy.y, enemy.d, enemy.d)
                if enemy_rect.colliderect(self.bullet_rect):
                    self.bullet = Bullet(self.shooter.x, self.shooter.y, self.shooter.image_rotation)
                    self.enemies_2.append(Enemy_2(enemy.x, enemy.y))
                    self.enemies_2.append(Enemy_2(enemy.x, enemy.y))
                    self.enemies_2.append(Enemy_2(enemy.x, enemy.y))
                    enemy.alive = False
                    self.points += 10
                    self.killed_big_enemies += 1
                elif enemy_rect.colliderect(shield_rect):
                    enemy.reverse()
                    self.energy -= 5
                elif enemy_rect.colliderect(self.player_rect):
                    enemy.reverse()
                    self.energy -= 10
            if (self.timer == 30*5 or self.timer == 30*10) and len(self.enemies) <= 2:
                self.enemies.append(Enemy(self.w, self.h))
            ## temporary list to manage the elimination of some enemies
            l = []
            for n in xrange(0, len(self.enemies)):
                enemy = self.enemies[n]
                if enemy.alive:
                    l.append(self.enemies[n])
            self.enemies = l

            ## manages small enemies one by one, checks collision with bullets, shield and tank
            for n in xrange(0, len(self.enemies_2)):
                enemy_2 = self.enemies_2[n]
                enemy_2.moves(time_seconds)
                enemy_2.bounces(self.background)
                if enemy.error:
                    self.enemies_2[n] = Enemy_2(self.w, self.h)
                self.screen.blit(enemy_2.image, (enemy_2.x, enemy_2.y))
                enemy_2_rect = pygame.Rect(enemy_2.x, enemy_2.y, enemy_2.d, enemy_2.d)
                if enemy_2_rect.colliderect(self.player_rect):
                    enemy_2.reverse()
                    self.energy -= 10
                elif enemy_2_rect.colliderect(shield_rect):
                    enemy_2.reverse()
                    self.energy -= 5
                elif enemy_2_rect.colliderect(self.bullet_rect):
                    self.bullet = Bullet(self.shooter.x, self.shooter.y, self.shooter.image_rotation)
                    enemy_2.alive = False
                    self.counter_enemies_2_dead += 1
                    self.points += 10
                    self.killed_small_enemies += 1
            ## temporary list to manage the elimination of some enemies
            l = []
            for n in xrange(0, len(self.enemies_2)):
                enemy_2 = self.enemies_2[n]
                if enemy_2.alive:
                    l.append(self.enemies_2[n])
            self.enemies_2 = l
            if self.counter_enemies_2_dead == 3:
                self.counter_enemies_2_dead = 0
                self.enemies.append(Enemy(self.w, self.h))

            ## manages rays of energy and collision with generator and tank and manages life time
            self.ray.moves(time_seconds)
            self.ray.bounces(self.background)
            self.screen.blit(self.ray.image, (self.ray.x, self.ray.y))
            ray_rect = pygame.Rect(self.ray.x, self.ray.y, self.ray.d, self.ray.d)
            if ray_rect.colliderect(generator_rect):
                self.ray.check_caught()
                if self.ray.caught:
                    self.ray = Ray(self.w, self.h)
                    self.energy += 20
                    self.points += 10
                    self.rays_collected += 1
                else:
                    self.ray.reverse()
            if ray_rect.colliderect(self.player_rect):
                self.ray.reverse()
            if self.timer >= 30*15 and self.timer <= 30*15.01 or \
               self.timer >= 30*30 and self.timer <= 30*30.01 or \
               self.timer >= 30*45 and self.timer <= 30*45.01 or \
               self.timer >= 30*60 and self.timer <= 30*60.01 or \
               self.timer >= 30*75 and self.timer <= 30*75.01 or \
               self.timer >= 30*90 and self.timer <= 30*90.01 or \
               self.timer >= 30*105 and self.timer <= 30*105.01 or \
               self.timer >= 30*120 and self.timer <= 30*120.01:
                self.ray = Ray(self.w, self.h)

            ## manages the end of the loop
            if self.collectible.finished == True:
                pygame.display.quit()
                self.end()
                
            pygame.display.update()
            
    def end(self):
        ## creates a whole new screen, calculates points and blits results
        pygame.init()
        screen = pygame.display.set_mode((600, 300), 0, 32)
        screen.fill((0,0,0))

        points = self.seconds+(self.minutes*60)+self.energy+self.points
        if self.killed_big_enemies >= 3 and self.killed_small_enemies >= 3 and self.rays_collected >= 3 and self.collectibles_collected >= 4:
            msg = "You did great!!!"
        else:
            msg = "You could have done better! ;)"

        end = True
        while end:     
            font = pygame.font.SysFont("comic",40)
            text = font.render(("Total points: "+str(points)), True, (255, 255, 255))
            text1 = font.render(msg, True, (255, 255, 255))
            screen.blit(text, (100, 100))
            screen.blit(text1, (100,200))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.display.quit()
                    end = False
            pygame.display.update()
      
Game()















