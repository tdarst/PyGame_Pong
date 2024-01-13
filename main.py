import pygame
from classes.Surfaces import paddle, pongBall, pongSurface
from classes.Window import gameWindow

# Initialize game window object
GAME_WINDOW = gameWindow.GameWindow()

# ======================================================================================================
# Name: TrackMovementAndDraw
# Purpose: Updates the coordinates of and draws all of the game objects in the order that they are given 
#          in the GameObjList via iteration.
# ======================================================================================================
def TrackMovementAndDraw(GameObjList):
    GAME_WINDOW.window.fill(GAME_WINDOW.background_color)
    for gameObj in GameObjList:
        # TODO: change this function to no longer need use of passed in coordinates of pong window.
        gameObj.updateCoordinates(600, 100)
        gameObj.drawImage()
        GAME_WINDOW.window.blit(gameObj.surface, (gameObj.coordX, gameObj.coordY))
        gameObj.fillSurface()

# ======================================================================================================
# Name: DetectCollision
# Purpose: To detect whether the ball has collided with any of the paddles
# ======================================================================================================
def DetectCollision(Ball, PlayerDict):
    for player in PlayerDict.values():
        if pygame.Rect.colliderect(player.getRect(), Ball.getRect()):
            Ball.speedX *= -1

# ======================================================================================================
# Name: DetectGoal
# Purpose: To check whether a goal has been scored or not.
# ======================================================================================================
def DetectGoal(Ball, playerDict):
    goalScored = False

    # If ball exits the left side of the window increment player right score
    # and update score displayed
    if Ball.coordX < -(Ball.diameter):
        goalScored = True
        player = playerDict["PlayerRight"]
        player.score += 1
        player.scoreDisplay.changeImage(player.score)
        
    # If ball exits the right side of the window increment player left score
    # and update score displayed
    elif Ball.coordX > GAME_WINDOW.width:
        goalScored = True
        player = playerDict["PlayerLeft"]
        player.score += 1
        player.scoreDisplay.changeImage(player.score)

    if goalScored:
        Ball.coordX = Ball.startX
        Ball.coordY = Ball.startY
        Ball.speedX *= -1

# ======================================================================================================
# Name: main
# Purpose: Initializes objects and variables and runs the game loop
# ======================================================================================================
def main():
    
    # Initialize objects for the two players and the ball
    PlayerRight      = paddle.playerRight()
    PlayerLeft       = paddle.playerLeft()
    Ball             = pongBall.PongBall()
    PongWindow       = pongSurface.PongSurface()

    # Lists to hold different game objects for different iterational purposes
    GameObjList = [PongWindow, PlayerRight, PlayerLeft, Ball, PlayerRight.scoreDisplay, PlayerLeft.scoreDisplay]
    PlayerDict  = {"PlayerRight":PlayerRight, "PlayerLeft":PlayerLeft}

    clock = pygame.time.Clock()
    
    # Game loop boolean
    running = True
    
    # Game loop
    while running:

        clock.tick(60)
    
        # Update game object coordinates and draw them
        TrackMovementAndDraw(GameObjList)
        
        # Detect ball and paddle collision
        DetectCollision(Ball, PlayerDict)
        
        # Detect whether a goal has happened, if so, reset ball
        DetectGoal(Ball, PlayerDict)
            
        # Detect whether the user has pressed the exit button in window, if so, exit program
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT = "X" button in window
                running = False
        
        # Updates the full display surface to the screen
        pygame.display.flip()
        
if __name__ == "__main__":
    main()

