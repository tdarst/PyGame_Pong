import pygame

# Inherited by all surfaces in the game.
class GameSurface:
    def __init__(self):
        super().__init__()
        
        # Surface's dimensions
        self.width = 0
        self.height = 0

        # Surface's coordinates
        self.coordX = 0
        self.coordY = 0

        # Surface object
        self.surface = pygame.Surface((self.width, self.height))

        # Color defining variables (default is black)
        self.color_r = 0
        self.color_g = 0
        self.color_b = 0
        self.color = (self.color_r,
                      self.color_g,
                      self.color_b)

        # Coordinate variables, left, right, top and bottom are for better readability
        self.left = self.coordX
        self.right = self.coordX + self.width
        self.top = self.coordY
        self.bottom = self.coordY + self.height

    # =======================================================================================================
    # Name: createSurface
    # Purpose: Creates the surface
    # =======================================================================================================
    def createSurface(self):
        self.surface = pygame.Surface((self.width, self.height))

    # =======================================================================================================
    # Name: updateCoordinates
    # Purpose: Updates the coordinate positions of surface each frame.
    # =======================================================================================================
    def updateCoordinates(self, PONG_WINDOW_BOTTOM=None, PONG_WINDOW_TOP=None):
        pass

    # =======================================================================================================
    # Name: fillSurface
    # Purpose: To fill the paddle's surface with color, creating an image.
    # =======================================================================================================
    def fillSurface(self):
        # Fill the surface, effectively "drawing"  the paddle's image
        self.surface.fill(self.color)
    
    # =======================================================================================================
    # Name: getRect
    # Purpose: To return a Rect object, essentially giving the coordinates of the objects surface for
    #          collision detection purposes.
    # =======================================================================================================
    def getRect(self):
        # Returns the coordinates of the paddle in a pygame rect object for collision detection purposes
        return pygame.Rect(self.coordX, self.coordY, self.width, self.height)