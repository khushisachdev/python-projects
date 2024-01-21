#trying to check the functions efficiency
def win_check(board,mark):
    return( (board[1]==mark and board[2]==mark and board[3]==mark) or
            (board[4]==mark and board[5]==mark and board[6]==mark) 
            or (board[7]==mark and board[8]==mark and board[9]==mark)
              or (board[1]==mark and board[4]==mark and board[7]==mark)
                or (board[2]==mark and board[5]==mark and board[8]==mark) 
                or (board[3]==mark and board[6]==mark and board[9]==mark)
                  or(board[1]==mark and board[5]==mark and board[9]==mark) or
                    (board[3]==mark and board[5]==mark and board[7]==mark) )
test_board = ['#','t','O','t','O','t','O','X','O','X']
print(win_check(test_board,'X'))