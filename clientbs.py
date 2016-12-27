import socket, pickle
"""Errors: 
bad input crashes everything
bad guesses count

TEST

"""
####The game itself
def chooseRow():
	inOcean = True
	global Splace
	while inOcean:
		try:
			Splace = int(raw_input("Enter start point\n"))
		except ValueError:
			print "Please enter a number, not a letter!"
			continue
		if Splace >= 0 and Splace < 10:
			inOcean = False
			continue
		print "Enter a number within our ocean please"
	global Eplace
	inOcean = True
	while inOcean:
		try:
			Eplace = int(raw_input("Enter end point\n"))
		except ValueError:
			print "Please enter a number, not a letter!"
			continue
		if Eplace >= 0 and Eplace < 10:
			inOcean = False
			continue
		print "Enter a number within our ocean please"
	
	global Cplace
	inOcean = True
	while inOcean:
		try:
			Cplace = int(raw_input("Enter collumn:\n"))
		except ValueError:
			print "Please enter a number, not a letter!"
			continue
		if Cplace >= 0 and Cplace < 10:
			inOcean = False
			continue
		print "Enter a number within our ocean please"
def chooseCol():
#Prevent letters
	inOcean = True
	global Splace
	while inOcean:
		try:
			Splace = int(raw_input("Enter start point\n"))
		except ValueError:
			print "Please enter a number, not a letter!"
			continue
		if Splace >= 0 and Splace < 10:
			inOcean = False
			continue
		print "Enter a number within our ocean please"
	global Eplace
	inOcean = True
	while inOcean:
		try:
			Eplace = int(raw_input("Enter end point\n"))
		except ValueError:
			print "Please enter a number, not a letter!"
			continue
		if Eplace >= 0 and Eplace < 10:
			inOcean = False
			continue
		print "Enter a number within our ocean please"
	
	global Rplace
	inOcean = True
	while inOcean:
		try:
			Rplace = int(raw_input("Enter row:\n"))
		except ValueError:
			print "Please enter a number, not a letter!"
			continue
		if Rplace >= 0 and Rplace < 10:
			inOcean = False
			continue
		print "Enter a number within our ocean please"

def createOwnBoard(YourBoard):
	timesToRun = 2
	while timesToRun > 0:
		choice = raw_input("R for vertical ship, C for horizontal!\n")
		if choice.lower() == 'c':
			chooseRow()
			for num in range(min(Splace, Eplace), max(Splace, Eplace)):
				YourBoard[num][Cplace] = "^"
			timesToRun -= 1
		elif choice.lower() == 'r':
			chooseCol()
			for num in range(min(Splace, Eplace), max(Splace, Eplace)):
				YourBoard[Rplace][num] = "^"
			timesToRun -= 1
		else:
			print "Please enter a valid letter"
	return YourBoard

def victoryChecker(Board):
	for i in range(len(Board)):
		for j in range(len(Board[i])):
			if Board[i][j] == "^":
				return False
	return True		
global victory
victory = False	
def game(HisBoard):
	moves = []
	for turn in range(4):
	#Prevent errors here
		guess_row = int(raw_input("Guess Row:\n"))
		guess_col = int(raw_input("Guess Col:\n"))
		if HisBoard[guess_row][guess_col] == "^":
			print "\nCongratulations! You hit a battleship!\n"
			moves.append("Hit")
			HisBoard[guess_row][guess_col] = "!"
			if victoryChecker(HisBoard):
				print "\nCongratulations! You won the battle!\n"
				moves.append("Won battle")
				victory = True
				break
			elif turn == 3:
				print "\nOpponents turn\n"
				moves.append("Turn")
				continue
		elif HisBoard[guess_row][guess_col] == "!":
			print "You guessed that one already."
			moves.append("twice")
			if turn == 3:
				print "\nOpponents turn\n"
				moves.append("Turn")
				continue
		else:
			if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
				print "Oops, that's not even in the ocean."
				moves.append("Out")
				if turn == 3:
					print "\nOpponents turn\n"
					client_socket.send("\nYour turn")
					continue
			elif(HisBoard[guess_row][guess_col] == "X"):
				print "\nYou guessed that one already.\n"
				moves.append("twice")
			else:
				print "\nYou missed the battleship!\n"
				moves.append("missed")
				HisBoard[guess_row][guess_col] = "X"
				if turn == 3:
					print "\nOpponents turn\n"
					moves.append("turn")
					continue
	return moves
	
	
def print_board(board):
	for row in board:
		print " ".join(row)

def HisTurn():
	global lost
	lost = False
	data = my_socket.recv(1024)
	data = pickle.loads(data)
	print data
	for item in data:
		item = item.lower()
		if item == "hit":
			print "\nYour ship was hurt"
		elif item == "won battle":
			print "\nYou lost the battle"
			lost = True
		elif item == "missed":
			print "\nHe missed your ship"
		elif item == "twice":
			print "\nHe shot the same place twice, what an idiot"
		elif item == "turn":
			print "\nIt's your turn now!"
###### Game Methods End
def end():
	my_socket.close()

port = 8820
ip = '172.17.2.88'
my_socket = socket.socket()
my_socket.connect((ip,port))
messg = my_socket.recv(1024)
tempMesg = raw_input(messg)
my_socket.send(tempMesg)
data_arr = my_socket.recv(1024)
MyBoard = pickle.loads(data_arr)



print_board(MyBoard)
print "\n This is your board! Now it's time to create some ships!"

MyBoard = createOwnBoard(MyBoard)
print "\nThis is your board now:\n"
print_board(MyBoard)
raw_input("\nPress any key to continue!\n")
print "Sending board to server.... Please wait\n"
dataToSend = pickle.dumps(MyBoard)
my_socket.send(dataToSend)#Send the board

data = my_socket.recv(1024) #Gets "Wait for me to choose"
print data
data = my_socket.recv(1024) #Gets "I did it"
print data
HisBoard = my_socket.recv(1024) #Gets board
HisBoard = pickle.loads(HisBoard)
print "\nRecived his board"
data = my_socket.recv(1024) #Gets the person who starts.
print data
if data == "You'll start!":
	while not victory:
		moves = game(HisBoard)
		data_string = pickle.dumps(moves)
		my_socket.send(data_string)
		if moves[-1] == "Won battle":
			break
		HisTurn()
		if lost:
			break
	end()
elif data == "I'll start!":
	while not victory:
		HisTurn()
		if lost:
			break
		moves = game(HisBoard)
		data_string = pickle.dumps(moves)
		my_socket.send(data_string)
	end()
