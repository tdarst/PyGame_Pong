import pygame
from classes.Surfaces import paddle, pongBall, pongSurface

# =============================================================================
# Name: GameState
# Purpose: Inherited by all states of the program (menu, playing game, etc.)
# =============================================================================
class GameState:
    def __init__(self, GameObj):

        # Gives the game object to the game state so it can reference the window
        self.gameObj = GameObj

        # List of relevant objects to be drawn in each state
        self.objList = []

    # ======================================================================================================
    # Name: runEvents
    # Purpose: Run's the games events
    # ======================================================================================================       
    def runEvents(self):
        pass

# =============================================================================
# Name: PlayingPong
# Purpose: State of the game where players are playing pong. Gets passed the
#          Game() object so it can reference the game window's attributes.
# =============================================================================
class PlayingPong(GameState):
    
    def __init__(self, GameObj):

        super().__init__(GameObj)

        # Instantiate all relevant objects
        self.PlayerRight = paddle.playerRight()
        self.PlayerLeft  = paddle.playerLeft()
        self.Ball        = pongBall.PongBall()
        self.PongWindow  = pongSurface.PongSurface()

        # Create list of relvant objects for iteration
        self.objList = [
            self.PongWindow,
            self.PlayerRight,
            self.PlayerLeft,
            self.Ball,
            self.PlayerRight.scoreDisplay,
            self.PlayerLeft.scoreDisplay
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
