import pygame
from ..Base import gameSurface

# ===========================================================================================
# Name: scoreSurface
# Purpose: Class for creating surfaces to hold the scores of players. Gets inherited
#          by both player's respective score display classes.
# ===========================================================================================
class scoreSurface(gameSurface.GameSurface):
    def __init__(self):
        super().__init__()

        # Width and height match the sprite images
        self.width = 20
        self.height = 30

        # Images for numbers 0-9
        self.images = {
            "0" : pygame.image.load(r"sprites\zero.png"),
            "1" : pygame.image.load(r"sprites\one.png"  ),
            "2" : pygame.image.load(r"sprites\two.png"  ),
            "3" : pygame.image.load(r"sprites\three.png"),
            "4" : pygame.image.load(r"sprites\four.png" ),
            "5" : pygame.image.load(r"sprites\five.png" ),
            "6" : pygame.image.load(r"sprites\six.png"  ),
            "7" : pygame.image.load(r"sprites\seven.png"),
            "8" : pygame.image.load(r"sprites\eight.png"),
            "9" : pygame.image.load(r"sprites\nine.png" )
        }
        
        # When you load an image with pygame.image.load it's loaded as a
        # surface, so we can just modify the surface straight from the
        # images dictionary.
        self.surface = self.images["0"]

    # ==========================================================================
    # Name: changeImage
    # Purpose: Updates the image to reflect the player's score
    # ==========================================================================
    def changeImage(self, number):
        if number < 10:
            self.surface = self.images[str(number)]

# ==========================================================================
# Name: playerLeftScoreDisplay
# Purpose: Class for the left player's score
# ==========================================================================
class playerLeftScoreDisplay(scoreSurface):
    def __init__(self):
        super().__init__()
        
        # Change coordinates to left side of screen
        self.coordX = 100
        self.coordY = 35

# ==========================================================================
# Name: playerRightScoreDisplay
# Purpose: Class for the right player's score
# ==========================================================================
class playerRightScoreDisplay(scoreSurface):
    def __init__(self):
        super().__init__()

        # Change coordinates to right side of screen
        self.coordX = 700
        self.coordY = 35