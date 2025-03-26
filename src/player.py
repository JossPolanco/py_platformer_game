import pygame
import settings
from pygame.locals import *

class Player:
    def __init__(self, x, y, platforms):
        # Dimensiones del jugador
        self.width = 20
        self.height = 20
        
        # Encontrar la plataforma más baja para posicionar el jugador
        lowest_platform = max(platforms, key=lambda p: p.rect.top)
        
        # Posicionar el jugador justo encima de la plataforma más baja
        spawn_y = lowest_platform.rect.top - self.height
        
        # Crear el rectángulo del jugador
        self.shape = pygame.Rect(x, spawn_y, self.width, self.height)
        
        # Vectores de posición y movimiento
        self.pos = settings.vec(x, spawn_y)
        self.vel = settings.vec(0, 0)
        
        # Variables de estado de salto
        self.on_ground = True
        self.can_jump = True
        self.jump_timer = 0
        self.JUMP_COOLDOWN = 100  # Milisegundos entre saltos
        
        # Referencia a plataformas
        self.platforms = platforms
        
    def draw(self, interface):
        pygame.draw.rect(interface, settings.blue, self.shape)
    
    def jump(self, current_time):
        # Salto solo si está en el suelo y puede saltar
        if self.on_ground and self.can_jump:
            self.vel.y = -10  # Velocidad inicial de salto
            self.on_ground = False
            self.can_jump = False
            self.jump_timer = current_time
    
    def update_jump_state(self, current_time):
        # Gestionar el cooldown del salto
        if not self.can_jump:
            if current_time - self.jump_timer >= self.JUMP_COOLDOWN:
                self.can_jump = True
    
    def move(self, platforms):
        # Obtener teclas presionadas
        pressed_keys = pygame.key.get_pressed()
        
        # Movimiento horizontal
        if pressed_keys[K_a]:
            self.vel.x = -4  # Movimiento a la izquierda
        elif pressed_keys[K_d]:
            self.vel.x = 4   # Movimiento a la derecha
        else:
            self.vel.x = 0  # Detener movimiento horizontal
        
        # Aplicar gravedad
        self.vel.y += 0.5
        
        # Límite de velocidad vertical
        self.vel.y = min(self.vel.y, 10)
        
        # Actualizar posición
        new_pos = self.pos + self.vel
        new_rect = pygame.Rect(new_pos.x, new_pos.y, self.width, self.height)
        
        # Reiniciar estado de suelo
        ground_collision = False
        
        # Detección de colisiones con plataformas
        for platform in platforms:
            # Verificar colisión
            if new_rect.colliderect(platform.rect):
                # Colisión superior (cayendo)
                if (self.vel.y > 0 and 
                    self.shape.bottom <= platform.rect.top + 10 and  # Margen para colisión
                    new_rect.bottom >= platform.rect.top):
                    new_pos.y = platform.rect.top - self.height
                    self.vel.y = 0
                    ground_collision = True
                
                # Colisión lateral izquierda
                elif self.vel.x > 0 and new_rect.right > platform.rect.left and new_rect.left < platform.rect.left:
                    new_pos.x = platform.rect.left - self.width
                
                # Colisión lateral derecha
                elif self.vel.x < 0 and new_rect.left < platform.rect.right and new_rect.right > platform.rect.right:
                    new_pos.x = platform.rect.right
        
        # Actualizar estado de suelo
        self.on_ground = ground_collision
        
        # Si está en el suelo, restablecer el salto
        if self.on_ground:
            self.can_jump = True
        
        # Actualizar posición
        self.pos = new_pos
        
        # Actualizar rectángulo
        self.shape.x = self.pos.x
        self.shape.y = self.pos.y
        
        # Envolver en pantalla
        if self.pos.x > settings.SCREEN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = settings.SCREEN_WIDTH