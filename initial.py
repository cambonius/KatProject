import tkinter as tk
from datetime import datetime

LOG_FILE = "log.txt"

def log_timestamp(label):
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")
    with open(LOG_FILE, "a") as f:
        f.write(f"{label}: {timestamp}\n")
    print(f"Logged: {label} at {timestamp}")

root = tk.Tk()
root.title("Timestamp Logger")

# Row 1: A–M
letters = [chr(i) for i in range(ord('A'), ord('N'))]  # A to M

frame1 = tk.Frame(root)
frame1.pack(pady=10)

for letter in letters:
    tk.Button(frame1, text=letter, width=6,
              command=lambda l=letter: log_timestamp(l)
    ).pack(side="left", padx=3)

# Row 2: name1–name9
names = [f"name{i}" for i in range(1, 10)]

frame2 = tk.Frame(root)
frame2.pack(pady=10)

for name in names:
    tk.Button(frame2, text=name, width=8,
              command=lambda n=name: log_timestamp(n)
    ).pack(side="left", padx=3)

root.mainloop()
