## for play game in computer first mode, first click a button for starting the game. 

import random
import tkinter
from tkinter import *
from functools import partial
from tkinter import messagebox
from copy import deepcopy

board = [
    [' ', ' ', ' '],
    [' ', ' ', ' '],
    [' ', ' ', ' ']
    ]

player = 'X'
opponent = 'O'


def isMovesLeft(board) :

	for i in range(3) :
		for j in range(3) :
			if (board[i][j] == ' ') :
				return True
	return False


def evaluate(b) :

	for row in range(3) :	
		if (b[row][0] == b[row][1] and b[row][1] == b[row][2]) :	
			if (b[row][0] == player) :
				return 10
			elif (b[row][0] == opponent) :
				return -10


	for col in range(3) :
	
		if (b[0][col] == b[1][col] and b[1][col] == b[2][col]) :
		
			if (b[0][col] == player) :
				return 10
			elif (b[0][col] == opponent) :
				return -10


	if (b[0][0] == b[1][1] and b[1][1] == b[2][2]) :
	
		if (b[0][0] == player) :
			return 10
		elif (b[0][0] == opponent) :
			return -10

	if (b[0][2] == b[1][1] and b[1][1] == b[2][0]) :
	
		if (b[0][2] == player) :
			return 10
		elif (b[0][2] == opponent) :
			return -10


	return 0


def minimax(board, depth, isMax) :
    score = evaluate(board)
    
        
    if (score == 10) :
        return score
 

    if (score == -10) :
        return score
 

    if (isMovesLeft(board) == False) :
        return 0
 

    if (isMax) :    
        best = -1000
        
        for i in range(3) :        
            for j in range(3) :
                  

                if (board[i][j]==' ') :
                    board[i][j] = player    
                    best = max( best, minimax(board,
                                                  depth + 1,
                                                  not isMax) )                         
                    board[i][j] = ' '
        return best
 
    else :
        best = 1000
        

        #if depth <=1:
        for i in range(3) :        
            for j in range(3) :
                  

                if (board[i][j] == ' ') :
                    board[i][j] = opponent
                    best = min(best, minimax(board, depth + 1, not isMax))
                    board[i][j] = ' '
        return best
    

def findBestMove(board) :
	bestVal = -1000
	bestMove = (-1, -1)


	for i in range(3) :	
		for j in range(3) :
		

			if (board[i][j] == ' ') :
			

				board[i][j] = player
                
                # we can change the flase to true for game be intermediate
                # explained in text file in the reademe .pdf file.
				moveVal = minimax(board, 0, False)
				board[i][j] = ' '

				if (moveVal > bestVal) :			
					bestMove = (i, j)
					bestVal = moveVal

	return bestMove




sign = 0
global y 
y = 0
def get_text_pc(i, j, gb, l1, l2):
    global sign
    global y
    
    if y != 0:
        if board[i][j] == ' ':
            if sign % 2 == 0:
                l1.config(state=DISABLED)
                l2.config(state=ACTIVE)
                board[i][j] = "X"
            else:
                button[i][j].config(state=ACTIVE)
                l2.config(state=DISABLED)
                l1.config(state=ACTIVE)
                board[i][j] = "O" 
                
    button[i][j].config(text=board[i][j])        
    sign += 1
    y+= 1
    
    x = True
    if evaluate(board) == 10:
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif evaluate(board) == -10:
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif (not isMovesLeft(board)):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
   
    if(x):
        if sign % 2 != 0:
            move = findBestMove(board)
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc(move[0], move[1], gb, l1, l2)
             


sign = 0

def get_text_pc1(i, j, gb, l1, l2):
    global sign
    
    if board[i][j] == ' ':
        if sign % 2 == 0:
            l1.config(state=DISABLED)
            l2.config(state=ACTIVE)
            board[i][j] = "X"
        else:
            button[i][j].config(state=ACTIVE)
            l2.config(state=DISABLED)
            l1.config(state=ACTIVE)
            board[i][j] = "O" 
                
    button[i][j].config(text=board[i][j])        
    sign += 1
    
    x = True
    if evaluate(board) == 10:
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Player won the match")
    elif evaluate(board) == -10:
        gb.destroy()
        x = False
        box = messagebox.showinfo("Winner", "Computer won the match")
    elif (not isMovesLeft(board)):
        gb.destroy()
        x = False
        box = messagebox.showinfo("Tie Game", "Tie Game")
   
    if(x):
        if sign % 2 != 0:
            move = findBestMove(board)
            button[move[0]][move[1]].config(state=DISABLED)
            get_text_pc1(move[0], move[1], gb, l1, l2)
            



def gameboard_pc(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()
    
    
    
    
    
def gameboard_pc1(game_board, l1, l2):
    global button
    button = []
    for i in range(3):
        m = 3+i
        button.append(i)
        button[i] = []
        for j in range(3):
            n = j
            button[i].append(j)
            get_t = partial(get_text_pc1, i, j, game_board, l1, l2)
            button[i][j] = Button(
                game_board, bd=5, command=get_t, height=4, width=8)
            button[i][j].grid(row=m, column=n)
    game_board.mainloop()



def withpc(game_board):
	game_board.destroy()
	game_board = Tk()
	game_board.title("Tic Tac Toe")
	l1 = Button(game_board, text="Player : X", width=10)
	l1.grid(row=1, column=1)
	l2 = Button(game_board, text = "Computer : O",
				width = 10, state = DISABLED)
	
	l2.grid(row = 2, column = 1)
	gameboard_pc(game_board, l1, l2)
    
    
    
def withpc1(game_board):
	game_board.destroy()
	game_board = Tk()
	game_board.title("Tic Tac Toe")
	l1 = Button(game_board, text="Player : X", width=10)
	l1.grid(row=1, column=1)
	l2 = Button(game_board, text = "Computer : O",
				width = 10, state = DISABLED)
	
	l2.grid(row = 2, column = 1)
	gameboard_pc1(game_board, l1, l2)
    


def play():
	menu = Tk()
	menu.geometry("250x250")
	menu.title("Tic Tac Toe")
	wpc = partial(withpc, menu)
	wpl = partial(withpc1, menu)
    
	head = Button(menu, text = "---Welcome to game---",
				activeforeground = 'red',
				activebackground = "yellow", bg = "red",
				fg = "yellow", width = 500, font = 'summer', bd = 5)
	
	B1 = Button(menu, text = "computer first", command = wpc,
				activeforeground = 'red',
				activebackground = "yellow", bg = "red",
				fg = "yellow", width = 500, font = 'summer', bd = 5)
	
	B2 = Button(menu, text = "player first", command = wpl, activeforeground = 'red',
				activebackground = "yellow", bg = "red", fg = "yellow",
				width = 500, font = 'summer', bd = 5)
	
	B3 = Button(menu, text = "Exit", command = menu.quit, activeforeground = 'red',
				activebackground = "yellow", bg = "red", fg = "yellow",
				width = 500, font = 'summer', bd = 5)
	head.pack(side = 'top')
	B1.pack(side = 'top')
	B2.pack(side = 'top')
	B3.pack(side = 'top')
	menu.mainloop()



play()

