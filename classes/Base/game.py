import pygame
from classes.Window import gameWindow
from . import gameState

class Game:
    def __init__(self):
        self.window = gameWindow.GameWindow()

        self.running = True

        self.states = {
            "Menu" : 0,
            "Game" : gameState.PlayingPong(self)
        }
        
        self.currentState = self.states["Game"]

        self.clock = pygame.time.Clock()

    def gameLoop(self):
        while self.running:

            self.clock.tick(60)

            self.currentState.EventLoop()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            pygame.display.flip()