import numpy as np
import regex as re
import pandas as pd
import time
from colorama import Style

'''
This is the worst code I have ever written and I can only apologise.
'''

nrs = re.compile('[0-9]+')
boards = []
with open('dec4_input.txt') as ip:
    order_of_numbers = ip.readline().split(",")
    for line in ip:
        if line == '\n': continue
        line = line.replace("\n", "")
        new_line = line.split(" ")
        new_line = filter(None, new_line)
        new_line = list(new_line)
        boards.append(new_line)
ip.close()
#print(boards)
#print("board length", len(boards))

board_collection = []
position_collection = []
wins_collection = []

def fill_position(board):
    position_var = {}
    for i, row in enumerate(board):
        for j in range(5):
            value = row[j]
            position_var[value] = (i,j)
    return position_var

for i in range(0,len(boards),5):
    current_board = boards[i:(i+5)]
    board_collection.append(current_board)
    position_collection.append(fill_position(current_board))
    wins_collection.append(np.zeros((5,5),dtype=np.bool8))

'''board_1 = boards[0:5]
board_2 = boards[5:10]
board_3 = boards[10:15]
position_1, position_2, position_3 = fill_position(board_1), fill_position(board_2), fill_position(board_3)
wins_1, wins_2, wins_3 = np.zeros((5,5),dtype=np.bool8),np.zeros((5,5),dtype=np.bool8),np.zeros((5,5),dtype=np.bool8)'''

def format_row(row):
    return '|' + '|'.join('{0:^5s}'.format(x) for x in row) + '|'

def format_board(board):
    return '\n\n'.join(format_row(row) for row in board)

#print(format_board(board_1), format_board(board_3))
#print(format_board(board_collection[0]))
#print(board_2)
#print(Style.BRIGHT + "Python")

def check_bingo(winning_board):
    for row in winning_board[:]:
        if all(row): return True
    for column in np.transpose(winning_board[:]):
        if all(column): return True

def update_board(board, position, wins, number):
    win_flag = False
    if number not in position.keys():
        return position,wins,win_flag
    x,y = position[number]
    wins[x][y] = True
    if check_bingo(wins): win_flag = True
    return position, wins, win_flag

def calculateScore(number, pos, wins, board):
    indices = zip(*np.where(wins == False))
    val = ''
    values = []
    for x,y in indices:
        val = board[x][y]
        values.append(int(val))
    #print(values, "Sum:", sum(values), "Number:", number)
    current_sum = sum(values)
    return current_sum, number, (current_sum*number)

boards_that_won = []
stop_flag = False

def check_some_numbers(numbers):
    global board_collection
    global position_collection
    global wins_collection
    global stop_flag
    global boards_that_won
    #current_position_2, current_wins_2 = position_2, wins_2
    #current_position_3, current_wins_3 = position_3, wins_3
    for i in numbers:
        for count,bo in enumerate(board_collection):
            if len(boards_that_won) == (len(board_collection)-1):
                #this loop is never reached?
                stop_flag = True
                current_position, current_wins = position_collection[count], wins_collection[count]
                current_position, current_wins, win_flag = update_board(bo, current_position, current_wins, str(i))
                break
                break
            if count in boards_that_won:
                continue
            current_position, current_wins = position_collection[count], wins_collection[count]
            current_position, current_wins, win_flag = update_board(bo, current_position, current_wins, str(i))
            if win_flag:
                #print("Board", count, "has won!")
                #if check_boards_that_won(count):
                if len(board_collection)==1:
                    stop_flag = True
                    #print("Board", count, "has won!", current_wins)
                    #print(calculateScore(int(i), current_position, current_wins, bo))
                    #index = np.where(boards_that_won == 0)[0]
                    #print("Loser board:", index)
                    break
                    break
                boards_that_won.append(count)
'''current_position_2, current_wins_2, win_flag = update_board(board_2, current_position_2, current_wins_2, str(i))
if win_flag:
    print("Board 2 has won!", current_wins_2)
    print(calculateScore(int(i), current_position_2, current_wins_2, board_2))
    break
current_position_3, current_wins_3, win_flag = update_board(board_3, current_position_3, current_wins_3, str(i))
if win_flag:
    print("Board 3 has won!", current_wins_3)
    print(calculateScore(int(i), current_position_3, current_wins_3, board_3))
    break'''

def check_boards_that_won(current_count):
    global boards_that_won
    global board_collection
    global position_collection
    global wins_collection
    boards_that_won[current_count] = 1
    losers = np.count_nonzero(boards_that_won==0)
    if losers < 30:
        print("Current losers: ", losers)
        print(boards_that_won)
    if losers == 1 or losers == 0:
        return True
    else:
        return False

#program_starts = time.time()
#seconds = 15

while not stop_flag:
    check_some_numbers(order_of_numbers[:])
    #current_time = time.time()
    #elapsed_time = current_time - program_starts
    if stop_flag:
        tuple2_comparison = boards_that_won
        print(tuple2_comparison)
        break

def check_board_no(index_to_check, numbers):
    global board_collection
    global position_collection
    global wins_collection
    global stop_flag
    #current_position_2, current_wins_2 = position_2, wins_2
    #current_position_3, current_wins_3 = position_3, wins_3
    for i in numbers:
        bo = board_collection[index_to_check]
        current_position, current_wins = position_collection[index_to_check], wins_collection[index_to_check]
        current_position, current_wins, win_flag = update_board(bo, current_position, current_wins, str(i))
        if win_flag:
            #if check_boards_that_won(count):
                print(calculateScore(int(i), current_position, current_wins, bo))
                #index = np.where(boards_that_won == 0)[0]
                #print("Loser board:", index)
                break

tuple1 = np.arange(0,100,1)
tuple2 = (69, 45, 83, 47, 64, 29, 36, 13, 89, 27, 40, 41, 76, 18, 21, 86, 87, 5, 14, 2, 16, 62, 7, 90, 8, 95, 15, 82, 63, 72, 74, 93, 94, 6, 22, 25, 56, 17, 59, 31, 32, 65, 0, 57, 50, 55, 35, 39, 70, 91, 9, 24, 42, 44, 96, 99, 73, 49, 68, 78, 79, 85, 30, 81, 88, 84, 33, 43, 52, 67, 92, 3, 61, 71, 34, 53, 58, 66, 77, 12, 23, 28, 37, 75, 11, 20, 48, 54, 60, 80, 97, 98, 10, 46, 1, 51, 26, 38, 4)

print([x for x in tuple1 if x not in tuple2])
#missing no. is 19; so this is probably the last board. tuple2_comparison directly comes from
# the while loop that checks all of the input data; it corresponds to tuple2 (manually copied).
#this leads me to assume 19 is indeed the last board. 

check_board_no(19,order_of_numbers[:])
