def display_board(board):
    
    print(" "+board[7]+" | "+board[8]+" | "+board[9]+" ")
    print("-------------")
    print(" "+board[6]+" | "+board[5]+" | "+board[4]+" ")
    print("-------------")
    print(" "+board[3]+" | "+board[2]+" | "+board[1]+" ")
board=["#","x","O","x","O","x","O","x","O","x","O"]
def player_input():
    marker=input()
    while not(marker=='X' or marker=='O'):
        marker=input("Enter a marker X/O").upper()
    if marker=='X':
        return('X','O')
    else:
        return('O','X')
def place_marker(board,marker,position):
    board[position]=marker
def win_check(board,marker):
    if((board[7]==marker and board[8]==marker and board[9]==marker) or
      (board[1]==marker and board[2]==marker and board[3]==marker) or
      (board[4]==marker and board[5]==marker and board[6]==marker) or
      (board[3]==marker and board[6]==marker and board[7]==marker) or
      (board[2]==marker and board[5]==marker and board[8]==marker) or
      (board[1]==marker and board[4]==marker and board[9]==marker) or
      (board[1]==marker and board[5]==marker and board[7]==marker) or
      (board[3]==marker and board[5]==marker and board[9]==marker) ):
        return True
    else:
        return False
import random
def choose_first():
    num=random.randint(0,1)
    if num==1:
        return 'player 1'
    else:
        return 'player 2'
def space_check(board,position):
    return board[position] == ' '
def full_board_check(board):
    isFull=True
    for i in board:
        if i==' ':
            isFull=False
    return isFull
def full_board_check(board):
    for i in range(1,10):
        if space_check(board,i):
            return False
    return True
def players_choice(board):
    position=0
    while not position in [1,2,3,4,5,6,7,8,9] or not space_check(board,position):
        position=int(input("Enter next position :"))
    return position
def replay():
    return input("Do you want to play again(Y/N) :").lower().startswith('y')
while True:
    board=[' ']* 10
    player1_marker,player2_marker=player_input()
    turn=choose_first()
    print(turn + " will play First")
    play_game=input("Are you ready to play the game Y/N").lower().startswith('y')
    if play_game:
        game_on=True
    else:
        game_on=False
    while game_on:
        if turn == 'player 1':
            display_board(board)
            position=players_choice(board)
            place_marker(board,player1_marker,position)
            if win_check(board,player1_marker):
                display_board(board)
                print("The game is draw, Better luvk next time! :")
                break
            else:
                turn="player 2"
        else:
            display_board(board)
            position=players_choice(board)
            place_marker(board,player2_marker,position)
            if win_check(board,player2_marker):
                display_board(board)
                print("Player 2 won the game!! congratzz")
                game_on=False
            else:
                if full_board_check(board):
                    display_board(board)
                    print("The game is draw, Better luvk next time! :")
                    break
                else:
                    turn="player 1"
    if not replay():
        break
    
