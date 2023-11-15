import pygame


''' FILE TO HOLD ALL OF THE GLOBAL VARIABLES AND CONTROLS '''

# Color settings for the game window
BACKGROUND_COLOR_R = 0
BACKGROUND_COLOR_G = 0
BACKGROUND_COLOR_B = 0
BACKGROUND_COLOR   = (BACKGROUND_COLOR_R, BACKGROUND_COLOR_G, BACKGROUND_COLOR_B)

# Game window caption
GAME_WINDOW_CAPTION = "Pygame Pong - Trevor Darst"

# Values for the speed of the paddles and ball
INITIAL_BALL_SPEED_X   = 1
INITIAL_BALL_SPEED_Y   = 1
INITIAL_PADDLE_SPEED_Y = 1

# Values for the keyboard controls for the paddles
PLAYER_RIGHT_CONTROL_UP   = pygame.K_UP   # Up arrow for directional keys
PLAYER_RIGHT_CONTROL_DOWN = pygame.K_DOWN # Down arrow for directional keys
PLAYER_LEFT_CONTROL_UP    = pygame.K_w    # W key on keyboard
PLAYER_LEFT_CONTROL_DOWN  = pygame.K_s    # S key on keyboard

# Dimensions for the game window
GAME_WINDOW_WIDTH  = 800
GAME_WINDOW_HEIGHT = 600

# Dimensions opon which the movement of the ball and paddle are bound
PONG_WINDOW_TOP    = 100
PONG_WINDOW_BOTTOM = 600
PONG_WINDOW_LEFT   = 0
PONG_WINDOW_RIGHT  = 800

PONG_WINDOW_COLOR = (100, 100, 0)