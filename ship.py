class battle_ship:
    def __init__(self, __row, __col):
        self.r = __row
        self.c = __col

    # checks whetever a spot is avaliable to place ships

    def check_avaibility(self, YourBoard, row, col):
        if YourBoard[row][col] == "^":
            print "no"
            return False
        else:
            print "yes"
            return True

    # Deploys the ships
    def createOwnBoard(self, YourBoard, length):
        if self.r > 7:
            direction = "down"
        else:
            direction = "up"
            if direction == 'up':
                for i in range(self.r, self.r + length):
                    if self.check_avaibility(YourBoard, i, self.c):
                        YourBoard[i][self.c] = "^"
                        if self.c > 7:
                            direction = "left"
                        else:
                            direction = "right"
                    else:
                        if self.check_avaibility(YourBoard, self.r + (length+1), self.c):
                            YourBoard[self.r-1][self.c] = "^"
                        else:
                            raise ValueError
            elif direction == "down":
                for i in range(self.r - length, self.r):
                    if self.check_avaibility(YourBoard, i, self.c):
                        YourBoard[i][self.c] = "^"
                        if self.c > 7:
                            direction = "left"
                        else:
                            direction = "right"
                    else:
                        if self.check_avaibility(YourBoard, self.r -(length+1), self.c):
                            YourBoard[self.r+1][self.c] = "^"
                        else:
                            raise ValueError
        return direction

    # deploys some more ships.
    def createOwnBoard1(self, YourBoard, direction, length):
        if direction == "left":
            for i in range(self.c - length, self.c):
                if self.check_avaibility(YourBoard, self.r, i):
                    YourBoard[self.r][i] = "^"
                else:
                    if self.check_avaibility(YourBoard, self.r, self.c -(length+1)):
                        YourBoard[self.r][self.c+1] = "^"
                    else:
                        raise ValueError
        elif direction == "right":
            for j in range(self.c, self.c + length):
                if self.check_avaibility(YourBoard, self.r, j):
                    YourBoard[self.r][j] = "^"
                else:
                    if self.check_avaibility(YourBoard, self.r, self.c + (length+1)):
                        YourBoard[self.r][self.c-1] = "^"
                    else:
                        raise ValueError
