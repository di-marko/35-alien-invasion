import pygame

class Aliens:
    def __init__(self, ai_game):
        self.screen = ai_game.screen
        self.screen_rect = ai_game.screen.get_rect()

        self.image = pygame.image.load("images/alien_1.gif")
        self.rect = self.image.get_rect()

        self.rect.midtop = self.screen_rect.midtop

    def blitme(self):
        self.screen.blit(self.image, self.rect)