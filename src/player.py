import pygame
import settings
from utils import load_frames, scale_images
from pygame.locals import *

class Player:
    def __init__(self, x, y, platforms):
        # Player asset        
        self.animations = []
        self.jump_animation = []
        
        for i in range(5):
            img = pygame.image.load(f"assets/img/Player/walk/Player_walk ({i}).png")
            img = scale_images(img, settings.player_width, settings.player_height)        
            self.animations.append(img)
        
        for i in range(2):
            img = pygame.image.load(f"assets/img/Player/jump/Player_jump ({i}).png")
            img = scale_images(img, settings.player_width, settings.player_height)        
            self.jump_animation.append(img)
            
        self.anim_index = 0
        self.asset = self.animations[self.anim_index]
        self.update_time = pygame.time.get_ticks()
        self.flip = False
        
        
        # Player dimensions
        self.width = 32
        self.height = 32
        
        # Find the lowest platform to position the player
        lowest_platform = max(platforms, key=lambda p: p.rect.top)
        
        # Position the player just above the lowest platform
        spawn_y = lowest_platform.rect.top - self.height
        
        # Create the player's rectangle
        self.shape = pygame.Rect(x, spawn_y, self.width, self.height)
        
        # Position and movement vectors
        self.pos = settings.vec(x, spawn_y)
        self.vel = settings.vec(0, 0)
        
        # Jump state variables
        self.on_ground = True
        self.can_jump = True
        self.jump_timer = 0
        self.JUMP_COOLDOWN = 100  # Milliseconds between jumps
        
        # Reference to platforms
        self.platforms = platforms

    
    # method that handles all the functionalities 
    def player_update(self, current_time):
        self.move()
        self.jump(current_time)
        self.aply_gravity()
        self.screen_limits()
        self.calculate_new_pos()
        self.handle_collision(self.platforms)        


    def active_run_animation(self):
        cooldown_animation = 50          
        
        if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
            self.anim_index = self.anim_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.anim_index >= len(self.animations):
            self.anim_index = 0        
        self.asset = pygame.transform.flip(self.animations[self.anim_index], self.flip, False)        
    
    
    def active_jump_animation(self):
        cooldown_animation = 50          
        
        if pygame.time.get_ticks() - self.update_time >= cooldown_animation:
            self.anim_index = self.anim_index + 1
            self.update_time = pygame.time.get_ticks()
        if self.anim_index >= len(self.jump_animation):
            self.anim_index = 0        
        self.asset = pygame.transform.flip(self.jump_animation[self.anim_index], self.flip, False)   


    def draw(self, interface):
        interface.blit(self.asset, self.shape)
        # pygame.draw.rect(interface, settings.blue, self.shape)
    
    
    def move(self):
        # Get pressed keys
        pressed_keys = pygame.key.get_pressed()
        
        # Horizontal movement
        if pressed_keys[K_a]:
            self.vel.x = -4  # Move left
            self.flip = True
            self.active_run_animation()
        elif pressed_keys[K_d]:
            self.vel.x = 4   # Move right
            self.flip = False
            self.active_run_animation()        
        else:
            self.vel.x = 0  # Stop horizontal movement   
            self.asset = pygame.transform.flip(self.animations[0], self.flip, False)     
        
        if pressed_keys[K_r]:
            self.pos = settings.vec(25, 500)
    
    def jump(self, current_time):
        pressed_keys = pygame.key.get_pressed()
        # Jump only if on the ground and can jump
        if self.on_ground and self.can_jump and pressed_keys[K_SPACE]:
            self.vel.y = -10  # Initial jump speed
            self.on_ground = False
            self.can_jump = False
            self.jump_timer = current_time
            self.update_jump_state(current_time)
            self.active_jump_animation()

    
    def update_jump_state(self, current_time):
        # Manage jump cooldown
        if not self.can_jump:
            if current_time - self.jump_timer >= self.JUMP_COOLDOWN:
                self.can_jump = True    

    
    def aply_gravity(self):
        # apply the gravity
        self.vel.y += 0.5
        # speed limit
        self.vel.y = min(self.vel.y, 10)


    def screen_limits(self):
        # Wrap around screen
        if self.pos.x > settings.SCREEN_WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = settings.SCREEN_WIDTH

    
    def calculate_new_pos(self):
        # calculates the new position
        return  self.pos + self.vel

    
    def handle_collision(self, platforms):
        # get new position
        new_pos = self.calculate_new_pos()
        new_rect = pygame.Rect(new_pos.x, new_pos.y, self.width, self.height)
        
        # Reset ground state
        ground_collision = False
        
        # Collision detection with platforms
        for platform in platforms:
            # Check collision
            if new_rect.colliderect(platform.rect):
                # Top collision (falling)
                if (self.vel.y > 0 and 
                    self.shape.bottom <= platform.rect.top + 10 and  # Margin for collision
                    new_rect.bottom >= platform.rect.top):
                    new_pos.y = platform.rect.top - self.height
                    self.vel.y = 0
                    ground_collision = True
                
                # Left side collision
                elif self.vel.x > 0 and new_rect.right > platform.rect.left and new_rect.left < platform.rect.left:
                    new_pos.x = platform.rect.left - self.width
                
                # Right side collision
                elif self.vel.x < 0 and new_rect.left < platform.rect.right and new_rect.right > platform.rect.right:
                    new_pos.x = platform.rect.right
        
        # Update ground state
        self.on_ground = ground_collision
        
        # If on the ground, reset jump
        if self.on_ground:
            self.can_jump = True
        
        # Update position
        self.pos = new_pos
        
        # Update rectangle
        self.shape.x = self.pos.x
        self.shape.y = self.pos.y