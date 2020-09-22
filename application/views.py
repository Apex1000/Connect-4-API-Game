from flask import render_template,request,redirect,url_for,Response
from application import app
import os,json
import uuid
import numpy as np
from .models import db,Game

ROW = 6
COLUMN = 7

def jsonconvert(log):
    items=[]
    for i in log:
        item={
            "id": i.id,
            "move":i.move
            }
        items.append(item)
    return items

def game_board():
	board = np.zeros((ROW,COLUMN))
	return board

board = game_board()
turn = 0
game_end = False
def turns():
    global turn
    turn+=1
    turn=turn%2

def boards(player, move):
    place = True
    i=0
    while(place):
        if i>=6:
            return False
        if move>=7:
            return False
        if board[i][move]==0:
            board[i][move]=player
            place=False
        else:
            i+=1
    return True
def checking_winner(board, piece):
	# Check horizontal locations for win
	for i in range(COLUMN-3):
		for j in range(ROW):
			if board[j][i] == piece and board[j][i+1] == piece and board[j][i+2] == piece and board[j][i+3] == piece:
				return True

	# Check vertical locations for win
	for i in range(COLUMN):
		for j in range(ROW-3):
			if board[j][i] == piece and board[j+1][i] == piece and board[j+2][i] == piece and board[j+3][i] == piece:
				return True

	# Check positively sloped diaganols
	for i in range(COLUMN-3):
		for j in range(ROW-3):
			if board[j][i] == piece and board[j+1][i+1] == piece and board[j+2][i+2] == piece and board[j+3][i+3] == piece:
				return True

	# Check negatively sloped diaganols
	for i in range(COLUMN-3):
		for j in range(3, ROW):
			if board[j][i] == piece and board[j-1][i+1] == piece and board[j-2][i+2] == piece and board[j-3][i+3] == piece:
				return True

def end_game():
    global game_end
    game_end = True

def response(data,sta):
    if game_end:
        global board,turn 
        turn = 0
        board = game_board()
    response = app.response_class(
        response=json.dumps(data),
        status=sta,
        mimetype='application/json'
    )
    return response
@app.route('/')
def index():
    data = {"Start New Game":"/game"}
    print (board)
    sta = 200
    return response(data,sta)
@app.route('/game')
def game():
    data =request.json
    mv = str(data['player'])+" "+str(data['move'])
    gm = Game(id= uuid.uuid4().hex,move=str(mv))
    db.session.add(gm)
    db.session.commit()
    if data['move']>7:
        data = {"error":"InValid Move"}
        sta = 404
        return response(data,sta)
    #Player 1 
    if turn == 0:
        if data["player"] == "Yellow":
            move = data['move']
            val = (boards(1,move))
            print (val)
            if val:
                turns()
                if checking_winner(board, 1):
                    data = {"Winner":"Yellow"}
                    end_game()
                    sta = 200
                    return response(data,sta)
            else:
                data = {"error":"InValid Move"}
                sta = 404
                return response(data,sta)
        else:
            data = {"error":"InValid User"}
            sta = 401
            return response(data,sta)
    #Player 2
    else:
        if data["player"] == "Red":
            move = data['move']
            val = (boards(2,move))
            print (val)
            if val:
                turns()
                if checking_winner(board, 2):
                    data = {"Winner":"Red"}
                    sta = 200
                    return response(data,sta)
            else:
                data = {"error":"InValid Move"}
                sta = 404
                return response(data,sta)
        else:
            data = {"error":"InValid User"}
            sta = 401
            return response(data,sta)
    print (board)
    sta = 200
    return response(data,sta)


@app.route('/lgg')
def log():
    om = Game.query.all()
    data = jsonconvert(om)
    sta = 200
    return response(data,sta)
