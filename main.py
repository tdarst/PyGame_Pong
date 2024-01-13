import pygame
from classes.Surfaces import paddle, pongBall, pongSurface
from classes.Window import gameWindow
from classes.Base import game

# Initialize game window object
#GAME_WINDOW = gameWindow.GameWindow()


def main():
    gameObject = game.Game()

    gameObject.gameLoop()
        
if __name__ == "__main__":
    main()

