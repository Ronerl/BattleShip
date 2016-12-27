class battle_ship:
    def __init__(self, __row, __col):
        self.r = __row
        self.c = __col

    def createOwnBoard(self, YourBoard):
        if self.r > 7:
            direction = "down"
        else:
            direction = "up"
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
        return direction

    def createOwnBoard1(self, YourBoard, direction):
        if direction == "left":
            for i in range(self.c - 3, self.c):
                YourBoard[self.r][i] = "^"
        elif direction == "right":
            for j in range(self.c, self.c + 3):
                YourBoard[self.r][j] = "^"