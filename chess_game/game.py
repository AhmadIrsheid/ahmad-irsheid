
from board import Board
from player import Player
from check_utils import is_checkmate

class GameManager:
    def __init__(self):
        self.board = Board()
        self.players = [
            Player("white", player_type="human"),
            Player("black", player_type="AI")
        ]
        self.current_player_index = 0

    def start_game(self):
        print("🎮 بدأت لعبة الشطرنج!")
        print("✏️ للتحكم: اكتب 4 أرقام مثل: 6 0 4 0")
        print("🚪 للخروج من اللعبة: اكتب exit")

        while True:
            self.board.print_board()
            current_player = self.players[self.current_player_index]
            print(f"🔁 دور اللاعب: {current_player.color}")

            from_pos, to_pos = current_player.get_move(self.board)

            if from_pos is None or to_pos is None:
                print(f"🚫 {current_player.color} لا يمكنه التحرك. انتهت اللعبة.")
                break

            piece = self.board.get_piece(from_pos)
            if piece is None:
                print("❌ ما في قطعة في هاي الخانة! حاول مرة ثانية.")
                continue

            if piece.color != current_player.color:
                print("❌ هاي مش قطعتك! بدك تحرك قطعة من نفس لونك.")
                continue

            success, message = self.board.move_piece(from_pos, to_pos)
            if not success:
                print(message)
                continue

            # تحقق من نهاية اللعبة
            if is_checkmate(self.board.board, self.players[self.current_player_index].color):
                print(f"🏁 اللاعب {self.players[1 - self.current_player_index].color} فاز بكش مات!")
                self.board.print_board()
                break

            self.current_player_index = 1 - self.current_player_index

if __name__ == "__main__":
    game = GameManager()
    game.start_game()


