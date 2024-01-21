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
    
    def __init__(self, GameObj: object):
        
        # Initialize game object, start network
        self.gameObj = GameObj

        # Get player assignment from server
        self.assignedPlayerNum = int(self.gameObj.assignedPlayerNum)
        self.assignedPlayer = None
        self.opponent = None

        # Insantiate game objects
        self.PlayerRight = paddle.playerRight()
        self.PlayerLeft  = paddle.playerLeft()
        self.Ball        = pongBall.PongBall()
        self.PongWindow  = pongSurface.PongSurface()
        self.pong        = PONG.pongImage()

        # Set player assignment based on server data
        self.determinePlayer()

        # Assign which player object you're controlling.
        self.setLocalControls()

        # Variable to hold data to be sent to server
        self.dataOut = f"{self.assignedPlayerNum}:{self.assignedPlayer.coordX},{self.assignedPlayer.coordY}"

        # Create list of game objects for iteration
        self.objList = [
            self.PongWindow,
            self.PlayerRight,
            self.PlayerLeft,
            self.Ball,
            self.pong
        ]

        # Create dictionary for players for better readability
        self.playerDict = {
            "PlayerRight" : self.PlayerRight,
            "PlayerLeft"  : self.PlayerLeft
        }

    # ======================================================================================================
    # Name: TrackMovementAndDraw
    # Purpose: Updates the coordinates of and draws all of the game objects in the order that they are given 
    #          in the GameObjList via iteration.
    # ======================================================================================================
    def TrackMovementAndDraw(self) -> None:
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
    def DetectCollision(self) -> None:
        for player in self.playerDict.values():
            if pygame.Rect.colliderect(player.getRect(), self.Ball.getRect()):
                self.Ball.speedX *= -1

    # ======================================================================================================
    # Name: DetectGoal
    # Purpose: To check whether a goal has been scored or not.
    # ======================================================================================================
    def DetectGoal(self) -> None:
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
    def DetectWin(self) -> tuple:
        hasWon = False
        for player in self.playerDict.values():
            if player.score == 9:
                win = True
                return hasWon, player

    # ======================================================================================================
    # Name: determinePlayer
    # Purpose: Assigns which player local user will be playing as.
    # ======================================================================================================
    def determinePlayer(self) -> None:
        if self.assignedPlayerNum == 0:
            self.assignedPlayer = self.PlayerLeft
            self.opponent = self.PlayerRight

        elif self.assignedPlayerNum == 1:
            self.assignedPlayer = self.PlayerRight
            self.opponent = self.PlayerLeft

    # ======================================================================================================
    # Name: setLocalControls
    # Purpose: Sets user controls to the locally controlled player object.
    # ======================================================================================================
    def setLocalControls(self) -> None:
        self.assignedPlayer.upKey = pygame.K_UP
        self.assignedPlayer.downKey = pygame.K_DOWN

    # ======================================================================================================
    # Name: updateData
    # Purpose: Updates the bariable that holds player number and player coordinates
    # ====================================================================================================== 
    def updateData(self) -> None:
        self.dataOut = f"{self.assignedPlayerNum}:{self.assignedPlayer.coordX},{self.assignedPlayer.coordY}"

    # ======================================================================================================
    # Name: parseData
    # Purpose: Parses the data received by the server
    # ====================================================================================================== 
    def parseData(self, data: str) -> tuple:
        data = data.split(":")[1].split(",")
        return int(data[0]), int(data[1])
    
    # ======================================================================================================
    # Name: sendData
    # Purpose: Sends the local player data to the server, returns opponent data
    # ====================================================================================================== 
    def sendData(self) -> str:
        reply = self.gameObj.network.send(self.dataOut)
        return reply

    # ======================================================================================================
    # Name: updateOpponentData
    # Purpose: Sends the local player data to the server, 
    # ====================================================================================================== 
    def updateOpponentData(self, object: object) -> None:
        opponentCoords = self.parseData(self.sendData())
        if opponentCoords:
            object.coordX = opponentCoords[0]
            object.coordY = opponentCoords[1]
            object.updateCoordinates(600,100)

    def updateLocalPlayerData(self, object: object) -> None:
        object.updateCoordinates(600, 100)
        self.updateData()


    # ======================================================================================================
    # Name: runEvents
    # Purpose: Run's the games events
    # ======================================================================================================            
    def runEvents(self) -> None:
        self.TrackMovementAndDraw()
        self.DetectCollision()
        self.DetectGoal()