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

        self.gameObj = GameObj

        self.assignedPlayerNum = int(self.gameObj.assignedPlayerNum)
        self.assignedPlayer = None
        self.opponent = None

        self.PlayerRight = paddle.playerRight()
        self.PlayerLeft  = paddle.playerLeft()
        self.Ball        = pongBall.PongBall()
        self.PongWindow  = pongSurface.PongSurface()
        self.pong        = PONG.pongImage()

        self.determinePlayer()
        self.setLocalControls()

        self.dataOut = f"{self.assignedPlayerNum}:{self.assignedPlayer.coordX},{self.assignedPlayer.coordY}"
        self.dataIn = None

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
            if object is self.assignedPlayer:
                self.updateLocalPlayerData(object)
            elif object is self.opponent:
                self.updateOpponentData(object)
            else:
                object.updateCoordinates(600,100)
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

    # TODO: ADD DOCUMENTATION
    def determinePlayer(self):
        if self.assignedPlayerNum == 0:
            self.assignedPlayer = self.PlayerLeft
            self.opponent = self.PlayerRight

        elif self.assignedPlayerNum == 1:
            self.assignedPlayer = self.PlayerRight
            self.opponent = self.PlayerLeft

    # TODO: ADD DOCUMENTATION
    def setLocalControls(self):
        self.assignedPlayer.upKey = pygame.K_UP
        self.assignedPlayer.downKey = pygame.K_DOWN

    # TODO: ADD DOCUMENTATION   
    def updateData(self):
        self.dataOut = f"{self.assignedPlayerNum}:{self.assignedPlayer.coordX},{self.assignedPlayer.coordY}"

    # TODO: ADD DOCUMENTATION
    def parseData(self, data):

        data = data.split(":")[1].split(",")
        print(data)
        return int(data[0]), int(data[1])
    
    # TODO: ADD DOCUMENTATION
    def sendData(self):
        reply = self.gameObj.network.send(self.dataOut)
        return reply
    
    def updateOpponentData(self, object):
        opponentCoords = self.parseData(self.sendData())
        if opponentCoords:
            object.coordX = opponentCoords[0]
            object.coordY = opponentCoords[1]
            object.updateCoordinates(600,100)

    def updateLocalPlayerData(self, object):
        object.updateCoordinates(600, 100)
        self.updateData()


    # ======================================================================================================
    # Name: runEvents
    # Purpose: Run's the games events
    # ======================================================================================================            
    def runEvents(self):
        self.TrackMovementAndDraw()
        self.DetectCollision()