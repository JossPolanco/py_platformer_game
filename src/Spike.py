import pygame
import settings
from pygame.locals import *
from utils import scale_images

class Spike:
    def __init__(self, x, y):
        # textures
        self.asset = pygame.image.load(settings.spike_texture)
        self.asset = scale_images(self.asset, 2, 2)
        # dimentions
        self.rect = self.asset.get_rect()
        self.rect.center = (x, y)           
    
    # update loop
    def spike_update(self, player, x_checkpoint, y_checkpoint):
        self.collision_handle(player, x_checkpoint, y_checkpoint)        
    
    
    def draw(self, interface):
        interface.blit(self.asset, self.rect)
        
    
    # checks the collitions with the player
    def collision_handle(self, player, x_checkpoint, y_checkpoint):
        if self.rect.colliderect(player.shape):            
            player.score = 0
            player.attemps += 1
            player.respawn(x_checkpoint, y_checkpoint)            