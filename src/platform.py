import pygame 
import settings
class Platform:
    def __init__(self):
        self.surf = pygame.Surface((settings.SCREEN_WIDTH, 20))
        self.surf.fill(settings.red)
        self.rect = self.surf.get_rect(center = (settings.SCREEN_WIDTH/2, settings.SCREEN_HEIGHT - 10))
    
    def draw(self, interface):
        pygame.draw.rect(interface, settings.red, self.rect)