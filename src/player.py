import pygame
import settings

class Player:
    def __init__(self, x, y):
        # dimentions of the shape
        self.shape = pygame.Rect(0, 0, 20, 20)
        # coords where is going to start
        self.shape.center = (x, y)
        
    # function to draw the player
    def draw(self, interface):
        pygame.draw.rect(interface, settings.blue, self.shape)