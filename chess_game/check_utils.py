def find_king(board, color):
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece and piece.color == color and piece.__class__.__name__ == "King":
                return (r, c)
    return None

def is_in_check(board, color):
    king_pos = find_king(board, color)
    if not king_pos:
        return False
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece and piece.color != color:
                moves = piece.get_valid_moves(board)
                if king_pos in moves:
                    return True
    return False

def is_checkmate(board, color):
    if not is_in_check(board, color):
        return False
    for r in range(8):
        for c in range(8):
            piece = board[r][c]
            if piece and piece.color == color:
                original_pos = (r, c)
                valid_moves = piece.get_valid_moves(board)
                for move in valid_moves:
                    captured = board[move[0]][move[1]]
                    board[move[0]][move[1]] = piece
                    board[r][c] = None
                    piece.position = move
                    still_in_check = is_in_check(board, color)
                    board[r][c] = piece
                    board[move[0]][move[1]] = captured
                    piece.position = original_pos
                    if not still_in_check:
                        return False
    return True
