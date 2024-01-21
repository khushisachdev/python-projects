#tic tac toe game code
#displaying a tic tac board and updationg it on user input
#displaying the board again and again after each round tic tac toe board on a number board "x" and "o
import random 


def display_board(board):
    
    print(board[7]+'|'+board[8]+'|'+board[9])
    print('-|-|-')
    print(board[4]+'|'+board[5]+'|'+board[6])
    print('-|-|-')
    print(board[1]+'|'+board[2]+'|'+board[3])
    

def player_input():
    marker=' '
    while marker!='X' and marker!='O':
        marker=input("Player 1 choose X or O: ").upper()
    player1=marker
    if player1=='X':
        return('X','O')
    else:
        return('O','X')
def position_marker(board,marker,position):
    board[position]=marker
def win_check(board,mark):
    return( (board[1]==mark and board[2]==mark and board[3]==mark) or
            (board[4]==mark and board[5]==mark and board[6]==mark) 
            or (board[7]==mark and board[8]==mark and board[9]==mark)
              or (board[1]==mark and board[4]==mark and board[7]==mark)
                or (board[2]==mark and board[5]==mark and board[8]==mark) 
                or (board[3]==mark and board[6]==mark and board[9]==mark)
                  or(board[1]==mark and board[5]==mark and board[9]==mark) or
                    (board[3]==mark and board[5]==mark and board[7]==mark) )
def choose_first():
    flip=random.randint(0,1)
    if(flip==0):
        return 'Player1'
    else:
        return 'Player2'
def space_check(board,position):
    if(board[position]==' '):
        return True
    else:
        return False 
def full_board(board):
    for i in range(1,10):
        if(space_check(board,i)):
            return False
    return True
def player_choice(board):
    choice=0
    while choice not in range(1,10) or not space_check(board,choice):
        choice=int(input("choose a position in (1-9): "))
    return choice 
def replay():
    choice=input("want to play again ('Yes'or 'No'): ").lower()
    if(choice=="yes"):
        return True
    else:
        return False
#game logic have a while loop on a replay function 
def Tic_tac_toe():
    print("welcome to game of TIC TAC TOE !!")
    while(True):
        #play the game 
        the_board=[' ']*10
        player1_marker,player2_marker=player_input()
        turn=choose_first()
        print(turn+" will go first")
        play_game=input("want to play a game: yes or no ")
        if(play_game=="yes"):
            game_on=True
        else:
            game_on=False
            break



        #game_play
        while(game_on):
            if(turn=="player1" or turn=="Player1"):
                display_board(the_board)
                choice=player_choice(the_board)
                position_marker(the_board,player1_marker,choice)
                if(win_check(the_board,player1_marker)==True):
                    display_board(the_board)
                    print("Player 1 has won ")
                    game_on=False
                else:
                    if(full_board(the_board)==True):
                        display_board(the_board)
                        print("Tie")
                        game_on=False
                    else:
                        turn="Player2"
            else:
                display_board(the_board)
                choice=player_choice(the_board)
                position_marker(the_board,player2_marker,choice)
                if(win_check(the_board,player2_marker)):
                    display_board(the_board)
                    print("Player 2 has won ")
                    game_on=False
                else:
                    if(full_board(the_board)):
                        display_board(the_board)
                        print("Tie")
                        game_on=False
                    else:
                        turn="Player1"



        if(replay()==False):
            break 
        else:
            Tic_tac_toe()
Tic_tac_toe()