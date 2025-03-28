import pygame
# screen configurations
SCREEN_WIDTH = 1295
SCREEN_HEIGHT = 720
FPS = 60

# colors (debug)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
black = (0, 0, 0)


# physics
vec = pygame.math.Vector2
ACC = 0.5
FRIC = -0.12

# dimentions
player_width = 2
player_height = 2

platform_width = 4
platform_height = 4

# TEXTURES
# platforms
Box_center_platform = "assets/img/Platforms/Box_center_platform.png"
Box_corner_bottom_left_platform = "assets/img/Platforms/Box_corner_bottom_left_platform.png"
Box_corner_bottom_right_platform = "assets/img/Platforms/Box_corner_bottom_right_platform.png"
Box_corner_top_left_platform = "assets/img/Platforms/Box_corner_top_left_platform.png"
Box_corner_top_right_platform = "assets/img/Platforms/Box_corner_top_right_platform.png"
Box_edge_left_platform = "assets/img/Platforms/Box_edge_left_platform.png"
Box_edge_right_platform = "assets/img/Platforms/Box_edge_right_platform.png"
Box_middle_bottom_platform = "/assets/img/Platforms/Box_middle_bottom_platform.png"
Box_middle_top_platform = "assets/img/Platforms/Box_middle_top_platform.png"
Line_corner_left_platform = "assets/img/Platforms/Line_corner_left_platform.png"
Line_corner_right_platform = "assets/img/Platforms/Line_corner_right_platform.png"
Line_middle_platform = "assets/img/Platforms/Line_middle_platform.png"
# objects
goald = "assets/img/Objects/Goald.png"
spike = "assets/img/Objects/Spike.png"
# extra
TITLE = "MegaGame"