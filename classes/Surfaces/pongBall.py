import pygame
from ..Base import gameSurface

#Object for the "Ball" in a game of Pong
class PongBall(gameSurface.GameSurface):
    def __init__(self):
        super().__init__()
        # Determines how fast the ball is moving
        self.speedX = 2
        self.speedY = 2
        
        # Length and Width
        self.width = 5
        self.height = 5

        self.diameter = self.width

        self.color_r = 255
        self.color_g = 255
        self.color_b = 255
        self.color = (self.color_r,
                      self.color_g,
                      self.color_b)
        
        # Surface that holds the ball's image, gets drawn onto the game window surface
        self.createSurface()
        
        self.startX = 400
        self.startY = 300

        # Coordinate variables, left, right, top and bottom are for better readability in main code
        self.coordX = self.startX
        self.coordY = self.startY 
        
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

    def fillSurface(self):
        self.surface.fill(self.color)