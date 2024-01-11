import pygame, os

# Object for the "Paddle" in a game of Pong

class Paddle:
    def __init__(self):
        # Determines how fast the paddle is moving       
        self.speedY = 5

        self.coordX = 0
        self.coordY = 0

        self.upKey = None
        self.downKey = None
        
        # Paddle dimensions
        self.height = 60
        self.width  = 5
        
        # Surface that holds the paddle's image, gets drawn onto the game window surface
        self.surface = pygame.Surface((self.width, self.height))
        
        # Player score
        self.score = 0
        
        # Coordinate variables, left, right, top and bottom are for better readability in main code
        self.left = self.coordX
        self.right = self.coordX + self.width
        self.top = self.coordY
        self.bottom = self.coordY + self.height
    
    # -------------------------------------------------------------------------------------------------------
    # Function: updateCoordinates()
    # -------------------------------------------------------------------------------------------------------
    # Purpose: To update the coordinates of the paddle based on speed setting if the paddle isn't touching
    #          the top or bottom of the screen.
    # Returns: Nothing
    # -------------------------------------------------------------------------------------------------------   
    def updateCoordinates(self, PONG_WINDOW_BOTTOM, PONG_WINDOW_TOP):
        key = pygame.key.get_pressed()
        if key[self.upKey]:
            if self.top != PONG_WINDOW_TOP:
                self.coordY -= self.speedY
            
        if key[self.downKey]:
            if self.bottom != PONG_WINDOW_BOTTOM:
                self.coordY += self.speedY
                
        self.left = self.coordX
        self.right = self.coordX + self.width
        self.top = self.coordY
        self.bottom = self.coordY + self.height
    
    # -------------------------------------------------------------------------------------------------------
    # Function: fillSurface()
    # -------------------------------------------------------------------------------------------------------
    # Purpose: To fill the paddle's surface with color, creating an image.
    # Returns: Nothing
    # -------------------------------------------------------------------------------------------------------      
    def fillSurface(self):
        # Fill the surface, effectively "drawing"  the paddle's image
        self.surface.fill((255, 255, 255))
    
    # -------------------------------------------------------------------------------------------------------
    # Function: getRect()
    # -------------------------------------------------------------------------------------------------------
    # Purpose: To return a Rect object, essentially giving the coordinates of the objects surface for
    #          collision detection purposes.
    # Returns: pygame Rect object
    # ------------------------------------------------------------------------------------------------------- 
    def getRect(self):
        # Returns the coordinates of the paddle in a pygame rect object for collision detection purposes
        return pygame.Rect(self.coordX, self.coordY, self.width, self.height)


class playerLeft(Paddle):
    def __init__(self):
        super().__init__()
        self.coordX = 0
        self.coordY = 10
        self.upKey = pygame.K_w
        self.downKey = pygame.K_s

class playerRight(Paddle):
    def __init__(self):
        super().__init__()
        self.coordX = 0
        self.coordY = 100
        self.coordX = 795
        self.coordY = 325
        self.upKey = pygame.K_UP
        self.downKey = pygame.K_DOWN
