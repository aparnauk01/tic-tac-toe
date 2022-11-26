

import random
class Player:
    def __init__(self,letter):
        self.letter = letter
    
    def get_move(self,game):
         pass


    
class Computer_Player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        val = random.choice(game.available_spots())
        return val

class Human_player(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self,game):
        valid_value = False
        val = None
        while not valid_value:
            square = input('Enter the valid value(0-9) :\n')
            try:
                val = int(square)
                if val not in game.available_spots():
                    raise ValueError('Invalid square')
                valid_value = True
            except ValueError as ve:
                print('Invalid Number')
        return val