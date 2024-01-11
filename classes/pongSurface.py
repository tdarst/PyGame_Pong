import pygame
from . import gameSurface

class PongSurface(gameSurface.GameSurface):
    def __init__(self):
        super().__init__()
        
        self.width = 800
        self.height = 500

        self.color_r = 0
        self.color_g = 0
        self.color_b = 255
        self.color = (self.color_r,
                      self.color_g,
                      self.color_b)

        self.coordX = 0
        self.coordY = 100
        self.surface = pygame.Surface((self.width, self.height))