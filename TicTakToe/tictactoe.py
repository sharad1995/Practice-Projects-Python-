#!/usr/bin/python

#Tic-Tak-Toe Game

# import only system from os
from os import system, name
# import sleep to show output for some time period
from time import sleep
# import random to select ramdom player to play first
import random



# global variables
position = [0,1,2,3,4,5,6,7,8,9]
# reset the board
theboard = [' ']*10


  
# define clear function 
def clear(): 
    # for windows 
    if name == 'nt': 
        _ = system('cls') 
    # for mac and linux(here, os.name is 'posix') 
    else: 
        _ = system('clear')


# display playing board
def disply_Board(board):
	clear()
	print ("\t "+"|"+"\t "+"|"+"\t")
	print ("    "+board[7]+"    "+"|"+"   "+board[8]+"   "+"|"+"    "+board[9]+"    ")
	print ("\t "+"|"+"\t "+"|"+"\t")
	print ("---------"+"|"+"-------"+"|"+"--------")
	print ("\t "+"|"+"\t "+"|"+"\t")
	print ("    "+board[4]+"    "+"|"+"   "+board[5]+"   "+"|"+"    "+board[6]+"    ")
	print ("\t "+"|"+"\t "+"|"+"\t")
	print ("---------"+"|"+"-------"+"|"+"--------")
	print ("\t "+"|"+"\t "+"|"+"\t")
	print ("    "+board[1]+"    "+"|"+"   "+board[2]+"   "+"|"+"    "+board[3]+"    ")
	print ("\t "+"|"+"\t "+"|"+"\t")


# assign signs
def choose_sign():
	sign = ''
	
	# ask playerA to choose X or O sign
	while sign != 'X' and sign != 'O':
		sign = raw_input("Player A : What would you like to be X or O : ").upper()

	# assign another player the opposite sign
	if sign == 'X':
		return ('X','O')
	else:
		return ('O','X')
	
	return (playerA,playerB)


# place the sign on board
def place_sign(board,sign,position):
	board[position] = sign


# validate the winning player
def validate_win(board,sign):
	return ((board[7] == sign and board[8] == sign and board[9] == sign) or # across the top
    (board[4] == sign and board[5] == sign and board[6] == sign) or # across the middle
    (board[1] == sign and board[2] == sign and board[3] == sign) or # across the bottom
    (board[7] == sign and board[4] == sign and board[1] == sign) or # down the middle
    (board[8] == sign and board[5] == sign and board[2] == sign) or # down the middle
    (board[9] == sign and board[6] == sign and board[3] == sign) or # down the right side
    (board[7] == sign and board[5] == sign and board[3] == sign) or # diagonal
    (board[9] == sign and board[5] == sign and board[1] == sign)) # diagonal


# player input and asign their signer as 'X' or 'O'
def choose_player_move_random():
	if random.randint(0,1) == 0:
		return 'Player 2'
	else:
		return 'Player 1'


# maintain the filled and empty positions
def space_check(board, position):
	return board[position] == ' '
	pass


# check weather board positions are full or not
def board_check(board):
	for i in range(1,10):
		if space_check(board,i):
			return False
	return True


# asks player to choose next position
def choose_position(board):
	pos = 0
	while pos not in [1,2,3,4,5,6,7,8,9] or not space_check(board,pos):
		pos = int(input('Choose your next move : (1-9)'))
	return pos


# asks player to play again
def reply():
	return raw_input('Do you want to play again? Enter yes or no.').lower().startswith('y')


# begin game
def begin():
	print("Welcome to Tic Tac Toe Game of the Year!")
	
	
	# game loop starts
	while True:
		player1_sign, player2_sign = choose_sign()
		turn = choose_player_move_random()
		
		print (turn, 'will make first move!')
		
		play_game = raw_input('Are you ready to play? Enter Yes or No.')
		
		if play_game.lower()[0] == 'y':
			game_on = True
		else:
			game_on = False
		
		while game_on:
			if turn == 'Player 1':
				
				# 1'st player turn code
				disply_Board(theboard)
				position = choose_position(theboard)
				place_sign(theboard, player1_sign, position)
				
				if validate_win(theboard, player1_sign):
					disply_Board(theboard)
					print ('Congratulations! Player 1 have won the game!')
					game_on = False
				else:
					if board_check(theboard):
						disply_Board(theboard)
						print('The game is a draw!')
						break
					else:
						turn = 'Player 2'
			else:
				
				# 2'nd player turn code
				disply_Board(theboard)
				position = choose_position(theboard)
				place_sign(theboard, player2_sign, position)
				
				if validate_win(theboard, player2_sign):
					disply_Board(theboard)
					print ('Congratulations! Player 2 have won the game!')
					game_on = False
				else:
					if board_check(theboard):
						disply_Board(theboard)
						print('The game is a draw!')
						break
					else:
						turn = 'Player 1'
		if not reply():
			break
	
	
begin()