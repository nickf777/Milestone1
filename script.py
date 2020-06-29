import random
test_board = ['0','1','2','3','4','5','6','7','8','9']

#Function to print out the board

def display_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[6]} | {board[7]} | {board[8]}')
    

#display_board(test_board)

def player_input():
    #Players pick their symbols
    choice_list = ['x', 'o']
    player1_symbol = ''

    #System validates the symbol choice
    while player1_symbol not in choice_list:
        player1_symbol = input('Player 1 - Do you want to be X or O?').strip().lower()
        if player1_symbol not in choice_list:
            print('Sorry that is not an accepted option - please pick X or O.')
    
    #System assigns the opposite symbol to Player 2

    new_list = [item for item in choice_list if item != player1_symbol]
    player2_symbol = new_list[0]
    
    return player1_symbol,player2_symbol

    #This returns a tuple

def place_marker(board,marker,position):
    
    #board is a list obect with 9 objects
    #marker is the player symbol
    #position is the index at which the player puts the symbol

    board[position] = marker
    display_board(board)
    

    #possible_indices = [i for i in range(0,10)]
    #choice = None
    
    #Asks the player for input, provides index number - if the input is not in a list  of possible options, displays the board and asks for a new input
    #while choice not in possible_indices:
    #    choice = int(input('Where would you like to place your marker? (0-9)'))
    #    if choice not in possible_indices:
    #        print('Sorry, that is not an accepted option - please pick a number from 0-9.')
    #        display_board(test_board)

    #Places the marker at a specific spot
    #board[choice] = marker


#place_marker(test_board,'X',2)

def win_check(board,marker):
    return board[0] == marker and board[1] == marker and board[2] == marker or #top row
    return board[3] == marker and board[4] == marker and board[5] == marker or #middle row
    return board[6] == marker and board[7] == marker and board[8] == marker or #bottom row
    return board[0] == marker and board[3] == marker and board[6] == marker or #col 1
    return board[1] == marker and board[4] == marker and board[7] == marker or #col 2
    return board[2] == marker and board[5] == marker and board[8] == marker or #col 3
    return board[0] == marker and board[4] == marker and board[8] == marker or #diag 1
    return board[2] == marker and board[4] == marker and board[6] == marker or #diag 2

    #returns true if any win condition is met

def choose_first():
    print('We will now decide who goes first.')
    player1 = 0
    player2 = 1
    decision = random.randint(0,1)
    if decision == player1:
        print('Player 1 goes first')
    else:
        print('Player 2 goes first')
