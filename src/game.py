import pygame
import settings
from Player import Player
from Platform import Platform

class Game:
    def __init__(self):
        # initialize the game
        pygame.init()
        # set window dimensions
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        # set title
        pygame.display.set_caption(settings.TITLE)
        # set clock
        self.clock = pygame.time.Clock()
        self.running = True
        
        # Create platforms
        self.platforms = [
            Platform(settings.SCREEN_WIDTH, 20, 200, 440, settings.red),  # Main platform
            Platform(100, 20, 50, 300, settings.blue),   # Floating platform 1
            Platform(100, 20, 650, 400, settings.green)   # Floating platform 2
        ]
                
        self.player = Player(150, 170, self.platforms)
        
    def run(self):
        # main game loop
        while self.running:
            # control frame rate
            self.clock.tick(settings.FPS)
            
            # get current time
            current_time = pygame.time.get_ticks()
            
            # handle events
            self.handle_events()
            
            # update
            self.update(current_time)
            
            # draw
            self.draw(current_time)
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self, current_time):
        # game logic
        pygame.display.update()
        # player movement
        self.player.player_update(current_time)
    
    def draw(self, current_time):
        self.screen.fill(settings.black)
        # draw player
        self.player.draw(self.screen)
        # draw platforms
        for platform in self.platforms:
            platform.draw(self.screen)
        # update screen
        pygame.display.flip()
