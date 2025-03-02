import tkinter as tk
import subprocess

def open_gui1():
    root.destroy()  # Close GUI 2
    subprocess.Popen(["python", "gui1.py"])  # Launch GUI 1

root = tk.Tk()
root.title("GUI 2")
root.geometry("300x200")

tk.Button(root, text="Switch to GUI 1", command=open_gui1).pack(pady=10)

root.mainloop()
