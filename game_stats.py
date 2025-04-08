class GameStats:
    """Track statics for alien Invasion"""
    def __init__(self,ai_game):
        """Initalize statics"""
        self.settings = ai_game.settings
        self.reset_stats()

    def reset_stats(self):
        """Initalize statics that can change during the game"""
        self.ships_left = self.settings.ship_limit