# ♟️ Chess Game with GUI

A complete Chess game built in Python using **Tkinter** for the graphical interface.  
The game supports **Player vs Player** and **Player vs AI** modes, with full chess rules including **Castling**, **Check**, and **Checkmate**.

---

## 🚀 Features
- **Two Game Modes**: 
  - Player vs Player
  - Player vs AI (simple AI logic with random valid moves)
- **Special Moves**:
  - Castling
  - Pawn promotion
  - Check & Checkmate detection
- **Graphical Interface**:
  - Interactive chessboard with colored highlights for moves and captures
  - Start screen with game mode selection
- **Customizable**:
  - Easy to modify AI logic for stronger opponents
  - Adjustable board colors and design

---

## 📸 Screenshots

**Start Screen**
![Start Screen](assets/start_screen.png)

**Gameplay**
![Gameplay](assets/gameplay.png)

---

## 🛠️ Installation
1. Clone the repository:
```bash
git clone https://github.com/ahmad-irsheid/chess_game.git
cd ChessGame





Install dependencies:

bash
Copy
Edit
pip install pillow
Run the game:

bash
Copy
Edit
python gui.py
📂 Project Structure
bash
Copy
Edit
ChessGame/
├── board.py        # Manages board state, moves, and rules
├── piece.py        # Piece classes (Pawn, Rook, Knight, Bishop, Queen, King)
├── player.py       # Player class for handling player turns
├── game.py         # Game logic manager (if using terminal version)
├── gui.py          # Tkinter-based graphical interface
├── logo.png        # Logo for start screen
└── README.md       # Project documentation
🤖 AI Behavior
The AI currently:

Looks for possible captures first

If no capture is available, plays a random valid move

Note: You can upgrade the AI by implementing chess algorithms like Minimax with Alpha-Beta Pruning.

📜 License
This project is licensed under the MIT License - feel free to modify and use it.

Author: Ahmad Rami Irsheid

🇸🇦 النسخة العربية
♟️ لعبة الشطرنج بواجهة رسومية
لعبة شطرنج متكاملة مكتوبة بلغة Python باستخدام مكتبة Tkinter للواجهة الرسومية.
تدعم اللعب بين لاعبين أو ضد الذكاء الاصطناعي (AI)، مع تطبيق كامل لقوانين الشطرنج بما في ذلك التبييت و كش الملك و كش مات.

🚀 المميزات
طورين للعب:

لاعب ضد لاعب

لاعب ضد AI (ذكاء اصطناعي بسيط)

حركات خاصة:

التبييت (Castling)

ترقية البيدق

التحقق من كش وكش مات

واجهة رسومية تفاعلية:

لوحة شطرنج ملونة مع تمييز الحركات والأكل

شاشة بداية لاختيار وضع اللعب

قابلة للتطوير:

إمكانية تحسين الذكاء الاصطناعي

تعديل ألوان اللوحة وتصميمها

📥 التثبيت
نسخ المستودع:

bash
Copy
Edit
git clone https://github.com/ahmad-irsheid/chess_game.git
cd ChessGame
تثبيت المكتبات المطلوبة:

bash
Copy
Edit
pip install pillow
تشغيل اللعبة:

bash
Copy
Edit
python gui.py

