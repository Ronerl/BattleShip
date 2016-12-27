class battle_ship:
    def __init__(self, row, col):
        self.r = row
        self.c = col

    def createOwnBoard(self, YourBoard):
        timesToRun = 2
        if self.r > 7:
            direction = "down"
        else:
            direction = "up"
        while timesToRun > 0:
            if direction == 'up':
                for i in range(self.r, self.r + 3):
                    YourBoard[i][self.c] = "^"
                    if self.c > 7:
                        direction = "left"
                    else:
                        direction = "right"
            elif direction == "down":
                for i in range(self.r - 3, self.r):
                    YourBoard[i][self.c] = "^"
                    if self.c > 7:
                        direction = "left"
                    else:
                        direction = "right"
            elif direction == "left":
                for i in range(self.c - 3, self.c):
                    YourBoard[self.r][i] = "^"
            elif direction == "right":
                for i in range(self.c, self.c+3):
                    YourBoard[self.r][i] = "^"
