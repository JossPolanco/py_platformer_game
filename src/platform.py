import pygame 
import settings
class Platform:
    def __init__(self, width, height, x, y):
        self.surf = pygame.Surface((width, height))
        self.surf.fill(settings.red)
        self.rect = self.surf.get_rect(center = (x, y))
    
    def draw(self, interface):
        pygame.draw.rect(interface, settings.red, self.rect)