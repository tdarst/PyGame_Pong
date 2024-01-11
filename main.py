import pygame, time, os
from paddle import Paddle
from pongBall import PongBall

# Color settings for the game window
PONG_WINDOW_COLOR = (255, 0, 0)
BACKGROUND_COLOR_R = 0
BACKGROUND_COLOR_G = 0
BACKGROUND_COLOR_B = 0
BACKGROUND_COLOR = (BACKGROUND_COLOR_R, BACKGROUND_COLOR_G, BACKGROUND_COLOR_B)

# Values for the speed of the paddles and ball
INITIAL_BALL_SPEED_X   = 2
INITIAL_BALL_SPEED_Y   = 2
INITIAL_PADDLE_SPEED_Y = 4

# Values for the keyboard controls for the paddles
PLAYER_RIGHT_CONTROL_UP   = pygame.K_UP   # Up arrow for directional keys
PLAYER_RIGHT_CONTROL_DOWN = pygame.K_DOWN # Down arrow for directional keys
PLAYER_LEFT_CONTROL_UP    = pygame.K_w    # W key on keyboard
PLAYER_LEFT_CONTROL_DOWN  = pygame.K_s    # S key on keyboard

# Dimensions for the game window
GAME_WINDOW_WIDTH  = 800
GAME_WINDOW_HEIGHT = 600

# Dimensions for the movement of the paddle and ball
PONG_WINDOW_TOP = 100
PONG_WINDOW_BOTTOM = 600
PONG_WINDOW_LEFT = 0
PONG_WINDOW_RIGHT = 800

# Initialize game window, add window title, color the background
GAME_WINDOW = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
pygame.display.set_caption('Pygame Pong - Trevor Darst')
GAME_WINDOW.fill(BACKGROUND_COLOR)

# -------------------------------------------------------------------------------------------------------
# Function: TrackMovementAndDraw()
# -------------------------------------------------------------------------------------------------------
# Purpose: To draw over the game window's previous frame, update the coordinates of the paddles and ball,
#          draw the surfaces of the paddles and ball to the game window, and then fill in the image for
#          the paddle and ball surfaces.
# Returns: Nothing
# -------------------------------------------------------------------------------------------------------
def TrackMovementAndDraw(GameObjList):
    GAME_WINDOW.fill(BACKGROUND_COLOR)
    for gameObj in GameObjList:
        gameObj.updateCoordinates(PONG_WINDOW_BOTTOM, PONG_WINDOW_TOP)
        GAME_WINDOW.blit(gameObj.surface, (gameObj.coordX, gameObj.coordY))
        gameObj.fillSurface()

# -------------------------------------------------------------------------------------------------------
# Function: DetectCollision()
# -------------------------------------------------------------------------------------------------------
# Purpose: To detect whether the ball has collided with any of the paddles
# Returns: Nothing
# -------------------------------------------------------------------------------------------------------
def DetectCollision(Ball, PlayerDict):
    for player in PlayerDict.values():
        if pygame.Rect.colliderect(player.getRect(), Ball.getRect()):
            Ball.speedX *= -1

# -------------------------------------------------------------------------------------------------------
# Function: UpdateScore()
# -------------------------------------------------------------------------------------------------------
# Purpose: To update a players score if they score a goal.
# Returns: Nothing
# -------------------------------------------------------------------------------------------------------
def UpdateScore(player):
    player.score += 1

# -------------------------------------------------------------------------------------------------------
# Function: DetectGoal()
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
    elif Ball.coordX > GAME_WINDOW_WIDTH:
        UpdateScore(playerDict["PlayerLeft"])
        return True
        
    # If no goal has been scored  
    return False

# -------------------------------------------------------------------------------------------------------
# Function: DetectGoal()
# -------------------------------------------------------------------------------------------------------
# Purpose: Initialize objects, run the game loop
# Returns: Nothing
# -------------------------------------------------------------------------------------------------------
def main():
    
    # Initialize objects for the two players and the ball
    PlayerRight = Paddle(795, 325, INITIAL_PADDLE_SPEED_Y, PLAYER_RIGHT_CONTROL_UP, PLAYER_RIGHT_CONTROL_DOWN)
    PlayerLeft  = Paddle(0, 100, INITIAL_PADDLE_SPEED_Y, PLAYER_LEFT_CONTROL_UP, PLAYER_LEFT_CONTROL_DOWN)
    Ball        = PongBall(GAME_WINDOW_WIDTH/2, PONG_WINDOW_TOP, INITIAL_BALL_SPEED_X, INITIAL_BALL_SPEED_Y)

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
        
        pygame.draw.line(GAME_WINDOW, PONG_WINDOW_COLOR, (PONG_WINDOW_LEFT, PONG_WINDOW_TOP), (PONG_WINDOW_RIGHT, PONG_WINDOW_TOP), width=5)
        # Detect ball and paddle collision
        DetectCollision(Ball, PlayerDict)
        
        # Detect whether a goal has happened, if so, reset ball
        if DetectGoal(Ball, PlayerDict):
            Ball.coordX = GAME_WINDOW_WIDTH/2
            Ball.coordY = PONG_WINDOW_TOP
            Ball.speedY = INITIAL_BALL_SPEED_Y
            Ball.speedX = -(INITIAL_BALL_SPEED_X)
            
        # Detect whether the user has pressed the exit button in window, if so, exit program
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT = "X" button in window
                running = False
        
        # Updates the full display surface to the screen
        pygame.display.flip()
        
if __name__ == "__main__":
    main()

