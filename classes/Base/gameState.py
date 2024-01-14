# =============================================================================
# Name: GameState
# Purpose: Inherited by all states of the program (menu, playing game, etc.)
# =============================================================================
class GameState:
    def __init__(self, GameObj):

        # Gives the game object to the game state so it can reference the window
        self.gameObj = GameObj

        # List of relevant objects to be drawn in each state
        self.objList = []

    # ======================================================================================================
    # Name: runEvents
    # Purpose: Run's the games events
    # ======================================================================================================       
    def runEvents(self):
        pass