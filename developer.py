from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image, ImageDraw
from tkinter import messagebox
import cv2
import os
import csv
from tkinter import filedialog


class Developer:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1100x670+20+20")
        self.root.title("Face Recognition System")
        self.root.configure(background="darkblue")

        # System Title
        systemTitle = Label(
            self.root,
            text="DEVELOPER",
            foreground="white",
            width=1100,
            height=0,
            bg="blue",
            font=("Times new roman", 25, "bold"),
        )
        systemTitle.place(x=0, y=0, width=1100, height=40)

        main_frame = Frame(self.root, bg="blue", borderwidth=2, height=600, width=540)
        main_frame.place(x=0, y=50, width=1100, height=600)

        top_image = Image.open(r"college_images/dev.jpg").resize((600, 600))
        self.my_image = ImageTk.PhotoImage(top_image)

        top_image_label = Label(main_frame, image=self.my_image)
        top_image_label.place(x=0, y=0, height=600, width=600)

        left_frame = Frame(main_frame, bg="white", borderwidth=2, height=600, width=480)
        left_frame.place(x=610, y=0)

        developer_details = Label(
            left_frame,
            text="Hello, \nmy name is Isaac.\n I am a full stack developer.",
            foreground="darkblue",
            bg="white",
            font=("Times new roman", 15, "bold"),
        )

        developer_details.place(x=0, y=0, height=200, width=280)

        developer_image = Image.open(r"college_images/developer2.jpg").resize(
            (200, 200)
        )

        """making the image circular"""
        mask = Image.new("L", (200, 200), 0)  # Create a blank black image
        draw = ImageDraw.Draw(mask)
        draw.ellipse((0, 0, 200, 200), fill=255)  # Draw a white circle

        # Apply the mask to the image
        circular_image = Image.new(
            "RGBA", (200, 200), (0, 0, 0, 0)
        )  # Transparent background
        circular_image.paste(developer_image, (0, 0), mask)  # Paste image using mask

        self.dev_image = ImageTk.PhotoImage(circular_image)

        developer_image_label = Label(
            left_frame,
            image=self.dev_image,
            background="blue",
            bd=1,
            relief=GROOVE,
        )

        developer_image_label.place(x=260, y=0, height=210, width=210)

        bottom_image = Image.open(r"college_images/developer.jpg").resize((470, 375))
        self.my_bottom_image = ImageTk.PhotoImage(bottom_image)

        bottom_image_label = Label(left_frame, image=self.my_bottom_image, bg="blue")
        bottom_image_label.place(x=0, y=215, height=380, width=480)


if __name__ == "__main__":
    root = Tk()
    obj = Developer(root)
    root.mainloop()
