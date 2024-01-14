import pygame
from ..Base import gameSurface

class pongImage(gameSurface.GameSurface):
    def __init__(self):
        super().__init__()

        self.coordX = 252
        self.coordY = 8

        self.surface = pygame.image.load(r"sprites\PONG.png")

        