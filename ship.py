import pygame

class Ship:
    """A class to manage the ship."""
    def __init__(self,ai_game):
        """Initalize the ship and set it's starting postition"""
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()
        self.settings = ai_game.settings

        #load the ship imaghe and its rect
        self.image = pygame.image.load("images\ship_recolor_001.png")
        self.rect = self.image.get_rect()

        #start each new ship at the bottom center of thge screen 
        self.rect.midbottom = self.screen_rect.midbottom
        # Store a float for the ships exact horizental Position
        self.x = float(self.rect.x)
        #movement flags
        self.moving_right = False
        self.moving_left = False
    def update(self):
        """Update the ships position based on the movement flag."""
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.x += self.settings.ship_speed
        if self.moving_left and self.rect.left > 0:
            self.x -= self.settings.ship_speed
        #update rect object from self.x
        self.rect.x = self.x
    def blitme(self):
        """Draw the ship at it's current location"""
        self.screen.blit(self.image,self.rect)