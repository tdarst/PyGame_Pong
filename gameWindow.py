import pygame

class GameWindow:
    def __init__(self):
        super().__init__
        self.width = 800
        self.height = 600

        self.background_color_r = 0
        self.background_color_g = 0
        self.background_color_b = 0
        self.background_color = (self.background_color_r, 
                                 self.background_color_g,
                                 self.background_color_b)
        
        self.window = pygame.display.set_mode((self.width, self.height))

        self.caption = pygame.display.set_caption('Pygame Pong - Trevor Darst')

        self.window.fill(self.background_color)

class PongSurface:
    def __init__(self):
        self.width = 800
        self.height = 500

        self.color_r = 255
        self.color_g = 0
        self.color_b = 0
        self.color = (self.color_r,
                      self.color_g,
                      self.color_b)

        self.coordX = 0
        self.coordY = 100
        self.surface = pygame.Surface((self.width, self.height))

    def updateCoordinates(self, a, b):
        pass

    def fillSurface(self):
        self.surface.fill(self.color)

