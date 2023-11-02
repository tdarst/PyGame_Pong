import pygame, os

# Object for the "Paddle" in a game of Pong

class Paddle:
    def __init__(self, InitLocationX, InitLocationY, SpeedY, UpKey, DownKey):
        # Determines how fast the paddle is moving       
        self.speedY = SpeedY
        
        # Paddle dimensions
        self.length = 60
        self.width  = 5
        
        # Surface that holds the paddle's image, gets drawn onto the game window surface
        self.surface = pygame.Surface((self.width, self.length))
        
        # Paddle keyboarad controls
        self.upKey = UpKey
        self.downKey = DownKey
        
        # Player score
        self.score = 0
        
        # Coordinate variables, left, right, top and bottom are for better readability in main code
        self.coordX = InitLocationX
        self.coordY = InitLocationY        
        self.left = self.coordX
        self.right = self.coordX + self.width
        self.top = self.coordY
        self.bottom = self.coordY + self.length
    
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
        self.bottom = self.coordY + self.length
    
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
        return pygame.Rect(self.coordX, self.coordY, self.width, self.length)