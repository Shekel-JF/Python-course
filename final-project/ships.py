from random import randint
import os
import time
import numpy as np
#Board for holding ship locations
HIDDEN_BOARD = [[" "] * 10 for x in range(10)]
# Board for displaying hits and misses
GUESS_BOARD = [[" "] * 10 for i in range(10)]
PLAYER_BOARD = [[" "] * 10 for i in range(10)]

def print_board(board):
    print("   A B C D E F G H I J")
    row_number = 1
    for row in board:
        row_number_str = str(row_number).rjust(2)
        row_str = "|".join(row)
        print("%s|%s|" % (row_number_str, row_str))
        row_number += 1

letters_to_numbers ={
    'A': 0,
    'B': 1,
    'C': 2,
    'D': 3,
    'E': 4,
    'F': 5,
    'G': 6,
    'H': 7,
    'I': 8,
    'J': 9
}

ships_size = [1, 1, 1, 1, 2, 2, 2, 3, 3, 4]
ship_front = [-1, 1]

global stop_condition
stop_condition = 0
global lose_condition
lose_condition = 0
global hit_last_turn
hit_last_turn = False
global col
col = 0
global row
row = 0

def create_ships(board):
  global win_condition
  win_condition = 0
  for size in ships_size:
    ship_row, ship_column = randint(0,9), randint(0,9)
    direction = randint(0, 1)
    front = randint(0, 1)
    if direction == 0:
      while(ship_row + size * front > 9):
        ship_row-=1
      while(ship_row + size * front < 0):
        ship_row+=1
      while size > 0:
        if board[ship_row + ship_front[front] * size][ship_column] != "X":
          board[ship_row + ship_front[front] * size][ship_column] = "X"
        else:
          tempx = randint(0, 9)
          tempy = randint(0, 9)
          while(board[tempx][tempy] == "X"):
            tempx = randint(0, 9)
            tempy = randint(0, 9)
          board[tempx][tempy] = "X"
        size-=1
        win_condition+=1         
    else:
      while(ship_column + size * ship_front[front] > 9):
        ship_column-=1
      while(ship_column + size * ship_front[front] < 0):
        ship_column+=1
      while size > 0:
        if board[ship_row][ship_column + ship_front[front] * size] != "X":
          board[ship_row][ship_column + ship_front[front] * size] = "X"
        else:
          tempx = randint(0, 9)
          tempy = randint(0, 9)
          while(board[tempx][tempy] == "X"):
            tempx = randint(0, 9)
            tempy = randint(0, 9)
          board[tempx][tempy] = "X"
        size-=1
        win_condition+=1
    if(win_condition == 20):
      break
def longships(ships, board):
  os.system('cls')
  print_board(board)
  global stop_condition
  ship_row = input("What row would you want your " + str(ships) +"-field ship on?: ") 
  while ship_row not in "12345678910":
    print('Not an appropriate choice, please select a valid row')
    ship_row = input("What row would you want your single-field ship on?: ")
  ship_column = input("Enter the column of the ship: ").upper()
  while ship_column not in "ABCDEFGHIJ":
    print('Not an appropriate choice, please select a valid column')
    ship_column = input("Enter the column of the ship: ").upper()
  direction = input("You want it to be horizontal (h) or vertical (v)?: " ).upper()
  while direction not in "HV":
    direction = input("You want it to be horizontal (h) or vertical (v)?: ").upper()
  
  temp = ships
  legit = True

  while(temp > 0):
    tempv = temp - 1
    temph = temp - 1
    if direction == 'H':
      tempv = 0
    else:
      temph = 0
    if int(ship_row) + tempv-1 > 9 or letters_to_numbers[ship_column] + temph > 9:
      print("Battlefront is the other way!")
      legit = False
      longships(ships, board)
      break
    elif(board[int(ship_row) + tempv-1][letters_to_numbers[ship_column] + temph] == "X"):
      print("You've already put your ship there!")
      legit = False
      time.sleep(1)
      longships(ships, board)
      break
    temp-=1

  if legit == True:
    stop_condition+=1
    temp = ships
    
    while(temp > 0):
      tempv = temp - 1
      temph = temp - 1
      if direction == 'H':
        tempv = 0
      else:
        temph = 0
      
      board[int(ship_row) + tempv - 1][letters_to_numbers[ship_column] + temph] = "X"
      ships_size.append(ships)
      temp-=1

def player_ships(board):
  global stop_condition
  for ships in ships_size:   
    os.system('cls')
    print_board(board)
    if(ships==1):
      ship_row = input("What row would you want your single-field ship on?: ")
      while ship_row not in "12345678910":
        print('Not an appropriate choice, please select a valid row')
        ship_row = input("What row would you want your single-field ship on?: ").upper()
      ship_column = input("Enter the column of the ship: ").upper()
      while ship_column not in "ABCDEFGHIJ":
        print('Not an appropriate choice, please select a valid column')
        ship_column = input("Enter the column of the ship: ").upper()
      if(board[int(ship_row)-1][letters_to_numbers[ship_column]] != "X"):
        board[int(ship_row)-1][letters_to_numbers[ship_column]] = "X"
        stop_condition+=1
      else:
        print("You've already put your ship there!")
        ships_size.append(1)
        time.sleep(1)
    
    elif(ships == 2):
      longships(ships, board)
    elif(ships == 3):
      longships(ships, board)
    elif(ships == 4):
      longships(ships, board)
    if stop_condition == 10:
       break


def get_ship_location():
    row = input("Enter the row of the ship: ").upper()
    while row not in "12345678910":
        print('Not an appropriate choice, please select a valid row')
        row = input("Enter the row of the ship: ").upper()
    column = input("Enter the column of the ship: ").upper()
    while column not in "ABCDEFGHIJ":
        print('Not an appropriate choice, please select a valid column')
        column = input("Enter the column of the ship: ").upper()
    return int(row) - 1, letters_to_numbers[column]

def enemy_turn(board):
    global lose_condition
    global hit_last_turn
    global col
    global row
    if(hit_last_turn == True):
      direction = randint(0, 1)
      if(direction == 0 and col-1 > 0):
        col-=1
      elif(row-1 > 0):
        row-=1
      else:
        col = randint(0, 9)
        row = randint(0, 9)  
    else:
      col = randint(0, 9)
      row = randint(0, 9)
    while(board[row][col] == "-" or board[row][col] == "O"):
      col = randint(0, 9)
      row = randint(0, 9)
    if board[row][col] == "X":
      board[row][col] = "O"
      lose_condition+=1
      hit_last_turn = True
      print("Enemy hit!")
    else:
      print("Enemy missed!")
      board[row][col] = "-"
      hit_last_turn = False

#check if all ships are hit
def count_hit_ships(board):
    count = 0
    for row in board:
        for column in row:
            if column == "X":
                count += 1
    return count

if __name__ == "__main__":
    
    player_ships(PLAYER_BOARD)
    create_ships(HIDDEN_BOARD)
    turns = 80
    os.system('cls')
    while turns > 0:
        print('Guess a battleship location')
        print_board(GUESS_BOARD)      
        print("\n       PLAYER BOARD")
        print_board(PLAYER_BOARD)
        row, column = get_ship_location()
        os.system('cls')
        if GUESS_BOARD[row][column] == "-" or GUESS_BOARD[row][column] == "X":
            print("You guessed that one already.")
        elif HIDDEN_BOARD[row][column] == "X":
            print("Hit")
            GUESS_BOARD[row][column] = "X" 
            turns -= 1  
        else:
            print("MISS!")
            GUESS_BOARD[row][column] = "-"   
            turns -= 1    
        if count_hit_ships(GUESS_BOARD) == win_condition:
            print("You win!")
            print_board(GUESS_BOARD)      
            print("\n       PLAYER BOARD")
            print_board(PLAYER_BOARD)
            break
        print("You have " + str(turns) + " turns left")
        if turns == 0:
            print("You ran out of turns")
            print_board(GUESS_BOARD)      
            print("\n       PLAYER BOARD")
            print_board(PLAYER_BOARD)           
        enemy_turn(PLAYER_BOARD)
        if lose_condition == 20:
            print("Mission failed we'll get 'em next time!")
            print_board(GUESS_BOARD)      
            print("\n       PLAYER BOARD")
            print_board(PLAYER_BOARD)