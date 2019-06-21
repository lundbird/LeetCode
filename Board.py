class Board:
    def __init__(self):
        self.B = [None,None,None] #2d array as the board
        #X = 1, None = empty, O = 0
        for i in range(3):
            self.B[i] = ["-","-","-"]
        

    def add_token(self, r, c, val):
        self.B[r][c] = val

    def print_board(self):
        for arr in self.B:
            for i in range(len(arr)):
                print(arr[i],end="")
                if i < 2:
                    print("|",end="")
            print() #newline
        print()
    
    def is_full(self):
        for arr in self.B:
            for val in arr:
                if val == "-":
                    return False
        return True

    def make_move(self): #AI method
        #AI is always 0 user is X
        if self.is_full():
            raise ValueError("No available move")
        for r in range(len(self.B)):
            for c in range(len(self.B[r])):
                if self.B[r][c] == "-":
                    self.add_token(r,c,"O")
                    return

    def play_game(self):
        while not self.is_full():
            #get user input
            r = int(input("Enter row:"))
            c = int(input("Enter col:"))

            self.add_token(r,c,'X')
            if self.is_full():
                self.print_board()
                return
            self.make_move()
            self.print_board()

    
if __name__ == "__main__":
    test = Board()
    test.print_board()
    print(test.is_full())
    # test.add_token(2,1,"X")
    # test.print_board()
    # print(test.is_full())

    test.play_game()

    # while True:
    #     test.make_move()
    #     test.print_board()

    