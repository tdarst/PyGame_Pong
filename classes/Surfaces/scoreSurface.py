import pygame
from ..Base import gameSurface

class scoreSurface(gameSurface.GameSurface):
    def __init__(self):
        super().__init__()

        self.width = 30
        self.length = 20

        self.image = None

    def changeImage(self, number):
        self.image = number

class playerLeftScoreDisplay(scoreSurface):
    def __init__(self):
        super().__init__()
        
        self.coordX = 100
        self.coordY = 35

        self.image = None

class playerRightScoreDisplay(scoreSurface):
    def __init__(self):
        super().__init__()

        self.coordX = 700
        self.coordY = 35

        self.image = None