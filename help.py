from tkinter import *
from PIL import ImageTk, Image, ImageDraw


class Help:
    def __init__(self, root):
        self.root = root
        self.root.geometry("800x650+20+20")
        self.root.title("Face Recognition System")
        self.root.configure(background="darkblue")

        # System Title
        systemTitle = Label(
            self.root,
            text="HELP DESK  ",
            foreground="white",
            width=800,
            height=0,
            bg="blue",
            font=("Times new roman", 25, "bold"),
        )
        systemTitle.place(x=0, y=0, width=800, height=40)

        main_frame = Frame(self.root, bg="blue", borderwidth=2, height=600, width=800)
        main_frame.place(x=0, y=50, width=800, height=600)

        top_image = Image.open(r"college_images/help.jpeg").resize((800, 600))
        self.my_image = ImageTk.PhotoImage(top_image)

        top_image_label = Label(main_frame, image=self.my_image)
        top_image_label.place(x=0, y=0, height=600, width=800)

        developer_label = Label(
            top_image_label,
            text="Email: mugwimiisaac230@gmail.com",
            foreground="blue",
            width=400,
            height=0,
            bg="white",
            font=("Times new roman", 13, "bold"),
        )
        developer_label.place(x=240, y=150, width=300, height=30)


if __name__ == "__main__":
    root = Tk()
    obj = Help(root)
    root.mainloop()
