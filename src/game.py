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
        self.x_checkpoint = 20
        self.y_checkpoint = -100
        
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
            Platform(64, 64, 400, -30, settings.Line_middle_platform, settings.platform_width, settings.platform_height),
            Platform(64, 64, 250, -100, settings.Line_middle_platform, settings.platform_width, settings.platform_height),
            Platform(32, 32, 140, -180, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 50, -220, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 140, -300, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 300, -340, settings.Line_middle_platform, 2, 2),
            Platform(48, 48, 400, -270, settings.Line_middle_platform, 3, 3),
            Platform(32, 32, 580, -300, settings.Line_middle_platform, 2, 2),
            Platform(48, 48, 750, -350, settings.Line_middle_platform, 3, 3),
            Platform(32, 32, 600, -440, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 450, -500, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 250, -480, settings.Line_middle_platform, 2, 2),
            Platform(48, 48, 150, -500, settings.Line_middle_platform, 3, 3),
            Platform(32, 32, 160, -610, settings.Line_middle_platform, 2, 2),
            Platform(48, 48, 50, -680, settings.Line_middle_platform, 3, 3),
            Platform(48, 48, 150, -780, settings.Line_middle_platform, 3, 3),
            Platform(32, 32, 300, -720, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 500, -720, settings.Line_middle_platform, 2, 2),
            Platform(48, 48, 600, -780, settings.Line_middle_platform, 3, 3),
            Platform(32, 32, 750, -850, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 620, -930, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 500, -900, settings.Line_middle_platform, 2, 2),
            Platform(64, 64, 400, -980, settings.Line_middle_platform, settings.platform_width, settings.platform_height),
            Platform(32, 32, 250, -980, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 55, -1000, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 75, -1100, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 250, -1150, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 400, -1160, settings.Line_middle_platform, 2, 2),
            Platform(32, 32, 400, -1250, settings.Line_middle_platform, 2, 2),
        ]
        
        self.coins = [
            Coin(200, 500, "bronze"),
            Coin(450, 470, "silver"),
            Coin(640, 430, "bronze"),
            Coin(680, 430, "bronze"),
            Coin(720, 430, "bronze"),
            Coin(750, 340, "bronze"),
            Coin(600, 270, "bronze"),
            Coin(450, 200, "silver"),
            Coin(320, 170, "bronze"),
            Coin(230, 80, "bronze"),
            Coin(400, 30, "gold"),
            Coin(400, -180, "silver"),
            Coin(140, -220, "bronze"),
            Coin(50, -260, "bronze"),
            Coin(140, -340, "silver"),
            Coin(300, -380, "bronze"),
            Coin(405, -320, "bronze"),
            Coin(580, -340, "bronze"),
            Coin(750, -400, "bronze"),
            Coin(600, -480, "bronze"),
            Coin(200, -300, "gold"),
            Coin(450, -540, "bronze"),
            Coin(250, -520, "silver"),
            Coin(160, -545, "gold"),
            Coin(20, -820, "silver"),
            Coin(300, -760, "bronze"),
            Coin(200, -780, "gold"),
            Coin(500, -760, "bronze"),
            Coin(610, -830, "bronze"),
            Coin(750, -890, "bronze"),
            Coin(620, -970, "bronze"),
            Coin(500, -940, "bronze"),
            Coin(450, -900, "gold"),
            Coin(400, -1040, "silver"),
            Coin(55, -1040, "bronze"),
            Coin(75, -1140, "bronze"),
            Coin(250, -1180, "silver"),
            Coin(400, -1200, "gold"),
        ]
        
        self.spikes = [
            Spike(235, -135, 2, 2, 0),
            Spike(140, -280, 2, 2, 180),
            Spike(278, -340, 2, 1, 90),
            Spike(385, -300, 1, 2, 0),
            Spike(135, -530, 1, 2, 0),
            Spike(35, -710, 1, 2, 0),
            Spike(165, -810, 1, 2, 0),
            Spike(280, -720, 1.5, 1, 90),
            Spike(585, -810, 1, 2, 0),
            Spike(435, -980, 1, 2, 270),
            Spike(258, -998, 1, 1, 0),  
        ]
        
        self.checkpoints = [
            Checkpoint(250, 1500),
            Checkpoint(400, -80),
            Checkpoint(160, -640),
            Checkpoint(400, -1282)            
        ]
        
        
        level_count = 1
        for checkpoint in self.checkpoints:            
            checkpoint.setLevel(level_count)    
            level_count += 1    

        # creates the player
        self.player = Player(20, 450, self.platforms, 1)

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
                self.y_checkpoint = checkpoint.rect.y
                
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
        
        # player movement
        self.player.player_update(current_time, self.x_checkpoint, self.y_checkpoint)      
    
    def draw(self):
        self.screen.fill(settings.black)
        # draw platforms
        for platform in self.platforms:
            platform.draw(self.screen)
            # platform.draw_hitbox(self.screen)
        # draw coins
        for coin in self.coins:
            coin.draw(self.screen)
            # coin.draw_hitbox(self.screen)
        # draw spikes
        for spike in self.spikes:
            spike.draw(self.screen)
            # spike.draw_hitbox(self.screen)
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