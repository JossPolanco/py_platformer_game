import pygame
import settings

def load_frames(sheet, frame_width, frame_height, num_frames):
        frames = []
        for i in range(num_frames):
            rect = pygame.Rect(i * frame_width, 0, frame_width, frame_height)
            frame = sheet.subsurface(rect)
            # frame = scale_img(frame, MAIN_CHARACTER_SCALE)
            frames.append(frame)
        return frames

def scale_images(asset, width, height):    
    scaled_img = pygame.transform.scale(asset, (asset.get_width() * width, asset.get_height() * height))
    return scaled_img