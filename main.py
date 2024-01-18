from classes.Base import game
import client

host = '127.0.0.1'
port = 65432

def main():
    Client = client.Client(host, port)
    gameObject = game.Game(Client)

    gameObject.gameLoop()
        
if __name__ == "__main__":
    main()

