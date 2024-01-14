import pygame
from ....Base import gameSurface
from . import scoreSurface

# ===========================================================================================
# Name: Paddle
# Purpose: Class for creating surfaces to hold the paddles of both players. Gets inherited
#          by both player's respective paddle classes.
# ===========================================================================================
class Paddle(gameSurface.GameSurface):
    def __init__(self):
        super().__init__()

        # Determines how fast the paddle is moving       
        self.speedY = 5

        # Paddle controls
        self.upKey = None
        self.downKey = None
        
        # Paddle dimensions
        self.height = 60
        self.width  = 5

        # Color settings
        self.color_r = 255
        self.color_g = 255
        self.color_b = 255
        self.color = (self.color_r,
                      self.color_g,
                      self.color_b)
        
        # Surface that holds the paddle's image, gets drawn onto the game window surface
        self.createSurface()
        
        # Player score
        self.score = 0

    # =======================================================================================================
    # Name: updateCoordinates
    # Purpose: Updates the coordinate positions of surface each frame.
    # =======================================================================================================
    def updateCoordinates(self, PONG_WINDOW_BOTTOM, PONG_WINDOW_TOP):
        key = pygame.key.get_pressed()

        # If key is up-key, go up.
        if key[self.upKey]:
            if self.top != PONG_WINDOW_TOP:
                self.coordY -= self.speedY
        
        # If key is down-key, go down.
        if key[self.downKey]:
            if self.bottom != PONG_WINDOW_BOTTOM:
                self.coordY += self.speedY
        
        # Coordinate variables, left, right, top and bottom are for better readability
        self.left = self.coordX
        self.right = self.coordX + self.width
        self.top = self.coordY
        self.bottom = self.coordY + self.height

    # =============================================================
    # Name: fillSurface
    # Purpose: Fills paddle with color setting
    # =============================================================
    def fillSurface(self):
        self.surface.fill(self.color)

# ===========================================================================================
# Name: playerLeft
# Purpose: Class for left player's paddle
# ===========================================================================================
class playerLeft(Paddle):
    def __init__(self):
        super().__init__()

        # Sets player left's initial coordinates
        self.coordX = 0
        self.coordY = 290

        # Sets controls
        self.upKey = pygame.K_w
        self.downKey = pygame.K_s

        # Initializes player left's score display object
        self.scoreDisplay = scoreSurface.playerLeftScoreDisplay()

# ===========================================================================================
# Name: playerRight
# Purpose: Class for right player's paddle
# ===========================================================================================
class playerRight(Paddle):
    def __init__(self):
        super().__init__()

        # Sets player right's initial coordinates
        self.coordX = 795
        self.coordY = 290

        # Sets controls
        self.upKey = pygame.K_UP
        self.downKey = pygame.K_DOWN

        # Initializes player right's score display object
        self.scoreDisplay = scoreSurface.playerRightScoreDisplay()
