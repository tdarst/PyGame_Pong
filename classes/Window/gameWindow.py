import pygame

# ===========================================================================================
# Name: GameWindow
# Purpose: Base class for the game window.
# ===========================================================================================
class GameWindow:
    def __init__(self):

        # Window dimensions
        self.width = 800
        self.height = 600

        # TODO: implement states (i.e. menu, game, etc.)
        self.state = None

        # Color settings for the window
        self.background_color_r = 0
        self.background_color_g = 0
        self.background_color_b = 0
        self.background_color = (self.background_color_r, 
                                 self.background_color_g,
                                 self.background_color_b)
        
        # Initialize display object with window dimensions
        self.window = pygame.display.set_mode((self.width, self.height))

        # Set display objects title
        self.caption = pygame.display.set_caption('Pygame Pong - Trevor Darst')

        # Fill window with color setting
        self.window.fill(self.background_color)

