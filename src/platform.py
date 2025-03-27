import pygame 
import settings

class Platform:
    def __init__(self, width, height, x, y, color):
        # Create platform surface and rectangle
        self.width = width
        self.height = height
        self.color = color
        
        # Create platform rectangle with correct positioning
        self.rect = pygame.Rect(x - width//2, y - height//2, width, height)
    
    def draw(self, interface):
        # Draw platform
        pygame.draw.rect(interface, self.color, self.rect)
    
    def get_top(self):
        # Return the top position of the platform
        return self.rect.top