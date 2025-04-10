class Settings:
    """A calss to store all settings for alien invasion"""
    def __init__(self):
        """Initalize the game's settings."""
        #Screen seettings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230,230,230)
        #bullet setting
        self.bullet_speed = 4.0
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = (60,60,60)
        self.bullet_allowed = 3
        #ship speed
        self.ship_speed = 3
        # sth like respawn again after dyeing
        self.ship_limit = 3
        # Alien settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 10

        #how quickly the game speeds up
        self.speedup_scale = 1.1
        self.initalize_dynamic_settings()

    def initalize_dynamic_settings(self):
        """ Initalize settings that change throughout the game"""
        self.ship_speed = 3
        self.bullet_speed = 2.5
        self.alien_speed = 1

        # fleet direction of 1 represents right; -1 represents left
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase speed settings"""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale