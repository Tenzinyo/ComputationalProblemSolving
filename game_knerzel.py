def printRules():
    print("""
    The Game of Knerzel

    This is a turn-taking dice game for two players. 
    "Knerzel" is the German word for the crusty end of a loaf of bread.

    During each round, each player starts with a whole loaf, 12 slices of bread.
    The goal is to end each turn with the smallest non-zero number of slices.

    A player begins their turn by rolling a six-sided die. 
    The value of the dice roll is subtracted from the number of slices.
    As long as some slices remain, the player may choose to roll again.
    If all the slices are gone, the Knerzel is lost and the turn is over.

    During each round, the player with the higher total score goes first. 
    If the players are tied, a player is chosen at random.

    After both players have taken a turn, their turn scores are compared.
    The player with the lowest non-zero turn score earns that many points 
    towards their total score. If the turn scores are tied, neither player
    earns any points.

    The game ends when at least one player has 12 or more total points.
    The player with the higher score wins. The game may not end in a tie.

    """)

def startingPlayer(player1Score, player2Score):
    """Return the player with the higher score, or a randomly chosen player
    if the scores are tied.

    Parameters:
        player1Score, a non-negative integer
        player2Score, a non-negative integer

    Return value: either 1 or 2
    """
    import random 
    random = random.random()
    
    if player1Score == player2Score:
        if random < 0.5:
            return 1
        else: 
            return 2
    elif player1Score > player2Score:
        return 1
    else:
        return 2
        


def rollAgain():
    """Prompt the user to enter 'y' for yes or 'n' for no until a valid 
    answer is given.

    Return value: True if the user answers 'y', False if the answer is 'n'
    """
    
    yesNo = input('Would you like to role again? Type y for yes and n for no: ')
    assert(yesNo == 'y' or yesNo == 'n')
    if yesNo == 'y':
        return True
    else:
        return False
    


def takeTurn(playerName):
    """Play one turn as described in the rules of the game.

    Parameter: playerName, a string
    

    Return value: the turn points, an integer between 0 and 12 (inclusive)
    """
    import random
    roll = random.random()
    playerName = str(input('Player Name? '))
    knerzel = 12
    
    
    while knerzel > 0 :
        if rollAgain() == True:
            
            if roll < (1/6):
                knerzel = knerzel - 1
            elif roll > (1/6) and roll <= (2/6):
                knerzel = knerzel - 2
            elif roll > (2/6) and roll <= (3/6):
                knerzel = knerzel -3
            elif roll > (3/6) and roll <= (4/6):
                knerzel = knerzel - 4
            elif roll > (4/6) and roll <= (5/6):
                knerzel = knerzel - 5
            else:
                knerzel = knerzel - 6
            print(' Your score is ' + str(knerzel) )
        else:
            return knerzel

