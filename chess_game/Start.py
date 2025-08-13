import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk  # تأكد من وجود مكتبة Pillow

def start_game(choice):
    import subprocess
    subprocess.run(["python3", "gui.py", choice])  # تمرير الاختيار للواجهة الرسومية
    root.destroy()

# نافذة البداية
root = tk.Tk()
root.title("شاشة البداية - شطرنج")
root.geometry("500x400")
root.configure(bg="#F0D9B5")

# شعار اللعبة
try:
    logo_img = Image.open("267242d9-7f81-4f72-b7b8-544f42727912.jpg")  # تأكد من وجود شعار
    logo_img = logo_img.resize((160, 160))
    logo_photo = ImageTk.PhotoImage(logo_img)
    tk.Label(root, image=logo_photo, bg="#F0D9B5").pack(pady=15)
except:
    tk.Label(root, text="♛ Chess Game ♛", font=("Arial", 28, "bold"), bg="#F0D9B5").pack(pady=25)

# اختيار نوع اللعب
tk.Label(root, text="اختر نمط اللعب", font=("Arial", 18), bg="#F0D9B5").pack(pady=10)

tk.Button(root, text="🧑‍🤝‍🧑 لاعبين", font=("Arial", 16), width=20,
          command=lambda: start_game("human")).pack(pady=10)

tk.Button(root, text="🤖 ضد AI", font=("Arial", 16), width=20,
          command=lambda: start_game("ai")).pack(pady=10)

root.mainloop()
