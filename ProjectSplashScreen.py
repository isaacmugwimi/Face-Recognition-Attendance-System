from tkinter import *

import time
from tkinter.ttk import Progressbar

from Login import Login


def frame_position():
    # Get screen width and height
    screen_width = splash_root.winfo_screenwidth()
    screen_height = splash_root.winfo_screenheight()

    # Window dimensions
    window_width = 430
    window_height = 300

    # Calculate x and y positions to center the window
    x_position = (screen_width // 2) - (window_width // 2)
    y_position = (screen_height // 2) - (window_height // 2) - 140
    splash_root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

splash_root = Tk()
splash_root.config()
# splash_root.geometry('430x300+550+230')
splash_root.title('Splash Screen')
splash_root.overrideredirect(True)
frame_position() # Positioning the frame at the center of the screen




def bar():
    splash_label3 = Label(frame, text='Loading', bg='#15191C', fg='#9AC72F', font=('Helvetica', 12))
    splash_label3.place(x=0, y=255)
    splash_label_dot = Label(frame, text='...', bg='#15191C', fg='#9AC72F', font=('Helvetica', 15))
    splash_label_dot.place(x=60, y=255)

    bar = Progressbar(frame, orient=HORIZONTAL, length=435)
    bar.place(x=0, y=280)
    percent = StringVar()
    percent_label = Label(frame, textvariable=percent, fg='#9AC72F', bg='#15191C', font=('Helvetica', 12))
    percent_label.place(x=80, y=255)

    r = 0
    for i in range(100):
        bar['value'] = r
        percent.set(str(int((r / 100) * 100)) + '%')
        frame.update_idletasks()
        time.sleep(0.03)
        r = r + 1
    splash_root.destroy()
    Login()
frame = Frame(splash_root, width=430, height=300, background='#15191C')
frame.place(x=0, y=0)

splash_label1 = Label(frame, text='Smart', font=('Helvetica', 30, 'bold'),
                      background='#15191C', foreground='#9AC72F')
splash_label1.place(x=50, y=80)

splash_label2 = Label(frame, text='Attendance System', font=('Helvetica', 25),
                      background='#15191C', foreground='#9AC72F')
splash_label2.place(x=130, y=120)

# button = customtkinter.CTkButton(frame, text_color='#15191C', text='Get Started', border_width=0, height=25,
# width=120, cursor='hand2', command=bar, font=('Helvetica', 13), fg_color='#9AC72F', corner_radius=15,
# hover_color='#FBD71D')
button = Button(frame, fg='#15191C', text='Get Started', border=0, height=1, width=10, cursor='hand2', command=bar,
                font=('Helvetica', 12), bg='#9AC72F', activebackground='#FBD71D', activeforeground='#9AC72F')
button.place(x=160, y=205)


def main_window():
    if __name__ == "__main__":
        Login()


# splash_root.after(500, main_window)

splash_root.mainloop()
