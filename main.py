import pygame, time, os
import paddle
from pongBall import PongBall
from gameWindow import GameWindow

# Color settings for the game window
PONG_WINDOW_COLOR = (255, 0, 0)

# Dimensions for the movement of the paddle and ball
PONG_WINDOW_TOP = 100
PONG_WINDOW_BOTTOM = 600
PONG_WINDOW_LEFT = 0
PONG_WINDOW_RIGHT = 800

# Initialize game window, add window title, color the background
GAME_WINDOW = GameWindow()

# -------------------------------------------------------------------------------------------------------
# Function: TrackMovementAndDraw
# -------------------------------------------------------------------------------------------------------
# Purpose: To draw over the game window's previous frame, update the coordinates of the paddles and ball,
#          draw the surfaces of the paddles and ball to the game window, and then fill in the image for
#          the paddle and ball surfaces.
# Returns: Nothing
# -------------------------------------------------------------------------------------------------------
def TrackMovementAndDraw(GameObjList):
    GAME_WINDOW.window.fill(GAME_WINDOW.background_color)
    for gameObj in GameObjList:
        gameObj.updateCoordinates(PONG_WINDOW_BOTTOM, PONG_WINDOW_TOP)
        GAME_WINDOW.window.blit(gameObj.surface, (gameObj.coordX, gameObj.coordY))
        gameObj.fillSurface()

# -------------------------------------------------------------------------------------------------------
# Function: DetectCollision
# -------------------------------------------------------------------------------------------------------
# Purpose: To detect whether the ball has collided with any of the paddles
# Returns: Nothing
# -------------------------------------------------------------------------------------------------------
def DetectCollision(Ball, PlayerDict):
    for player in PlayerDict.values():
        if pygame.Rect.colliderect(player.getRect(), Ball.getRect()):
            Ball.speedX *= -1

# -------------------------------------------------------------------------------------------------------
# Function: UpdateScore
# -------------------------------------------------------------------------------------------------------
# Purpose: To update a players score if they score a goal.
# Returns: Nothing
# -------------------------------------------------------------------------------------------------------
def UpdateScore(player):
    player.score += 1

# -------------------------------------------------------------------------------------------------------
# Function: DetectGoal
# -------------------------------------------------------------------------------------------------------
# Purpose: To check whether a goal has been scored or not.
# Returns: Boolean
# -------------------------------------------------------------------------------------------------------
def DetectGoal(Ball, playerDict):
    # If ball exits the left side of the window
    if Ball.coordX < -(Ball.diameter):
        UpdateScore(playerDict["PlayerRight"])
        return True
        
    # If ball exits the right side of the window
    elif Ball.coordX > GAME_WINDOW.width:
        UpdateScore(playerDict["PlayerLeft"])
        return True
        
    # If no goal has been scored  
    return False

# -------------------------------------------------------------------------------------------------------
# Function: DetectGoal
# -------------------------------------------------------------------------------------------------------
# Purpose: Initialize objects, run the game loop
# Returns: Nothing
# -------------------------------------------------------------------------------------------------------
def main():
    
    # Initialize objects for the two players and the ball
    PlayerRight = paddle.playerRight()
    PlayerLeft  = paddle.playerLeft()
    Ball        = PongBall()

    # Lists to hold different game objects for different iterational purposes
    GameObjList = [PlayerRight, PlayerLeft, Ball]
    PlayerDict = {"PlayerRight":PlayerRight, "PlayerLeft":PlayerLeft}

    clock = pygame.time.Clock()
    
    # Game loop boolean
    running = True
    
    # Game loop
    while running:

        clock.tick(60)
    
        # Update game object coordinates and draw them
        TrackMovementAndDraw(GameObjList)
        
        pygame.draw.line(GAME_WINDOW.window, PONG_WINDOW_COLOR, (PONG_WINDOW_LEFT, PONG_WINDOW_TOP), (PONG_WINDOW_RIGHT, PONG_WINDOW_TOP), width=5)
        # Detect ball and paddle collision
        DetectCollision(Ball, PlayerDict)
        
        # Detect whether a goal has happened, if so, reset ball
        if DetectGoal(Ball, PlayerDict):
            Ball.coordX = Ball.startX
            Ball.coordY = Ball.startY
            Ball.speedX = -(Ball.speedX)
            
        # Detect whether the user has pressed the exit button in window, if so, exit program
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT = "X" button in window
                running = False
        
        # Updates the full display surface to the screen
        pygame.display.flip()
        
if __name__ == "__main__":
    main()

