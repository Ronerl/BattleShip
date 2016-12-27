class battle_ship:
    def __init__(self, __row, __col):
        self.r = __row
        self.c = __col
        self.l = None
        self.h = None
        self.p = {}

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
                        self.p.__setitem__(i, self.c)
                        if self.c > 7:
                            direction = "left"
                        else:
                            direction = "right"
                    else:
                        if self.check_avaibility(YourBoard, self.r + (length+1), self.c):
                            YourBoard[self.r + (length+1)][self.c] = "^"
                            self.p.__setitem__(self.r + (length+1), self.c)
                        else:
                            raise ValueError
            elif direction == "down":
                for i in range(self.r - length, self.r):
                    if self.check_avaibility(YourBoard, i, self.c):
                        YourBoard[i][self.c] = "^"
                        self.p.__setitem__(i, self.c)
                        if self.c > 7:
                            direction = "left"
                        else:
                            direction = "right"
                    else:
                        if self.check_avaibility(YourBoard, self.r -(length+1), self.c):
                            YourBoard[self.r -(length+1)][self.c] = "^"
                            self.p.__setitem__(self.r -(length+1), self.c)
                        else:
                            raise ValueError
        return direction

    # deploys some more ships.
    def createOwnBoard1(self, YourBoard, direction, length):
        if direction == "left":
            for i in range(self.c - length, self.c):
                if self.check_avaibility(YourBoard, self.r, i):
                    YourBoard[self.r][i] = "^"
                    self.p.__setitem__(self.r, i)
                else:
                    if self.check_avaibility(YourBoard, self.r, self.c -(length+1)):
                        YourBoard[self.r][self.c - (length+1)] = "^"
                        self.p.__setitem__(self.r, self.c - (length+1))
                    else:
                        raise ValueError
        elif direction == "right":
            for j in range(self.c, self.c + length):
                if self.check_avaibility(YourBoard, self.r, j):
                    YourBoard[self.r][j] = "^"
                    self.p.__setitem__(self.r, j)
                else:
                    if self.check_avaibility(YourBoard, self.r, self.c + (length+1)):
                        YourBoard[self.r][self.c + (length+1)] = "^"
                        self.p.__setitem__(self.r, self.c+(length+1))
                    else:
                        raise ValueError

    def re_decorate(self, YourBoard, sign):
        i = 0
        while i < len(self.p.keys()):
            YourBoard[self.p.keys()[i]][self.p.values()[i]] = sign
            i += 1




