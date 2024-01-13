import pygame
from ..Base import gameSurface

class scoreSurface(gameSurface.GameSurface):
    def __init__(self):
        super().__init__()

        self.width = 20
        self.height = 30

        # When you load an image into pygame it's automatically created as a surface
        self.images = {
            "0" : pygame.image.load(r"C:\Users\trevo\REPOS\PyGame_Pong\sprites\zero.png" ),
            "1" : pygame.image.load(r"C:\Users\trevo\REPOS\PyGame_Pong\sprites\one.png"  ),
            "2" : pygame.image.load(r"C:\Users\trevo\REPOS\PyGame_Pong\sprites\two.png"  ),
            "3" : pygame.image.load(r"C:\Users\trevo\REPOS\PyGame_Pong\sprites\three.png"),
            "4" : pygame.image.load(r"C:\Users\trevo\REPOS\PyGame_Pong\sprites\four.png" ),
            "5" : pygame.image.load(r"C:\Users\trevo\REPOS\PyGame_Pong\sprites\five.png" ),
            "6" : pygame.image.load(r"C:\Users\trevo\REPOS\PyGame_Pong\sprites\six.png"  ),
            "7" : pygame.image.load(r"C:\Users\trevo\REPOS\PyGame_Pong\sprites\seven.png"),
            "8" : pygame.image.load(r"C:\Users\trevo\REPOS\PyGame_Pong\sprites\eight.png"),
            "9" : pygame.image.load(r"C:\Users\trevo\REPOS\PyGame_Pong\sprites\nine.png" )
        }
        
        self.surface = self.images["0"]

    def changeImage(self, number):
        if number < 10:
            self.surface = self.images[str(number)]

class playerLeftScoreDisplay(scoreSurface):
    def __init__(self):
        super().__init__()
        
        self.coordX = 100
        self.coordY = 35

class playerRightScoreDisplay(scoreSurface):
    def __init__(self):
        super().__init__()

        self.coordX = 700
        self.coordY = 35