import pygame

#Object for the "Ball" in a game of Pong

class PongBall:
    def __init__(self):
        # Determines how fast the ball is moving
        self.speedX = 2
        self.speedY = 2
        
        # Length and Width
        self.diameter = 5
        
        # Surface that holds the ball's image, gets drawn onto the game window surface
        self.surface = pygame.Surface((self.diameter, self.diameter))
        
        # Coordinate variables, left, right, top and bottom are for better readability in main code
        self.coordX = 800
        self.coordY = 600 
        self.left = self.coordX
        self.right = self.coordX + self.diameter
        self.top = self.coordY
        self.bottom = self.coordY + self.diameter
        
    # -------------------------------------------------------------------------------------------------------
    # Function: updateCoordinates
    # -------------------------------------------------------------------------------------------------------
    # Purpose: To update the coordinates of the ball based on speed setting and also to alter the speed
    #          settings based on the ball coordinates (if the ball hits the top or bottom of the screen)
    # Returns: Nothing
    # -------------------------------------------------------------------------------------------------------   
    def updateCoordinates(self, PONG_WINDOW_BOTTOM, PONG_WINDOW_TOP):
        # Modify coordinates based on speed setting, update directional variables
        self.coordX += self.speedX
        self.coordY += self.speedY
        
        self.left = self.coordX
        self.right = self.coordX + self.diameter
        self.top = self.coordY
        self.bottom = self.coordY + self.diameter
        
        if self.top < PONG_WINDOW_TOP or self.bottom > PONG_WINDOW_BOTTOM:
            self.speedY *= -1
            
    # -------------------------------------------------------------------------------------------------------
    # Function: fillSurface
    # -------------------------------------------------------------------------------------------------------
    # Purpose: To fill the ball's surface with color, creating an image.
    # Returns: Nothing
    # -------------------------------------------------------------------------------------------------------  
    def fillSurface(self):
        # Fill the surface, effectively "drawing"  the ball's image
        self.surface.fill((255, 255, 255))
    
    # -------------------------------------------------------------------------------------------------------
    # Function: getRect
    # -------------------------------------------------------------------------------------------------------
    # Purpose: To return a Rect object, essentially giving the coordinates of the objects surface for
    #          collision detection purposes.
    # Returns: pygame Rect object
    # -------------------------------------------------------------------------------------------------------  
    def getRect(self):
        # Returns the coordinates of the ball in a pygame rect object for collision detection purposes
        return pygame.Rect(self.coordX, self.coordY, self.diameter, self.diameter)
        