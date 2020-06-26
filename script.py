test_board = ['#','X','O','X','O','X','O','X','O','X']

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
    pass




