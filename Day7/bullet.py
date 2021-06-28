import pygame 
from pygame.sprite import Sprite


class Bullet(Sprite):
    def __init__(self, settings, screen, ship):
        self.settings = settings
        self.screen = screen

        super(Bullet, self).__init__() # inheritance 

        self.rect = pygame.Rect(0, 0, self.settings.bullet_width, self.settings.bullet_height)
        self.rect.centerx = ship.rect.centerx 
        self.rect.top = ship.rect.top 

        self.y = float(self.rect.y)

        self.color = self.settings.bullet_color
        self.speed_factor = self.settings.bullet_speed_factor
    
    
    def update(self):
        self.y = self.y - self.speed_factor
        self.rect.y = self.y 
    

    def draw_bullet(self):
        pygame.draw.rect(self.screen, self.color, self.rect)






        