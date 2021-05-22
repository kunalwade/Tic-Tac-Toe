
import math
import random

class Player:
    def __init__(self, letter):
        #letter is x or o
        self.letter= letter

        #we wamt all players to get next move

    def get_move(self, game):
        pass

#Inheritance used
class RandomComputerPlayer(Player):
    def __init__(self, letter):
        #letter will be x or o for tic tac toe
        super().__init__(letter)

    def get_move(self, game):
        #get a random valid spot for next move
        square = random.choice(game.available_moves())
        return square

class HumanPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        valid_square = False
        val = None
        while not valid_square:
            square = input(self.letter + '\'s turn. Input move (0-8):')
            #we are going to check that this is correct value by trying to cast
            #it to an integer and if it's not then we say its invalid
            #if that spot is not available on board then we say its invalid
            
            try:
                val = int(square)
                if val not in game.available_moves():
                    raise ValueError
                valid_square = True #if these are succesful then yay!!
            except ValueError:
                print("Invalid Square. Try bAgain")

        return val

class GeniusComputerPlayer(Player):
    def __init__(self, letter):
        super().__init__(letter)

    def get_move(self, game):
        if len(game.available_moves()) ==9:
            square = random.choice(game.available_moves()) #randomly chose one
        else:
            #get squaure based of minimax algorithm
            square = self.minimax(game, self.letter)['position']
        return square
    def minimax(self, state, player):
        max_player = self.letter #yourself means uss
        other_player = 'O' if player == 'X' else 'X' #other player

        #first we want to check if previous move is a winner
        #this is the base case
        if state.current_winner == other_player:
            #we should return position AND score bcoz we need to keep track of score
            #for minimax to work
            return{'position': None,
                   'score': 1 * (state.num_empty_squares() +1) if other_player == max_player else -1 *(
                       state.num_empty_squares() +1)}
        elif not state.empty_squares(): #no empty squares
            return{'positions': None, 'score': 0}

        #initialize some dictionaries
        if player == max_player:
            best = {'positions': None, 'score': -math.inf} #each score should maximize(be larger)
        else:
            best = {'positions': None, 'score': math.inf} #each score should minimize

        for possible_move in state.available_moves():
            #step1: make a move try that spot
            state.make_move(possible_move, player)
            #step2: recurse using minimax a game after making that move
            sim_score = self.minimax(state, other_player) #we alternate players
            

            #step3: undo the move
            state.board[possible_move] = ' '
            state.current_winner = None
            sim_score['position'] = possible_move #otherwise this will get messed up from recursion
            
            #step4: update dictionary if necessary
            if player == max_player:
                if sim_score['score'] > best['score']:
                    best =sim_score #replace best
            else:  #but minimize the other player
                if sim_score['score'] < best['score']:
                    best = sim_score #replace best

        return best
                    
            
            
            


    
        
        
