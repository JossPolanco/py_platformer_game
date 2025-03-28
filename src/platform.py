import pygame 
import settings
from utils import scale_images
from pygame.locals import *


class Platform:
    def __init__(self, width, height, x, y, texture):
        # Create platform surface and rectangle
        self.width = width
        self.height = height
        self.texture = pygame.image.load(texture)
        self.texture = scale_images(self.texture, settings.platform_width, settings.platform_height)  
        
        # Create platform rectangle with correct positioning
        self.rect = pygame.Rect(x - width//2, y - height//2, width, height)
    
    def draw(self, interface):
        # Draw platform
        interface.blit(self.texture, self.rect)
    
    def get_top(self):
        # Return the top position of the platform
        return self.rect.top
    
    def draw_hitbox(self, interface):
        # Draw the hitbox of the platform in red
        pygame.draw.rect(interface, (255, 0, 0), self.rect, 2)