import socket, pickle, ship


# The game itself
def chooseRow():
    inOcean = True
    while inOcean:
        try:
            row = int(raw_input("Enter row\n")) - 1
        except ValueError:
            print "Please enter a number, not a letter!"
            continue
        if row >= 0 and row < 10:
            inOcean = False
            continue
        print "Enter a number within our ocean please"
    return row



def chooseCol():
    # Prevent letters
    inOcean = True
    while inOcean:
        try:
            col = int(raw_input("Enter col\n")) - 1
        except ValueError:
            print "Please enter a number, not a letter!"
            continue
        if col >= 0 and col < 10:
            inOcean = False
            continue
        print "Enter a number within our ocean please"
    return col



def createOwnBoard(YourBoard):
    ship1 = ship.battle_ship(chooseRow(), chooseCol())
    ship2 = ship.battle_ship(chooseRow(), chooseCol())
    direction = ship1.createOwnBoard(YourBoard)
    ship2.createOwnBoard1(YourBoard, direction)
    return YourBoard






def victoryChecker(Board):
    for i in range(len(Board)):
        for j in range(len(Board[i])):
            if Board[i][j] == "^":
                return False
    return True

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


def game(HisBoard):
    moves = []
    for turn in range(4):
        # Prevent errors here
        guess_row = guessRow()
        guess_row -= 1
        guess_col = guessCol()
        guess_col -= 1
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
                    moves.append("turn")
                    continue
            elif (HisBoard[guess_row][guess_col] == "X"):
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


def HisTurn(my_socket):
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
    return lost


# Game Methods End
def end(my_socket):
    my_socket.close()

#---------------main-----------------

    port = 8820
    ip = '172.22.18.23'
    my_socket = socket.socket()
    my_socket.connect((ip, port))
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
    my_socket.send(dataToSend)  # Send the board

    data = my_socket.recv(1024)  # Gets "Wait for me to choose"
    print data
    data = my_socket.recv(1024)  # Gets "I did it"
    print data
    HisBoard = my_socket.recv(1024)  # Gets board
    HisBoard = pickle.loads(HisBoard)
    print "\nRecived his board"
    data = my_socket.recv(1024)  # Gets the person who starts.
    print data
    if data == "You'll start!":
        while not victory:
            moves = game(HisBoard)
            data_string = pickle.dumps(moves)
            my_socket.send(data_string)
            if moves[-1] == "Won battle":
                break
            lost = HisTurn(my_socket)
            if lost:
                break
        end(my_socket)
    elif data == "I'll start!":
        while not victory:
            lost = HisTurn(my_socket)
            if lost:
                break
            moves = game(HisBoard)
            data_string = pickle.dumps(moves)
            my_socket.send(data_string)
        end(my_socket)
