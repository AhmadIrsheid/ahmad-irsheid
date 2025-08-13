class Piece:
    def __init__(self, color, position):
        self.color = color
        self.position = position  # (row, col)

    def get_valid_moves(self, board):
        return []

class Pawn(Piece):
    def get_valid_moves(self, board):
        moves = []
        r, c = self.position
        direction = -1 if self.color == "white" else 1

        # خطوة للأمام
        if 0 <= r + direction < 8 and board[r + direction][c] is None:
            moves.append((r + direction, c))

        # أكل القطع بشكل قطري
        for dc in [-1, 1]:
            nr, nc = r + direction, c + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                target = board[nr][nc]
                if target is not None and target.color != self.color:
                    moves.append((nr, nc))

        return moves

class Rook(Piece):
    def get_valid_moves(self, board):
        moves = []
        directions = [(1,0), (-1,0), (0,1), (0,-1)]
        r, c = self.position
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] is None:
                    moves.append((nr, nc))
                else:
                    if board[nr][nc].color != self.color:
                        moves.append((nr, nc))
                    break
                nr += dr
                nc += dc
        return moves

class Knight(Piece):
    def get_valid_moves(self, board):
        moves = []
        r, c = self.position
        steps = [(2,1), (2,-1), (-2,1), (-2,-1), (1,2), (1,-2), (-1,2), (-1,-2)]
        for dr, dc in steps:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                target = board[nr][nc]
                if target is None or target.color != self.color:
                    moves.append((nr, nc))
        return moves

class Bishop(Piece):
    def get_valid_moves(self, board):
        moves = []
        directions = [(1,1), (1,-1), (-1,1), (-1,-1)]
        r, c = self.position
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] is None:
                    moves.append((nr, nc))
                else:
                    if board[nr][nc].color != self.color:
                        moves.append((nr, nc))
                    break
                nr += dr
                nc += dc
        return moves

class Queen(Piece):
    def get_valid_moves(self, board):
        moves = []
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        r, c = self.position
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            while 0 <= nr < 8 and 0 <= nc < 8:
                if board[nr][nc] is None:
                    moves.append((nr, nc))
                else:
                    if board[nr][nc].color != self.color:
                        moves.append((nr, nc))
                    break
                nr += dr
                nc += dc
        return moves

class King(Piece):
    def get_valid_moves(self, board):
        moves = []
        directions = [(1,0), (-1,0), (0,1), (0,-1), (1,1), (1,-1), (-1,1), (-1,-1)]
        r, c = self.position
        for dr, dc in directions:
            nr, nc = r + dr, c + dc
            if 0 <= nr < 8 and 0 <= nc < 8:
                target = board[nr][nc]
                if target is None or target.color != self.color:
                    moves.append((nr, nc))
        return moves
