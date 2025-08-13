import tkinter as tk
from tkinter import messagebox
from board import Board
import random

class ChessGUI:
    LIGHT = "#F0D9B5"
    DARK = "#B58863"
    HIGHLIGHT_HUMAN_MOVE = "#F7EC7D"
    ATTACK_HUMAN = "#0AB819"
    HIGHLIGHT_AI_MOVE = "#27C1B2"
    ATTACK_AI = "#FF5555"
    SELECT = "#FAA937"
    SIZE = 60

    def __init__(self, root, vs_ai=False):
        self.root = root
        self.root.title("لعبة الشطرنج")
        self.board = Board()
        self.selected = None
        self.vs_ai = tk.BooleanVar(value=vs_ai)

        self.frame = tk.Frame(root)
        self.frame.pack(padx=10, pady=10)

        self.canvas = tk.Canvas(self.frame, width=8*self.SIZE, height=8*self.SIZE)
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)

        self.msg = tk.Label(root, text="", font=("Arial", 14), bg="#ddd")
        self.msg.pack(fill="x")

        ctrl_frame = tk.Frame(root)
        ctrl_frame.pack(pady=5)

        self.reset_btn = tk.Button(ctrl_frame, text="🔁 إعادة اللعبة", command=self.reset_game)
        self.reset_btn.pack(side="left", padx=5)

        self.draw_board()
        self.update_pieces()

        self.ai_turn = False
        self.root.after(100, self.ai_move_if_needed)

    def draw_board(self):
        for r in range(8):
            for c in range(8):
                x0, y0 = c * self.SIZE, r * self.SIZE
                color = self.LIGHT if (r + c) % 2 == 0 else self.DARK
                self.canvas.create_rectangle(x0, y0, x0 + self.SIZE, y0 + self.SIZE,
                                             fill=color, tags=f"square_{r}_{c}")

    def update_pieces(self):
        self.canvas.delete("piece")
        for r in range(8):
            for c in range(8):
                piece = self.board.board[r][c]
                if piece:
                    symbol = self.get_symbol(piece)
                    x = c * self.SIZE + self.SIZE / 2
                    y = r * self.SIZE + self.SIZE / 2
                    self.canvas.create_text(x, y, text=symbol,
                                            font=("Segoe UI Symbol", 32),
                                            tags=("piece", f"{r}_{c}"))
        self.canvas.tag_raise("piece")

    def on_click(self, event):
        if self.vs_ai.get() and self.board.current_turn == "black":
            self.msg.config(text="⏳ انتظر دور AI...")
            return

        row = int(event.y // self.SIZE)
        col = int(event.x // self.SIZE)

        if self.selected is None:
            piece = self.board.board[row][col]
            if piece and piece.color == self.board.current_turn:
                self.selected = (row, col)
                moves = piece.get_valid_moves(self.board.board)

                self.reset_colors()

                for mr, mc in moves:
                    target = self.board.board[mr][mc]
                    if target is None:
                        self.canvas.itemconfig(f"square_{mr}_{mc}", fill=self.HIGHLIGHT_HUMAN_MOVE)
                    else:
                        self.canvas.itemconfig(f"square_{mr}_{mc}", fill=self.ATTACK_HUMAN)

                sr, sc = self.selected
                self.canvas.itemconfig(f"square_{sr}_{sc}", fill=self.SELECT)
                self.msg.config(text=f"اختر مكان للتحريك من {self.selected}")
            else:
                self.msg.config(text="❌ اختر قطعة من دورك فقط.")
        else:
            moved, message = self.board.move_piece(self.selected, (row, col))
            self.selected = None
            self.reset_colors()
            self.update_pieces()

            if moved:
                self.msg.config(text="✅ تمت الحركة بنجاح.")
                self.check_end()

                if self.vs_ai.get() and self.board.current_turn == "black":
                    self.ai_turn = True
                    self.msg.config(text="🤖 دور AI...")
                    self.root.after(700, self.ai_move_if_needed)
            else:
                self.msg.config(text=f"❌ {message}")

    def reset_colors(self):
        for r in range(8):
            for c in range(8):
                base_color = self.LIGHT if (r + c) % 2 == 0 else self.DARK
                self.canvas.itemconfig(f"square_{r}_{c}", fill=base_color)

    def ai_move_if_needed(self):
        if not self.ai_turn:
            return

        moves = []
        capture_moves = []

        for r in range(8):
            for c in range(8):
                piece = self.board.board[r][c]
                if piece and piece.color == "black":
                    valid = piece.get_valid_moves(self.board.board)
                    for move in valid:
                        target = self.board.board[move[0]][move[1]]
                        if target is not None and target.color == "white":
                            capture_moves.append(((r, c), move))
                        else:
                            moves.append(((r, c), move))

        if capture_moves:
            start, end = random.choice(capture_moves)
        elif moves:
            start, end = random.choice(moves)
        else:
            self.finish_game("لا مزيد من الحركات، انتهت اللعبة.")
            return

        self.reset_colors()
        sr, sc = start
        er, ec = end

        self.canvas.itemconfig(f"square_{sr}_{sc}", fill=self.SELECT)

        target_piece = self.board.board[er][ec]
        if target_piece is None:
            self.canvas.itemconfig(f"square_{er}_{ec}", fill=self.HIGHLIGHT_AI_MOVE)
        else:
            self.canvas.itemconfig(f"square_{er}_{ec}", fill=self.ATTACK_AI)

        self.update_pieces()

        self.root.after(700, lambda: self.do_ai_move(start, end))

    def do_ai_move(self, start, end):
        moved, message = self.board.move_piece(start, end)
        self.ai_turn = False
        self.reset_colors()
        self.update_pieces()
        if moved:
            self.msg.config(text="🤖 AI قام بالحركة.")
            self.check_end()
        else:
            self.msg.config(text=f"🤖 خطأ في حركة AI: {message}")

    def check_end(self):
        if self.board.is_king_captured("black"):
            self.finish_game("🏁 الأبيض فاز! الملك الأسود تم أسره.")
        elif self.board.is_king_captured("white"):
            self.finish_game("🏁 الأسود فاز! الملك الأبيض تم أسره.")

    def finish_game(self, text):
        self.msg.config(text=text)
        messagebox.showinfo("نهاية اللعبة", text)

    def get_symbol(self, piece):
        symbols = {
            "Pawn": "♙" if piece.color == "white" else "♟",
            "Rook": "♖" if piece.color == "white" else "♜",
            "Knight": "♘" if piece.color == "white" else "♞",
            "Bishop": "♗" if piece.color == "white" else "♝",
            "Queen": "♕" if piece.color == "white" else "♛",
            "King": "♔" if piece.color == "white" else "♚",
        }
        return symbols[type(piece).__name__]

    def reset_game(self):
        self.board = Board()
        self.selected = None
        self.ai_turn = False
        self.msg.config(text="اللعبة أعيدت. دور الأبيض يبدأ.")
        self.reset_colors()
        self.update_pieces()

# --------------------------------------------------
# ✅ شاشة البداية

if __name__ == "__main__":
    from PIL import Image, ImageTk

    def start_game(vs_ai):
        start_root.destroy()
        root = tk.Tk()
        gui = ChessGUI(root, vs_ai=vs_ai)
        root.mainloop()

    start_root = tk.Tk()
    start_root.title("ابدأ اللعبة")
    start_root.geometry("400x450")

    try:
        image = Image.open("267242d9-7f81-4f72-b7b8-544f42727912.jpg")
        image = image.resize((200, 200))
        logo = ImageTk.PhotoImage(image)
        logo_label = tk.Label(start_root, image=logo)
        logo_label.image = logo
        logo_label.pack(pady=20)
    except Exception as e:
        print("⚠️ لم يتم تحميل الشعار:", e)

    label = tk.Label(start_root, text="اختر نمط اللعب", font=("Arial", 18))
    label.pack(pady=10)

    btn_ai = tk.Button(start_root, text="اللعب ضد AI", font=("Arial", 14), width=20, command=lambda: start_game(True))
    btn_ai.pack(pady=5)

    btn_human = tk.Button(start_root, text="لاعب ضد لاعب", font=("Arial", 14), width=20, command=lambda: start_game(False))
    btn_human.pack(pady=5)

    start_root.mainloop()
