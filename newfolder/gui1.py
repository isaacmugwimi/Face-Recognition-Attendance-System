import tkinter as tk
from tkinter import messagebox
import subprocess

def show_message():
    messagebox.showinfo("Message", "Hello from GUI 1!")

def open_gui2():
    root.destroy()  # Close GUI 1
    subprocess.Popen(["python", "gui2.py"])  # Launch GUI 2

root = tk.Tk()
root.title("GUI 1")
root.geometry("300x200")

tk.Button(root, text="Show Message", command=show_message).pack(pady=10)
tk.Button(root, text="Switch to GUI 2", command=open_gui2).pack(pady=10)

root.mainloop()