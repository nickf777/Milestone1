import random

#Function to print out the board

def display_board(board):
    print(f'{board[0]} | {board[1]} | {board[2]}')
    print(f'{board[3]} | {board[4]} | {board[5]}')
    print(f'{board[6]} | {board[7]} | {board[8]}')

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

def place_marker(board,marker,position):
    board[position] = marker
    display_board(board)

def win_check(board,marker):
    return ((board[0] == marker and board[1] == marker and board[2] == marker) or #top row
    (board[3] == marker and board[4] == marker and board[5] == marker) or #middle row
    (board[6] == marker and board[7] == marker and board[8] == marker) or #bottom row
    (board[0] == marker and board[3] == marker and board[6] == marker) or #col 1
    (board[1] == marker and board[4] == marker and board[7] == marker) or #col 2
    (board[2] == marker and board[5] == marker and board[8] == marker) or #col 3
    (board[0] == marker and board[4] == marker and board[8] == marker) or #diag 1
    (board[2] == marker and board[4] == marker and board[6] == marker))  #diag 2

    #returns true if any win condition is met

def choose_first():
    print('We will now decide who goes first.')
    print('Deciding...')
    player1 = 10
    player2 = 11
    decision = random.randint(10,11)
    if decision == player1:
        first_player = 'Player 1'
        second_player = 'Player 2'
        print('Player 1 goes first')
    elif decision == player2:
        first_player = 'Player 2'
        second_player = 'Player 1'
        print('Player 2 goes first')
    return first_player, second_player

def space_check(board,position):
    possible_items = ['X','O']
    #Returns a boolean indicating whether or not a space on the board is freely available
    if board[position] not in possible_items:
        return True
    else:
        return False

def full_board_check(board):
    remaining_spaces = 0
    possible_items = ['X','O']
    for item in board:
        if item not in possible_items:
            remaining_spaces += 1
    if remaining_spaces == 0:
        return True
    else:
        return False


def player_choice(board):
    #Write a function that asks for a player's next position (as a number 1-9) and then uses the function space_check to check if it's a free position. If it is, then return the position for later use.
    free_space = False
    while free_space == False:
        choice = int(input('Please pick a position to play. (0-8)'))
        if space_check(board,choice) == False:
            print('Sorry, that space is already taken. Please pick another.')
        else:
            print(f'You chose {choice}. Great choice!')
            free_space = True
    return choice

def replay():
    replay_choice = input('Do you want to play again (Y/N)').upper().strip()
    return replay_choice == 'Y'

def run_game():
    
    game_status = True
    test_board = ['0','1','2','3','4','5','6','7','8']

    while game_status == True:
        #Introduce and Assign Players To Their Symbols
        print('Welcome to Tic Tac Toe. Please follow the instructions or the game will implode and I will be very upset.')
        player_list = player_input()
        player1 = player_list[0].upper()
        print(f'Player 1 - you chose {player1} ')
        player2 = player_list[1].upper()
        print(f'Player 2 - that means you are {player2}')

        #Decide who will choose first
        player_order = choose_first()
        first_player = player_order[0] #str Player 1 or Player 2
        second_player = player_order[1]

        #Connect turn order with the player symbols
        first_player_marker = None
        second_player_marker = None
        if first_player == 'Player 1':
            first_player_marker = player1
            second_player_marker = player2
        else:
            first_player_marker = player2
            second_player_marker = player1
        

        #Empty Board With Index Numbers is Shown
        print('Here is the board: ')
        display_board(test_board)

        #Allow the first player to place their marker. The symbols are held in player 1 and player 2
        
        board_check = False
        game_won = False
        while board_check == False and game_won == False:
            #First player chooses
            print(f'{first_player} it is time to place your marker')
            choice = player_choice(test_board)
            space_check(test_board,choice)
            place_marker(test_board,first_player_marker,choice)
            board_check = full_board_check(test_board)
            game_won = win_check(test_board,first_player_marker)
            if game_won == True: 
                print(f'{first_player} you win! Congratulations!')
                break
            elif board_check == True:
                print('The board is full - it is a tie!')
                break
            

            #Second player chooses
            print(f'{second_player} it is time to place your marker')
            choice = player_choice(test_board)
            space_check(test_board,choice)
            place_marker(test_board,second_player_marker,choice)
            board_check = full_board_check(test_board)
            game_won = win_check(test_board,second_player_marker)
            if game_won == True: 
                print(f'{second_player} you win! Congratulations!')
                break
            elif board_check == True:
                print('The board is full - it is a tie!')
                break
            
           


        #Ask if they want to replay
        replay_choice = replay()
        if replay_choice == True:
            print("Let's play again!")
        else:
            print('Thanks for playing!')
            game_status = False



