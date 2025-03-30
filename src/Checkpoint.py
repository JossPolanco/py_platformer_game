import pygame
import settings
from utils import scale_images

class Checkpoint:
    def __init__(self, x, y):
        # textures
        self.asset = pygame.image.load(settings.checkpoint_texture)
        self.asset = scale_images(self.asset, 2, 2)
        
        # dimentions
        self.rect = self.asset.get_rect()
        self.rect.center = (x, y)
        
        # others
        self.flip = False
        self.isActive = False
        self.level = 0
    
    
    # update loop
    def checkpoint_update(self, player):
        self.collision_handle(player)        
        
    def draw(self, interface):
        interface.blit(self.asset, self.rect)
    
    
    # checks the collitions with the player
    def collision_handle(self, player):
        if self.rect.colliderect(player.shape) and self.isActive == False:                        
            self.isActive = True         
            print(f"level: {self.level}")

    
    # sets the level to each checkpoint
    def setLevel(self, level):
        self.level = level        
    
    
    # gets the level of each checkpoint
    def getLevel(self):
        return self.level
    