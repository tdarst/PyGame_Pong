from classes.Base import game

host = '127.0.0.1'
port = 65432

def main():
    gameObject = game.Game()
    gameObject.gameLoop()
        
if __name__ == "__main__":
    main()

