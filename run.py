#Random module for randomly accepting the values
# ‘X’ indicates the ships hit
# ‘ - ’ indicates the hits missed
from random import randint

HIDDEN_PATTERN = [[' '] * 8 for x in range(8)]
GUESS_PATTERN = [[' '] * 8 for x in range(8)]

let_to_num = {'A':0,'B':1, 'C':2,'D':3,'E':4,'F':5,'G':6,'H':7}


def print_board(board):
    print('  A B C D E F G H') 
    print(' *****************')
    row_num = 1
    for row in board:
        print("%d|%s|" % (row_num, "|".join(row)))
        row_num +=1




def get_ship_location():
    while True:
        # Enter the row number between 1 to 8
        row = input('Please enter a ship row 1-8 ').strip()
        if row.isdigit() and row in '12345678':
            break
        else:
            print('Please enter a valid number between 1-8')
    while True:
        # Enter the Ship column from A TO H
        column = input('Please enter a ship column A-H ').upper().strip()
        if column in 'ABCDEFGH' and column no:
            
        else:
            print("Please enter a valid letter ")
    return int(row) - 1, let_to_num[column]

#Function that creates the ships
def create_ships(board):
    for ship in range(5):
        ship_r, ship_cl = randint(0,7), randint(0,7)
        while board[ship_r][ship_cl] == 'X':
            ship_r, ship_cl  =  randint(0, 7), randint(0, 7)
        board[ship_r][ship_cl] =  'X'


def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == 'X':
                count += 1
    return count

create_ships(HIDDEN_PATTERN)
#print_board(Hidden_Pattern)
turns = 10
while turns > 0:
    print('Welcome to Battleship')
    print_board(GUESS_PATTERN)
    row, column = get_ship_location()
    if GUESS_PATTERN[row][column] ==  '-':
        print(' You already guessed that ')
    elif HIDDEN_PATTERN[row][column] == 'X':
        print(' Congratulations you have hit the battleship ')
        GUESS_PATTERN[row][column] =  'X'
        turns -= 1
    else:
        print('Sorry, You missed')
        GUESS_PATTERN[row][column] = '-'
        turns -= 1
    if  count_hit_ships(GUESS_PATTERN) == 5:
        print(" Congratulations you have sunk all the battleships ")
        break
    print(' You have ' + str(turns) + ' turns remaining ')
    
    
    if turns  ==  0:
        print('Game Over ')
        break
