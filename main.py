import pygame, time, os
from PongProperties import *
from paddle import Paddle
from pongBall import PongBall

# Initialize game window, set caption, and fill the background
GAME_WINDOW = pygame.display.set_mode((GAME_WINDOW_WIDTH, GAME_WINDOW_HEIGHT))
pygame.display.set_caption(GAME_WINDOW_CAPTION)
GAME_WINDOW.fill(BACKGROUND_COLOR)

clock = pygame.time.Clock()

# -------------------------------------------------------------------------------------------------------
# Function: TrackMovementAndDraw()
# -------------------------------------------------------------------------------------------------------
# Purpose: To draw over the game window's previous frame, update the coordinates of the paddles and ball,
#          draw the surfaces of the paddles and ball to the game window, and then fill in the image for
#          the paddle and ball surfaces.
# Returns: Nothing
# -------------------------------------------------------------------------------------------------------
def TrackMovementAndDraw(game_obj_list, dt):
    GAME_WINDOW.fill(BACKGROUND_COLOR)
    for game_obj in game_obj_list:
        game_obj.updateCoordinates(PONG_WINDOW_BOTTOM, PONG_WINDOW_TOP, dt)
        GAME_WINDOW.blit(game_obj.surface, (game_obj.coordX, game_obj.coordY))
        game_obj.fillSurface()

# -------------------------------------------------------------------------------------------------------
# Function: DetectCollision()
# -------------------------------------------------------------------------------------------------------
# Purpose: To detect whether the ball has collided with any of the paddles
# Returns: Nothing
# -------------------------------------------------------------------------------------------------------
def DetectCollision(ball, player_dict):
    for player in player_dict.values():
        if pygame.Rect.colliderect(player.getRect(), ball.getRect()):
            ball.speedX *= -1

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
def DetectGoal(ball, player_dict):
    # If ball exits the left side of the window
    if ball.coordX < -(ball.diameter):
        UpdateScore(player_dict["PlayerRight"])
        return True
        
    # If ball exits the right side of the window
    elif ball.coordX > GAME_WINDOW_WIDTH:
        UpdateScore(player_dict["PlayerLeft"])
        return True
        
    # If no goal has been scored  
    return False

# -------------------------------------------------------------------------------------------------------
# Function: main()
# -------------------------------------------------------------------------------------------------------
# Purpose: Initialize objects, run the game loop
# Returns: Nothing
# -------------------------------------------------------------------------------------------------------
def main():
    # Initialize objects for the two players and the ball
    player_right = Paddle(795, 325, INITIAL_PADDLE_SPEED_Y, PLAYER_RIGHT_CONTROL_UP, PLAYER_RIGHT_CONTROL_DOWN)
    player_left  = Paddle(0, 100, INITIAL_PADDLE_SPEED_Y, PLAYER_LEFT_CONTROL_UP, PLAYER_LEFT_CONTROL_DOWN)
    ball         = PongBall(GAME_WINDOW_WIDTH/2, PONG_WINDOW_TOP, INITIAL_BALL_SPEED_X, INITIAL_BALL_SPEED_Y)

    # Lists to hold different game objects for different iterational purposes
    game_obj_list = [player_right, player_left, ball]
    player_dict = {"PlayerRight":player_right, "PlayerLeft":player_left}

    # Game loop condition
    running = True
    integer = 0
    
    # Game loop
    while running:

        # Get current framerate
        framerate = clock.tick(60)

        # Updates the full display surface to the screen
        pygame.display.flip()

        # Update game object coordinates and draw them
        TrackMovementAndDraw(game_obj_list, framerate)
        
        # Draw line indicating the top of the window in which game objects can move
        pygame.draw.line(GAME_WINDOW, PONG_WINDOW_COLOR, (PONG_WINDOW_LEFT, PONG_WINDOW_TOP), (PONG_WINDOW_RIGHT, PONG_WINDOW_TOP), width=5)
        
        # Detect ball and paddle collision
        DetectCollision(ball, player_dict)
        
        # Detect whether a goal has happened, if so, reset ball, and change it's direction
        if DetectGoal(ball, player_dict):
            ball.coordX = GAME_WINDOW_WIDTH/2
            ball.coordY = PONG_WINDOW_TOP
            ball.speedY = INITIAL_BALL_SPEED_Y
            ball.speedX *= -1 
            
        # Detect whether the user has pressed the exit button in window, if so, exit program
        for event in pygame.event.get():
            if event.type == pygame.QUIT: # pygame.QUIT = "X" button in window upper right
                running = False
  
if __name__ == "__main__":
    main()

