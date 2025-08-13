from piece import Pawn, Rook, Knight, Bishop, Queen, King
from check_utils import is_in_check  # من ملف check_utils.py

class Board:
    def __init__(self):
        self.board = [[None]*8 for _ in range(8)]
        self.current_turn = "white"
        self.setup_board()

    def setup_board(self):
        for col in range(8):
            self.board[1][col] = Pawn("black", (1,col))
            self.board[6][col] = Pawn("white", (6,col))

        self.board[0][0] = Rook("black", (0,0))
        self.board[0][7] = Rook("black", (0,7))
        self.board[7][0] = Rook("white", (7,0))
        self.board[7][7] = Rook("white", (7,7))

        self.board[0][1] = Knight("black", (0,1))
        self.board[0][6] = Knight("black", (0,6))
        self.board[7][1] = Knight("white", (7,1))
        self.board[7][6] = Knight("white", (7,6))

        self.board[0][2] = Bishop("black", (0,2))
        self.board[0][5] = Bishop("black", (0,5))
        self.board[7][2] = Bishop("white", (7,2))
        self.board[7][5] = Bishop("white", (7,5))

        self.board[0][3] = Queen("black", (0,3))
        self.board[7][3] = Queen("white", (7,3))

        self.board[0][4] = King("black", (0,4))
        self.board[7][4] = King("white", (7,4))

    def move_piece(self, start, end):
        sr, sc = start
        er, ec = end
        piece = self.board[sr][sc]
        if piece is None:
            return False, "لا توجد قطعة هنا."

        if piece.color != self.current_turn:
            return False, "ليس دورك."

        valid_moves = piece.get_valid_moves(self.board)
        if end not in valid_moves:
            return False, "الحركة غير قانونية."

        # تجربة الحركة
        captured = self.board[er][ec]
        self.board[er][ec] = piece
        self.board[sr][sc] = None
        old_pos = piece.position
        piece.position = (er, ec)

        # بعد كل حركة ناجحة
    

        # تبديل الدور
        self.current_turn = "black" if self.current_turn == "white" else "white"
        return True, "✅ تمت الحركة"

    def is_king_captured(self, color):
        for row in self.board:
            for piece in row:
                if piece and piece.color == color and piece.__class__.__name__ == "King":
                    return False
        return True








