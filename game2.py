import time
from player2 import HumanPlayer, RandomComputerPlayer,GeniusComputerPlayer
class TicTacToe:
    def __init__(self):
        self.board = [' ' for _ in range(9) ] #we will use single list to represent #*3 board
        self.current_winner = None #keep track of winner!

    def print_board(self):
        #this is just getting rows
        for row in [self.board[i*3 : (i+1)*3] for i in range(3)]:
            print('| ' + ' | '.join(row) + ' |')

    @staticmethod
    def print_board_nums():
        #0 | 1 | 2 ectc tells what number corresponds to what box

        number_board = [[str(i) for i in range(j*3, (j+1)*3)] for j in range(3)]
        for row in number_board:
            print('| ' + ' | '.join(row) + ' |')


    def available_moves(self):
        #list comprehension
        return[i for i, spot in enumerate(self.board) if spot == ' ']

    def empty_squares(self):
        return ' ' in self.board

    def num_empty_squares(self):
        return self.board.count(' ')

    def make_move(self, square, letter):
        #if valid move then make move(assign square to letter)
        #then return true if invalid retrurn false
        if self.board[square] == ' ':
            self.board[square] = letter
            if self.winner(square,letter):
                self.current_winner = letter
            return True
        return False

    def winner(self, square, letter):
        #winner if 3 in row anywhere we have to check all of these
        #first lets check row
        row_ind = square // 3
        row = self.board[row_ind*3 : (row_ind +1) * 3]
        if all([spot == letter for spot in row]):
            return True

        #check column
        col_ind = square %3
        column = [self.board[col_ind+i *3] for i in range(3)]
        if all([spot == letter for spot in column]):
            return True

        #check diagonal
        #but ony if square is an even number(0,2,4,,6,8)
        #these are only possible move to win diagonal
        if square %2 ==0:
            diagonal1 = [self.board[i] for i in [0, 4, 8]] #left to right diagonal
            if all([spot == letter for spot in diagonal1]):
                return True
            diagonal2 = [self.board[i] for i in [2, 4, 6]] #right to left diagonal
            if all([spot == letter for spot in diagonal2]):
                return True
        #if all these check fails
        return False
            
                
               
def play(game, x_player, o_player, print_game= True):
    #return winner of game or none it tie
    if print_game:
        game.print_board_nums()

        letter = 'X' #starting letter
        #iterate while the game still has empty squares
        #we dont have to worry about winner because we will just retrun that
        #which will break the loop

        while game.empty_squares():
            
            
            #get move from appropriate player
            if letter == 'O':
                square = o_player.get_move(game)
            else:
                square = x_player.get_move(game)

            #lets define a fun to make a move
            if game.make_move(square, letter):
                    if print_game:
                        print(letter +f' makes a move to square {square}')
                        game.print_board()
                        print(' ') #just empty line

                    if game.current_winner:
                        if print_game:
                            print(letter + 'wins!')
                        return letter

                    #after we made our move we need to alternate letters
                    letter = 'O' if letter == 'X' else 'X' #switches player
          #tiny break
            time.sleep(0.8)
               
             

    if print_game:
        print("IT's a TIE!!!")

if __name__ == '__main__':
    x_player = HumanPlayer('X')
    o_player = GeniusComputerPlayer('O')
    t = TicTacToe()
    result = play(t, x_player, o_player, print_game=True)
       
                
            
        
