from IPython.display import clear_output

def display_board(board):
    clear_output()
    
    print('   |   |')
    print(' ' + board[7] + ' | ' + board[8] + ' | ' + board[9])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[4] + ' | ' + board[5] + ' | ' + board[6])
    print('   |   |')
    print('-----------')
    print('   |   |')
    print(' ' + board[1] + ' | ' + board[2] + ' | ' + board[3])
    print('   |   |')

    
def place_marker(board, marker, position):
    board[position] = marker


def win_check(board,mark):
    
    return ((board[7] == mark and board[8] == mark and board[9] == mark) or 
    (board[4] == mark and board[5] == mark and board[6] == mark) or 
    (board[1] == mark and board[2] == mark and board[3] == mark) or 
    (board[7] == mark and board[4] == mark and board[1] == mark) or 
    (board[8] == mark and board[5] == mark and board[2] == mark) or 
    (board[9] == mark and board[6] == mark and board[3] == mark) or 
    (board[7] == mark and board[5] == mark and board[3] == mark) or 
    (board[9] == mark and board[5] == mark and board[1] == mark)) 

import random

def choose_first():
    if random.randint(0, 1) == 0:
        return 'I'
    else:
        return 'You'
    
def space_check(board, position):
    return board[position].isdigit() 

def full_board_check(board):
    for i in range(1,10):
        if space_check(board, i):
            return False
    return True

def player_choice(board):
    position = 0
    while position not in [1,2,3,4,5,6,7,8,9] or not space_check(board, position):
        position = int(input('Choose your next position: (1-9) '))
    return position

def replay():
    response = input('Do you want to play again? Enter Yes or No: ').lower()
    if response.startswith('y'):
        return True
    else:
        print("Okay bye :(")
        return False

def check_win_move(board, marker, i):
    temp_board = board.copy()
    temp_board[i] = marker
    return win_check(temp_board, marker)

def check_fork_move(board, marker, i):
    temp_board = board.copy()
    temp_board[i] = marker
    winning_moves = 0
    for j in range(1,10):
        if check_win_move(temp_board, marker, j) and temp_board[j] == str(j):
            winning_moves += 1
    return winning_moves >= 2

def computer_choice(board, computer_marker, player_marker):
    # First, check if we can win in the next move
    for i in range(1,10):
        if space_check(board, i):
            if check_win_move(board, computer_marker, i):
                return i

    # Block the player's win move
    for i in range(1,10):
        if space_check(board, i):
            if check_win_move(board, player_marker, i):
                return i

    # Try to take one of the corners if they are free
    for i in [1, 3, 7, 9]:
        if space_check(board, i):
            return i

    # Try to take the center if it is free
    if space_check(board, 5):
        return 5

    # Play on one of the sides
    for i in [2, 4, 6, 8]:
        if space_check(board, i):
            return i

    # Take any free space
    for i in range(1,10):
        if space_check(board, i):
            return i

print("LET'S PLAY TIC TAC TOE :D")

while True:
    # Reset the board
    theBoard = [''] + list(map(str, range(1, 10)))
    player_marker, computer_marker = 'X', 'O' 
    turn = choose_first()
    print(turn + ' will go first.')
    
    play_game = input('Are you ready to play? Enter Yes or No: ')
    
    if play_game.lower()[0] == 'y':
        game_on = True
    else:
        game_on = False

    while game_on:
        if turn == 'You':
            # Player's turn.
            display_board(theBoard)
            position = player_choice(theBoard)
            place_marker(theBoard, player_marker, position)

            if win_check(theBoard, player_marker):
                display_board(theBoard)
                print('Congratulations! You have won the game!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("It's a draw!")
                    break
                else:
                    turn = 'I'

        else:
            # Computer's turn.
            display_board(theBoard)
            position = computer_choice(theBoard, 'O', 'X')  # Aquí estamos llamando a la función con los nuevos argumentos
            place_marker(theBoard, 'O', position)

            if win_check(theBoard, 'O'):
                display_board(theBoard)
                print('I have won!')
                game_on = False
            else:
                if full_board_check(theBoard):
                    display_board(theBoard)
                    print("It's a draw!")
                    break
                else:
                    turn = 'You'

    if not replay():
        break