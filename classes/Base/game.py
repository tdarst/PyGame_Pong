import pygame
from classes.Window import gameWindow
from ..States.Play import Play
import network

# =============================================================================
# Name: Game
# Purpose: Object to hold the states, window, and run the game loop
# =============================================================================
class Game:
    def __init__(self):
        
        self.network = network.Network()

        self.assignedPlayerNum = self.network.id

        # Window upon which everything is drawn over
        self.window = gameWindow.GameWindow()

        # Running flag
        self.running = True

        # Dictionary of all game states
        # TODO: implement the menu and the game over menu
        self.states = {
            "Menu" : None,
            "Game" : Play.PlayingPong(self),
            "Game Over Menu" : None
        }
        
        # Holds whatever state is currently running
        self.currentState = self.states["Game"]

        # Instantiate clock object that dictates frame rate
        self.clock = pygame.time.Clock()

    # =============================================================================
    # Name: gameLoop
    # Purpose: Runs the game loop
    # =============================================================================
    def gameLoop(self):
        while self.running:
            
            # Try to keep it at 60 fps
            self.clock.tick(60)

            # Go through events of current state
            self.currentState.runEvents()

            # Search for player quit event, quit if it exists
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            # Update the window
            pygame.display.flip()