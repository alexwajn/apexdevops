class TicTacToe:
    grid = []
    
    def __init__(self):
        for i in range(3):
            self.grid.append([' ', ' ', ' '])
    
    def insert_play(self, player):
        while True:
            play = input(f"This is player {player}'s turn. Enter the row and column of play. Index starts with 0! ")
            row = int(play[0])
            col = int(play[-1])
            if self.grid[row][col] == ' ':
                self.grid[row][col] = player
                break
            else: print("Place taken already!")
        self.print_grid()
    
    def print_grid(self):
        print("    COLUMN")
        print("    0  1  2")
        print(f"R 0 {self.grid[0][0]}| {self.grid[0][1]}| {self.grid[0][2]}")
        print("   "+"-"*8)
        print(f"O 1 {self.grid[1][0]}| {self.grid[1][1]}| {self.grid[1][2]}")
        print("   "+"-"*8)
        print(f"W 2 {self.grid[2][0]}| {self.grid[2][1]}| {self.grid[2][2]}")
    
    def check_win(self, player):
        if self.grid[0] == [player, player, player] or \
        self.grid[1] == [player, player, player] or \
        self.grid[2] == [player, player, player] or \
        (self.grid[0][0] == player and self.grid[1][0] == player and self.grid[2][0] == player) or \
        (self.grid[0][1] == player and self.grid[1][1] == player and self.grid[2][1] == player) or \
        (self.grid[0][2] == player and self.grid[1][2] == player and self.grid[2][2] == player) or \
        (self.grid[0][2] == player and self.grid[1][1] == player and self.grid[2][0] == player) or \
        (self.grid[0][0] == player and self.grid[1][1] == player and self.grid[2][2] == player):
            return False
        else: return True
    
    def is_play_avail(self):
        count = 0
        for row in self.grid:
            for col in row:
                if col == ' ': count += 1
        if count > 0: return True
        else: return False
    
    def game_loop(self):
        print("Tic Tac Toe game developed by Alex v0.1a")
        player = "X"
        self.print_grid()
        next_play = True
        while next_play:
            self.insert_play(player)
            next_play = self.check_win(player) and self.is_play_avail()
            winner = player
            if player == "X": player = "O"
            else: player = "X"
        if self.check_win(winner):
            print(f"Player {winner} won!")
        else: print("Nobody won this time!")
game = TicTacToe()
game.game_loop()
