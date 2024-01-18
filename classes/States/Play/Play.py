import pygame
from ...Base import gameState
from ...SharedSurfaces import PONG
from .Surfaces import paddle, pongBall, pongSurface

# =============================================================================
# Name: PlayingPong
# Purpose: State of the game where players are playing pong. Gets passed the
#          Game() object so it can reference the game window's attributes.
# =============================================================================
class PlayingPong(gameState.GameState):
    
    def __init__(self, GameObj):

        super().__init__(GameObj)

        # Instantiate all relevant objects
        self.player      = None
        self.PlayerRight = paddle.playerRight()
        self.PlayerLeft  = paddle.playerLeft()
        self.Ball        = pongBall.PongBall()
        self.PongWindow  = pongSurface.PongSurface()
        self.pong        = PONG.pongImage()

        self.dataToServer = {
            "PlayerRightX" : self.PlayerRight.coordX,
            "PlayerRightY" : self.PlayerRight.coordY,
            "PlayerRightScore" : self.PlayerRight.score,
            "PlayerLeftX" : self.PlayerLeft.coordX,
            "PlayerLeftY" : self.PlayerLeft.coordY,
            "PlayerLeftScore" : self.PlayerLeft.scoreDisplay,
            "BallX" : self.Ball.coordX,
            "BallY" : self.Ball.coordY,
            "PongWindowX" : self.PongWindow.coordX,
            "PongWindowY" : self.PongWindow.coordY,
            "PongX" : self.pong.coordX,
            "PongY" : self.pong.coordY
        }

        # Create list of relvant objects for iteration
        self.objList = [
            self.PongWindow,
            self.PlayerRight,
            self.PlayerLeft,
            self.Ball,
            self.pong
        ]

        # Create dictionary for players for better readability
        # when used in function
        self.playerDict = {
            "PlayerRight" : self.PlayerRight,
            "PlayerLeft"  : self.PlayerLeft
        }

    # ======================================================================================================
    # Name: TrackMovementAndDraw
    # Purpose: Updates the coordinates of and draws all of the game objects in the order that they are given 
    #          in the GameObjList via iteration.
    # ======================================================================================================
    def TrackMovementAndDraw(self):
        self.gameObj.window.window.fill(self.gameObj.window.background_color)
        for object in self.objList:
            object.updateCoordinates(600, 100)
            object.drawImage()
            self.gameObj.window.window.blit(object.surface, (object.coordX, object.coordY))
            object.fillSurface()

    # ======================================================================================================
    # Name: DetectCollision
    # Purpose: To detect whether the ball has collided with any of the paddles
    # ======================================================================================================
    def DetectCollision(self):
        for player in self.playerDict.values():
            if pygame.Rect.colliderect(player.getRect(), self.Ball.getRect()):
                self.Ball.speedX *= -1

    # ======================================================================================================
    # Name: DetectGoal
    # Purpose: To check whether a goal has been scored or not.
    # ======================================================================================================
    def DetectGoal(self):
        goalScored = False

        if self.Ball.coordX < -(self.Ball.diameter):
            goalScored = True
            player = self.playerDict["PlayerRight"]
            player.score += 1
            player.scoreDisplay.updateSprite(player.score)

        elif self.Ball.coordX > self.gameObj.window.width:
            goalScored = True
            player = self.playerDict["PlayerLeft"]
            player.score += 1
            player.scoreDisplay.updateSprite(player.score)

        if goalScored:
            self.Ball.coordX = self.Ball.startX
            self.Ball.coordY = self.Ball.startY
            self.Ball.speedX *= -1

    # ======================================================================================================
    # Name: DetectWin
    # Purpose: To check whether a player has won or not.
    # ======================================================================================================
    def DetectWin(self):
        hasWon = False
        for player in self.playerDict.values():
            if player.score == 9:
                win = True
                return hasWon, player
            
    def updateDataToServer(self):
        self.dataToServer = {
            "PlayerRightX" : self.PlayerRight.coordX,
            "PlayerRightY" : self.PlayerRight.coordY,
            "PlayerRightScore" : self.PlayerRight.score,
            "PlayerLeftX" : self.PlayerLeft.coordX,
            "PlayerLeftY" : self.PlayerLeft.coordY,
            "PlayerLeftScore" : self.PlayerLeft.scoreDisplay,
            "BallX" : self.Ball.coordX,
            "BallY" : self.Ball.coordY,
            "PongWindowX" : self.PongWindow.coordX,
            "PongWindowY" : self.PongWindow.coordY,
            "PongX" : self.pong.coordX,
            "PongY" : self.pong.coordY
        }
            
    # ======================================================================================================
    # Name: runEvents
    # Purpose: Run's the games events
    # ======================================================================================================            
    def runEvents(self):
        self.TrackMovementAndDraw()
        self.DetectCollision()
        self.DetectGoal()
        if self.DetectWin():
            print("won")