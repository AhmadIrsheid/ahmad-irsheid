
import random

class Player:
    def __init__(self, color, player_type="human"):
        self.color = color
        self.type = player_type

    def get_move(self, board):
        if self.type == "AI":
            print(f"🤖 ({self.color}) AI يفكر...")

            all_moves = []
            for row in range(8):
                for col in range(8):
                    piece = board.get_piece((row, col))
                    if piece and piece.color == self.color:
                        moves = piece.get_valid_moves(board.board)
                        for move in moves:
                            all_moves.append(((row, col), move))

            if all_moves:
                return random.choice(all_moves)
            else:
                print("🤖 AI ما قدر يتحرك.")
                return None, None

        # human input as before
        while True:
            try:
                move = input(f"{self.color} player's move (مثال: 6 0 4 0) أو 'exit' للخروج: ").strip()
                if move.lower() == "exit":
                    print("🚪 تم إنهاء اللعبة.")
                    exit()
                parts = move.split()
                if len(parts) != 4:
                    print("❌ لازم تدخل 4 أرقام: start_row start_col end_row end_col")
                    continue
                start_row, start_col, end_row, end_col = map(int, parts)
                if not all(0 <= x < 8 for x in [start_row, start_col, end_row, end_col]):
                    print("❌ كل الإحداثيات لازم تكون بين 0 و 7.")
                    continue
                return (start_row, start_col), (end_row, end_col)
            except ValueError:
                print("❌ دخلت إشي مش رقم! حاول مرة ثانية.")

