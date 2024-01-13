import pygame
from ..Base import gameSurface

# ===================================================================================
# Name: PongSurface
# Purpose: Class for the "field" on which the pong game is played.
# ===================================================================================
class PongSurface(gameSurface.GameSurface):
    def __init__(self):
        super().__init__()
        
        # Height and width of the "field"
        self.width = 800
        self.height = 500

        # Color settings
        self.color_r = 0
        self.color_g = 0
        self.color_b = 255
        self.color = (self.color_r,
                      self.color_g,
                      self.color_b)

        # Draw location of the upper left hand corner.
        self.coordX = 0
        self.coordY = 100

        # Create the surface
        self.createSurface()

    # ===================================================================================
    # Name: fillSurface
    # Purpose: Fill the surface of the "field" with color setting.
    # ===================================================================================
    def fillSurface(self):
        self.surface.fill(self.color)