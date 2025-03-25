import pygame
import settings
from pygame.locals import *

class Player:
    def __init__(self, x, y):
        # dimentions of the shape
        self.shape = pygame.Rect(0, 0, 20, 20)
        # coords where is going to start
        self.shape.center = (x, y)
        # variables to the movement
        self.pos = settings.vec((10, 385))
        self.vel = settings.vec(0,0)
        self.acc = settings.vec(0,0)
        
    # function to draw the player
    def draw(self, interface):
        pygame.draw.rect(interface, settings.blue, self.shape)
        
    
    def move(self):
        self.acc = settings.vec(0,0)
    
        pressed_keys = pygame.key.get_pressed()
        
        # detects the input to move the player
        if pressed_keys[K_a]:
            self.acc.x = - settings.ACC 
        if pressed_keys[K_d]:
            self.acc.x = settings.ACC 
        if pressed_keys[K_s]:
            self.acc.y = settings.ACC
        if pressed_keys[K_w]:
            self.acc.y = - settings.ACC
        # multiply the movement with the fricction to add the friction
        self.acc.x += self.vel.x * settings.FRIC
        self.acc.y += self.vel.y * settings.FRIC
        
        self.vel += self.acc
        self.pos += self.vel + 0.5 * self.acc
        
        # if the player goes out of the screen we reset the position
        if self.pos.x > settings.SCREEN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = settings.SCREEN_WIDTH
        
        self.shape.midbottom = self.pos


