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
            Platform(64, 64, 35, 688, settings.Line_middle_platform, settings.platform_width, settings.platform_height),             
            Platform(128, 64, 230, 688, settings.Line_middle_platform, 8, settings.platform_height),
            Platform(64, 64, 400, 620, settings.Line_middle_platform, settings.platform_width, settings.platform_height),
            Platform(128, 64, 580, 580, settings.Line_middle_platform, 8, settings.platform_height)
        ]

        self.player = Player(25, 170, self.platforms)
        
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
            platform.draw_hitbox(self.screen)
        # update screen
        pygame.display.flip()
