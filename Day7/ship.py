import pygame 
import os 

class Ship:
    def __init__(self, settings, screen):
        self.screen = screen 

        image_path = os.path.join(".", "images", "ship.bmp")
        self.image = pygame.image.load(image_path)
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        self.rect.centerx = float(self.screen_rect.centerx) 
        self.rect.bottom = self.screen_rect.bottom 

        self.settings = settings 

        self.moving_right = False 
        self.moving_left = False 

    def update(self):
        if self.moving_right == True and self.rect.right < self.screen_rect.right: 
            self.rect.centerx = self.rect.centerx + self.settings.ship_speed_factor

        if self.moving_left == True and self.rect.left > 0:
            self.rect.centerx = self.rect.centerx - self.settings.ship_speed_factor 

    def blitme(self):
        self.screen.blit(self.image, self.rect)

