import pygame
import settings
from player import Player
from platform import Platform
class Game:
    def __init__(self):
        # initialice the game
        pygame.init()
        # set up the dimentions of the window
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        # set up the title
        pygame.display.set_caption(settings.TITLE)
        # set up the run time or clock
        self.clock = pygame.time.Clock()
        self.running = True
        
        self.player = Player(150, 150)
        self.platform = Platform(50, 50, 200, 200)
        
    def run(self):
        # update method
        while self.running:
            # set the frame rate
            self.clock.tick(settings.FPS)
            # here we are going to put the inputs
            self.handle_events()
            # update the screen each frame
            self.update()
            # self.draw()
            # draw the player
            self.player.draw(self.screen)
            
            self.platform.draw(self.screen)
            
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    
    def update(self):
        # here goes the logic
        pygame.display.update()
    
    
    def draw(self):
        self.screen.fill(settings.black)
        pygame.display.flip()