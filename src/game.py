import pygame
import settings
from Player import Player
from Platform import Platform
from Coin import Coin

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
            Platform(64, 64, 35, 550, settings.Line_middle_platform, settings.platform_width, settings.platform_height),             
            Platform(128, 64, 230, 550, settings.Line_middle_platform, 8, settings.platform_height),
            Platform(64, 64, 450, 520, settings.Line_middle_platform, settings.platform_width, settings.platform_height),
            Platform(128, 64, 680, 480, settings.Line_middle_platform, 8, settings.platform_height)
        ]
        
        self.coins = [
            Coin(230, 450, "gold"),
            Coin(400, 400, "silver")
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
        
        for coin in self.coins:
            coin.coin_update(self.player)
    
    def draw(self, current_time):
        self.screen.fill(settings.black)
        # draw player
        self.player.draw(self.screen)
        # draw platforms
        for platform in self.platforms:
            platform.draw(self.screen)
            platform.draw_hitbox(self.screen)
        # draw coins
        for coin in self.coins:
            coin.draw(self.screen)
            # coin.draw_hitbox(self.screen)
        self.draw_score(f"Score: {self.player.score}", settings.font_blocky , settings.white, 700, 5)
        # update screen
        pygame.display.flip()

    
    def draw_score(self, text, font, color, x, y):
        img = font.render(text, True, color)
        self.screen.blit(img, (x, y))