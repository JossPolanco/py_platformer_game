import pygame, settings
from utils import scale_images
from pygame.locals import *

class Coin:
    def __init__(self, x, y, type):
        # animation of the coin
        self.animation = []
        self.coinType = type
        self.getCoinType(self.coinType)
        self.anim_index = 0
        self.asset = self.animation[self.anim_index]
        self.update_time = pygame.time.get_ticks()

        # self.pos = settings.vec(x, y)
        self.rect = self.asset.get_rect()
        self.rect.center = (x, y)
        self.flip = False

    
    def coin_update(self, player):
        self.run_animation()      
        self.collision_handle(player)  
    
    
    def getCoinType(self, type):
        match type:
            case "bronze":
                for i in range(3):
                    img = pygame.image.load(f"assets/img/Coins/Bronze/Coin_bronze ({i}).png")
                    img = scale_images(img, settings.coin_width, settings.coin_height)        
                    self.animation.append(img)
                return self.animation
            
            case "silver":
                for i in range(3):
                    img = pygame.image.load(f"assets/img/Coins/Silver/Coin_silver ({i}).png")
                    img = scale_images(img, settings.coin_width, settings.coin_height)
                    self.animation.append(img)
                return self.animation
            
            case "gold":
                for i in range(3):
                    img = pygame.image.load(f"assets/img/Coins/Gold/Coin_gold ({i}).png")
                    img = scale_images(img, settings.coin_width, settings.coin_height)
                    self.animation.append(img)
                return self.animation
    
    
    def run_animation(self):
        cooldown_animation = 100          
        
        if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
            self.anim_index = self.anim_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.anim_index >= len(self.animation):
            self.anim_index = 0        
        self.asset = pygame.transform.flip(self.animation[self.anim_index], self.flip, False) 


    def draw(self, interface):
        interface.blit(self.asset, self.rect)
        
    # def draw_hitbox(self, interface):
    #     # Draw the hitbox of the platform in red
    #     pygame.draw.rect(interface, (255, 0, 0), self.rect, 2)
    
    def collision_handle(self, player):
        if self.rect.colliderect(player.shape):
            if self.coinType == "bronze":
                player.score += 1
            elif self.coinType == "silver":
                player.score += 3
            elif self.coinType == "gold":
                player.score += 5
            self.rect.center = (-1000, -1000)