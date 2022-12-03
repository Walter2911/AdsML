class Data:
    def __init__(self, score=0):
        self.score = score

    def getScore(self):
        return self.score                                            # 221910312015(K.L.S.Akash)


class Scoreboard:

    def __init__(self, capacity=10):
        self.board = [None] * capacity
        self.size = 0

    def __getitem__(self, index):
        return self.board[index]

    def __str__(self):
        return "\n".join(str(self.board[j]) for j in range(self.size))   # 221910312015(K.L.S.Akash)

    def __add__(self, element):
        score = element
        good = self.size < len(self.board) or score > self.board[-1]

        if good:
            if self.size < len(self.board):
                self.size += 1
            j = self.size - 1
            while j > 0 and self.board[j - 1] < score:
                self.board[j] = self.board[j - 1]
                j -= 1
            self.board[j] = element


scoreboard = Scoreboard()
inputs = int(input("Enter no. of entries: "))

for i in range(inputs):
    data = Data(int(input("Enter the score: ")))                   # 221910312015(K.L.S.Akash)
    scoreboard.__add__(data.score)

print(f"Array after inputs: {scoreboard.board}")
for i in range(4, 9):
    print(f"{i + 1}th highest score is {scoreboard.__getitem__(i)}")

print(f"Top 10 scores are: \n{scoreboard.__str__()}")