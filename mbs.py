import socket, pickle
from random import randint

# ------------------------GameStart

#### Battle Start

p1board = []
p2board = []

for x in range(10):
    p1board.append(["O"] * 10)
for x in range(10):
    p2board.append(["0"] * 10)


######Game Methods
def print_board(board):
    for row in board:
        print " ".join(row)


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
    # Prevent letters
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


def victoryChecker(Board):
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            if Board[i][j] == "^":
                return False
    return True


def whoStarts():
    num = randint(1, 2)
    return num


######Game Methods End

def guessCol():
    while True:
        try:
            guess_col = int(raw_input("Guess col:\n"))
            return guess_col
        except ValueError:
            print "Please enter a number, not a letter!\n"


def guessRow():
    while True:
        try:
            guess_row = int(raw_input("Guess row:\n"))
            return guess_row
        except ValueError:
            print "Please enter a number, not a letter!\n"

global victory
victory = False


def game(p1board):
    moves = []
    for turn in range(4):
        guess_row = guessRow()
        guess_row -= 1
        guess_col = guessCol()
        guess_col -= 1
        if p1board[guess_row][guess_col] == "^":
            print "\nCongratulations! You hit a battleship!\n"
            moves.append("Hit")
            p1board[guess_row][guess_col] = "!"
            if victoryChecker(p1board):
                print "\nCongratulations! You won the battle!\n"
                moves.append("Won battle")
                victory = True
                break
            elif turn == 3:
                print "\nOpponents turn\n"
                moves.append("Turn")
                continue
        elif p1board[guess_row][guess_col] == "!":
            print "You guessed that one already."
            moves.append("twice")
            if turn == 3:
                print "\nOpponents turn\n"
                client_socket.send("\nYour turn")
                continue
        else:
            if (guess_row < 0 or guess_row > 9) or (guess_col < 0 or guess_col > 9):
                print "Oops, that's not even in the ocean."
                moves.append("Out")
                if turn == 3:
                    print "\nOpponents turn\n"
                    client_socket.send("\nYour turn")
                    continue
            elif (p1board[guess_row][guess_col] == "X"):
                print "\nYou guessed that one already.\n"
                moves.append("twice")
            else:
                print "\nYou missed the battleship!\n"
                moves.append("missed")
                p1board[guess_row][guess_col] = "X"
                if turn == 3:
                    print "\nOpponents turn\n"
                    moves.append("turn")
                    continue
    return moves


def HisTurn():
    global lost
    lost = False
    data = client_socket.recv(1024)
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


# ---------------------------GameEnd
def end():
    client_socket.close()
    server_socket.close()


port = 8820
server_socket = socket.socket()
server_socket.bind(('0.0.0.0', port))

server_socket.listen(5)

(client_socket, client_address) = server_socket.accept()
print "connected!\n"
client_socket.send("Ready to start! Press any key to start!")
client_socket.recv(1024)
##########
data_string = pickle.dumps(p1board)
client_socket.send((data_string))
p2board = client_socket.recv(1024)
p2board = pickle.loads(p2board)
client_socket.send("Wait for me to choose!")
print_board(p1board)
print "\n This is your board! Now it's time to create some ships!"
createOwnBoard(p1board)
client_socket.send("I did it!")
data_string = pickle.dumps(p2board)
client_socket.send(data_string)
print_board(p1board)
print "\nThis is your board!\n"
num = whoStarts()
print num
if num == 1:
    print "He starts"
    client_socket.send("You'll start!")
    while not victory:
        HisTurn()
        if lost:
            break
        moves = game(p2board)
        data_string = pickle.dumps(moves)
        client_socket.send(data_string)
    end()
elif num == 2:
    print "You start"
    client_socket.send("I'll start!")
    while not victory:
        moves = game(p2board)
        data_string = pickle.dumps(moves)
        client_socket.send(data_string)
        if moves[-1] == "Won battle":
            break
        HisTurn()
        if lost:
            break
    end()
