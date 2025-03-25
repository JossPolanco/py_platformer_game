import pygame
import settings
from player import Player
from platform import Platform

class Game:
    def __init__(self):
        # inicializar el juego
        pygame.init()
        # configurar dimensiones de la ventana
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        # configurar título
        pygame.display.set_caption(settings.TITLE)
        # configurar reloj
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Crear plataformas
        self.platforms = [
            Platform(settings.SCREEN_WIDTH, 20, 200, 440),  # Plataforma principal
            Platform(100, 20, 50, 300),   # Plataforma flotante 1
            Platform(100, 20, 350, 200)   # Plataforma flotante 2
        ]
        
        self.player = Player(150, 150, self.platforms)
        
    def run(self):
        # bucle principal del juego
        while self.running:
            # controlar velocidad de fotogramas
            self.clock.tick(settings.FPS)
            
            # obtener tiempo actual
            current_time = pygame.time.get_ticks()
            
            # manejar eventos
            self.handle_events()
            
            # actualizar
            self.update(current_time)
            
            # dibujar
            self.draw(current_time)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self, current_time):
        # lógica de juego
        pygame.display.update()
        # movimiento del jugador
        self.player.move(self.platforms)
    
    def draw(self, current_time):
        self.screen.fill(settings.black)
        # dibujar jugador
        self.player.draw(self.screen)
        # dibujar plataformas
        for platform in self.platforms:
            platform.draw(self.screen)
        # actualizar pantalla
        pygame.display.flip()
        
        # Detectar presión de tecla de salto
        if pygame.key.get_pressed()[pygame.K_SPACE]:
            self.player.jump(current_time)
        
        # Actualizar estado de salto
        self.player.update_jump_state(current_time)