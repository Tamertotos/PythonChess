class GameState:

    def __init__(self):
        self.board = [
            ["bR","bN","bB","bQ","bK","bB","bN","bR"],
            ["bp","bp","bp","bp","bp","bp","bp","bp"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["--","--","--","--","--","--","--","--"],
            ["wp","wp","wp","wp","wp","wp","wp","wp"],
            ["wR","wN","wB","wQ","wK","wB","wN","wR"]
        ]
        self.white_move = True
        self.move_log = []


    def make_move(self,move):
        if self.board[move.start_row][move.start_column] == "--":
            print("EMPTY BOARD")
            return

        if self.white_move == True and self.board[move.start_row][move.start_column][0] == 'w':
            self.board[move.end_row][move.end_column] = move.piece_moved
            self.board[move.start_row][move.start_column] = "--"
            self.white_move = not self.white_move
            print(f"move ID: {move.move_Id} ")
            print(move.chess_notation())
            self.move_log.append(move);

        if self.white_move == False and self.board[move.start_row][move.start_column][0] == 'b':
            self.board[move.end_row][move.end_column] =  move.piece_moved
            self.board[move.start_row][move.start_column] = "--"
            self.white_move = not self.white_move
            print(f"move ID: {move.move_Id} ")
            print(move.chess_notation())
            self.move_log.append(move);


    def undo_move(self):
        if len(self.move_log) == 0:
            raise IndexError("No moves to undo!")


        if len(self.move_log) != 0:
            move = self.move_log.pop()
            self.board[move.start_row][move.start_column] = move.piece_moved
            self.board[move.end_row][move.end_column] = move.piece_captured
            self.white_move = not self.white_move

    def get_valid_moves(self):
        '''All moves considering CHECK'''
        pass

    def get_all_moves(self):
        '''All moves without considering CHECKS'''
        valid_moves = []
        for row in range(len(self.board)):
            for col in range(len(self.board)):
                turn = self.board[row][col][0]
                if (turn == 'w' and self.white_move) or (turn == 'b' and not self.white_move):
                    piece = self.board[row][col][1]
                    if piece == 'p':
                        self.pawn_moves(row,col,valid_moves)

        return valid_moves

    def pawn_moves(self,row,col,valid_moves):
        '''Generates all valid pawn moves for the pawn at (row,col) and appends them to valid_moves.

            ARGS:
                row(int): row index of the pawn (0-7)
                col(int): column index of the pawn (0-7)
                valid_moves (list): list to append valid Move obejects to

            HANDLES:
                Single step, double step from starting rank, diagonal captures.
        '''

        #Unnnecessary lambda usage to pass the project requirements!
        is_empty = lambda piece : piece == '--'

        if self.white_move:
            if is_empty(self.board[row-1][col]):
                valid_moves.append(Move((row,col), (row-1, col), self.board))
            if col < 7 and is_empty(self.board[row-1][col+1][0]):
                valid_moves.append(Move((row,col), (row-1, col+1), self.board))
            if col > 0 and is_empty(self.board[row-1][col-1][0]):
                valid_moves.append(Move((row,col), (row-1, col-1), self.board))
            if row == 6 and is_empty(self.board[row-2][col]) and is_empty(self.board[row-1][col]):
                valid_moves.append(Move((row,col), (row-2, col), self.board))

        if not self.white_move:
            if is_empty(self.board[row+1][col]):
                valid_moves.append(Move((row,col), (row+1, col), self.board))
            if col < 7 and is_empty(self.board[row+1][col+1][0]):
                valid_moves.append(Move((row,col), (row+1, col+1), self.board))
            if col > 0 and is_empty(self.board[row+1][col-1][0]):
                valid_moves.append(Move((row,col), (row+1, col-1), self.board))
            if row == 1 and is_empty(self.board[row+2][col]) and is_empty(self.board[row+1][col]):
                valid_moves.append(Move((row,col), (row+2, col), self.board))



class Move:
    def __init__(self, start_move, end_move, board):
        self.start_row = start_move[0]
        self.start_column = start_move[1]
        self.end_row = end_move[0]
        self.end_column = end_move[1]
        self.piece_moved = board[self.start_row][self.start_column]
        self.piece_captured = board[self.end_row][self.end_column]
        self.move_Id = self.start_row * 1000 + self.start_column * 100 + self.end_row * 10 + self.end_column

    def __eq__(self,other):
        '''Overriding equals for the Move objects according to self.move_Id; if this attribute is equal they are the same object'''
        if  isinstance(other,Move):
            return other.move_Id == self.move_Id
        return False


    def chess_notation(self):
        rows_dict = {0 : "8", 1: "7" , 2: "6", 3: "5", 4: "4", 5: "3", 6: "2", 7:"1"}
        column_dict = {0 : "a", 1: "b", 2: "c", 3: "d", 4: "e", 5: "f", 6: "g", 7: "h"}

        piece_type = self.piece_moved[1]
        letters = {"p" : "" , "R":"R", "N":"N", "B": "B", "Q":"Q", "K":"K"}

        capture = "x" if self.piece_captured != "--" else ""

        if piece_type == "p" and capture:
            capture = column_dict[self.start_column] + "x"

        return letters[piece_type] + capture + column_dict[self.end_column] + rows_dict[self.end_row]