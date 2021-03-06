class Settings:
    def __init__(self):
        self.screen_width = 1200 
        self.screen_height = 800 
        self.bg_color = (107, 165, 227)

        # settings for ship speed 
        self.ship_speed_factor = 1.5

        # settings for bullet 
        self.bullet_width = 3
        self.bullet_height = 15 
        self.bullet_color = (60, 60, 60)
        self.bullet_speed_factor = 1
        self.bullets_allowed = 5