import pygame
from classes.Surfaces import paddle, pongBall, pongSurface

class GameState:
    def __init__(self, GameObj):

        self.gameObj = GameObj

        self.objList = []

        self.playerDict = {}

    def EventLoop(self):
        pass

class PlayingPong(GameState):
    
    def __init__(self, GameObj):

        super().__init__(GameObj)
        self.PlayerRight = paddle.playerRight()
        self.PlayerLeft  = paddle.playerLeft()
        self.Ball        = pongBall.PongBall()
        self.PongWindow  = pongSurface.PongSurface()

        self.objList = [
            self.PongWindow,
            self.PlayerRight,
            self.PlayerLeft,
            self.Ball,
            self.PlayerRight.scoreDisplay,
            self.PlayerLeft.scoreDisplay
        ]

        self.playerDict = {
            "PlayerRight" : self.PlayerRight,
            "PlayerLeft"  : self.PlayerLeft
        }

    def TrackMovementAndDraw(self):
        self.gameObj.window.window.fill(self.gameObj.window.background_color)
        for object in self.objList:
            object.updateCoordinates(600, 100)
            object.drawImage()
            self.gameObj.window.window.blit(object.surface, (object.coordX, object.coordY))
            object.fillSurface()

    def DetectCollision(self):
        for player in self.playerDict.values():
            if pygame.Rect.colliderect(player.getRect(), self.Ball.getRect()):
                self.Ball.speedX *= -1

    def DetectGoal(self):
        goalScored = False

        if self.Ball.coordX < -(self.Ball.diameter):
            goalScored = True
            player = self.playerDict["PlayerRight"]
            player.score += 1
            player.scoreDisplay.changeImage(player.score)

        elif self.Ball.coordX > self.gameObj.window.width:
            goalScored = True
            player = self.playerDict["PlayerLeft"]
            player.score += 1
            player.scoreDisplay.changeImage(player.score)

        if goalScored:
            self.Ball.coordX = self.Ball.startX
            self.Ball.coordY = self.Ball.startY
            self.Ball.speedX *= -1

    def DetectWin(self):
        hasWon = False
        for player in self.playerDict.values():
            if player.score == 9:
                win = True
                return hasWon, player
            
    def EventLoop(self):
        self.TrackMovementAndDraw()
        self.DetectCollision()
        self.DetectGoal()
        if self.DetectWin():
            print("won")
