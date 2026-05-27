class GameState:

    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bN","bB","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wN","wB","wR"]
        ]
        self.white_move = True

    def make_move(self,move):
        if self.board[move.start_row][move.start_column] == "--":
            print("EMPTY BOARD")
            return

        if self.white_move == True and self.board[move.start_row][move.start_column][0] == 'w':
            self.board[move.end_row][move.end_column] = self.board[move.start_row][move.start_column]
            self.board[move.start_row][move.start_column] = "--"
            self.white_move = not self.white_move

        if self.white_move == False and self.board[move.start_row][move.start_column][0] == 'b':
            self.board[move.end_row][move.end_column] = self.board[move.start_row][move.start_column]
            self.board[move.start_row][move.start_column] = "--"
            self.white_move = not self.white_move



class Move:
    def __init__(self, start_move, end_move, board):
        self.start_row = start_move[0]
        self.start_column = start_move[1]
        self.end_row = end_move[0]
        self.end_column = end_move[1]
        self.piece_moved = board[self.start_row][self.start_column]
        self.piece_captured = board[self.end_row][self.end_column]