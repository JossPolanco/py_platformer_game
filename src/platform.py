import pygame 
import settings

class Platform:
    def __init__(self, width, height, x, y, color):
        # Crear superficie y rectángulo de la plataforma
        self.width = width
        self.height = height
        self.color = color
        
        # Crear rectángulo de la plataforma con posicionamiento correcto
        self.rect = pygame.Rect(x - width//2, y - height//2, width, height)
    
    def draw(self, interface):
        # Dibujar plataforma
        pygame.draw.rect(interface, self.color, self.rect)
    
    def get_top(self):
        # Devolver la posición superior de la plataforma
        return self.rect.top