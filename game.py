import player
import math
from player import Player,Computer_Player,Human_player
class TicTacToe:
    def __init__(self) -> None:
        self.board = [ ' ' for _ in range(9)]
        self.current_winner = None
    
    def board_structure(self):
        for row in [self.board[i*3: (i+1)*3] for i in range(3)]:
            print("|"+ "|".join(row)+"|")
    
    @staticmethod
    def print_board_num():
        num_board = [[str(i) for i in range(j*3 , (j+1)*3)] for j in range(3)]
        for row in num_board:
            #print(row)
            print("|"+"|".join(row)+"|")

    def available_spots(self):
        return [i for i,spot in enumerate(self.board) if spot == ' ' ]

    def num_available_spots(self):
        return self.board.count(' ')
    
    def empty_squares(self):
        for a in self.board:
            if a == ' ':
                return True
        return False

    def move(self,square,letter):
        if self.board[square] == ' ':
            self.board[square] = letter 
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False
    
    def winner(self,square, letter):
        #check row
        print(square)
        rowind = math.floor(int(square) / 3)
        row = self.board[rowind*3: (rowind+1)*3]
        if all (spot == letter for spot in row):
            return True
        
        #check col
        colind = int(square) % 3
        col = [self.board[colind+(i*3)] for i in range(3)]
        if all (spot == letter for spot in col):
            return True
        # check diagonals
        if int(square)% 2 == 0:
            diagonal1 = [self.board[i] for i in [0,4,8]]
            if all (spot == letter for spot in diagonal1):
                return True
            diagonal2 = [self.board[i] for i in [2,4,6]]
            if all (spot == letter for spot in diagonal2):
                return True
        return False

  
def play(game,x_player,o_player, print_board=True):
    if print_board:
        game.print_board_num()
    letter ='X'
    while game.empty_squares():
        if letter =='X':
            square = x_player.get_move(game)
        else:
            square = o_player.get_move(game)
        if game.move(square,letter):
            if print_board:
                print(f"{letter} makes move to {square}")
                game.board_structure()
            print("Curretn winnder: ")
            print(game.current_winner)
            if game.current_winner:
                print(f"{letter} wins")
                return letter
        if letter == 'X':
            letter= 'O'
        else:
            letter ='X'
    
    print("iTS  atie")           
  

def main():
    x_player = Computer_Player('X')
    o_player = Human_player('O')
    t=TicTacToe()
    play(t,x_player,o_player,print_board=True)

if __name__ == "__main__":
    main()

