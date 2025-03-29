import pygame
import settings
from Player import Player
from Platform import Platform
from Coin import Coin
from Spike import Spike
from Checkpoint import Checkpoint
class Game:
    def __init__(self):
        # initialize the game
        pygame.init()     
        
        # set window dimensions
        self.screen = pygame.display.set_mode((settings.SCREEN_WIDTH, settings.SCREEN_HEIGHT))
        
        # camera settings
        self.camera_offset = 0
        self.camera_target_offset = 0
        self.level = 0
        
        # set title
        pygame.display.set_caption(settings.TITLE)
        
        # set clock
        self.clock = pygame.time.Clock()
        self.running = True
        
        # other
        self.x_checkpoint = 0
        self.y_checkpoint = 170
        
        # Create platforms
        self.platforms = [
            Platform(64, 64, 35, 550, settings.Line_middle_platform, settings.platform_width, settings.platform_height),             
            Platform(128, 64, 230, 550, settings.Line_middle_platform, 8, settings.platform_height),
            Platform(64, 64, 450, 520, settings.Line_middle_platform, settings.platform_width, settings.platform_height),
            Platform(128, 64, 680, 480, settings.Line_middle_platform, 8, settings.platform_height),
            Platform(32, 32, 750, 370, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 600, 300, settings.Line_middle_platform, 2, 2),            
            Platform(64, 64, 450, 250, settings.Line_middle_platform, settings.platform_width, settings.platform_height),
            Platform(32, 32, 320, 200, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 230, 120, settings.Line_middle_platform, 2, 2),
            Platform(64, 64, 400, 80, settings.Line_middle_platform, settings.platform_width, settings.platform_height),
            Platform(64, 64, 400, -20, settings.Line_middle_platform, settings.platform_width, settings.platform_height),
            Platform(64, 64, 400, -1000, settings.Line_middle_platform, settings.platform_width, settings.platform_height),
        ]
        
        self.coins = [
            Coin(230, 450, "gold"),
            Coin(400, 400, "silver")
        ]
        
        self.spikes = [
            Spike(150, 150)
        ]
        
        self.checkpoints = [
            Checkpoint(200, 500),
            Checkpoint(400, -70),
            Checkpoint(300, -150)            
        ]
        
        
        level_count = 1
        for checkpoint in self.checkpoints:            
            checkpoint.setLevel(level_count)    
            level_count += 1    

        # creates the player
        self.player = Player(0, 170, self.platforms, 1)

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
            self.draw()
    
    def handle_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
    
    def update(self, current_time):
        # game logic
        pygame.display.update()
        # player movement
        self.player.player_update(current_time, self.x_checkpoint, self.y_checkpoint)
        
        # self.screen_position = self.player.move()
        
        for coin in self.coins:
            coin.coin_update(self.player)
        
        for spike in self.spikes:
            spike.spike_update(self.player, self.x_checkpoint, self.y_checkpoint)
        
        
        for checkpoint in self.checkpoints:
            # saves the previou state
            was_active_before = checkpoint.isActive
            
            # updates the checkpoint
            checkpoint.checkpoint_update(self.player)
            
            # checks if the checkpoint just be activate in the current frame
            if checkpoint.isActive and not was_active_before:
                print(f"¡Checkpoint level {checkpoint.getLevel()} activate")
                self.level = checkpoint.getLevel()
                
                self.x_checkpoint = checkpoint.rect.x
                self.y_checkpoint = checkpoint.rect.y - 30
                
                print(f"pos x check: {self.x_checkpoint}")
                print(f"pos y check: {self.y_checkpoint}")
                # if this does not is the first camera, it moves
                if checkpoint.getLevel() > 1:
                    self.camera_target_offset += settings.SCREEN_HEIGHT                    
        
        # smooth displacement of the cameraa
        if self.camera_offset < self.camera_target_offset:
            displacement = min(5, self.camera_target_offset - self.camera_offset)
            self.camera_offset += displacement            
            
            # adjust each element of the map
            for platform in self.platforms:
                platform.rect.y += displacement
            for coin in self.coins:
                coin.rect.y += displacement
            for spike in self.spikes:
                spike.rect.y += displacement
            for checkpoint in self.checkpoints:
                checkpoint.rect.y += displacement             
    
    def draw(self):
        self.screen.fill(settings.black)
        # draw platforms
        for platform in self.platforms:
            platform.draw(self.screen)
            platform.draw_hitbox(self.screen)
        # draw coins
        for coin in self.coins:
            coin.draw(self.screen)
            # coin.draw_hitbox(self.screen)
        # draw spikes
        for spike in self.spikes:
            spike.draw(self.screen)
        # draw checkpoints
        for checkpoint in self.checkpoints:
            checkpoint.draw(self.screen)
        # draw player
        self.player.draw(self.screen)                
        
        # draws the UI in the screen
        self.draw_ui(f"Score: {self.player.score}", settings.font_blocky , settings.white, 700, 5)
        self.draw_ui(f"Attemps: {self.player.attemps}", settings.font_blocky , settings.white, 5, 5)
        # update screen
        pygame.display.flip()

    
    def draw_ui(self, text, font, color, x, y):
        img = font.render(text, True, color)
        self.screen.blit(img, (x, y))