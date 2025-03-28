from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from customtkinter import *
import cv2
import numpy as np


class Train:
    
    def __init__(self, root):
        self.root = root
        self.root.title("Images")
        self.frame_position()
        self.root.wm_overrideredirect(True)
        # self.root.transient(self.root.master)
        self.train_method()

        # self.root.mainloop()

    # Positioning the frame at the center of the screen
    def frame_position(self):
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Window dimensions
        window_width = 800
        window_height = 700

        # Calculate x and y positions to center the window
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2) -80
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

        # Explanation:
        # 1. (screen_height // 2) gets the midpoint of the screen vertically.
        # 2. (window_height // 2) gets half of the window's height.
        # 3. Subtracting them centers the window vertically.
        # 4. The additional "-80" shifts the window upward by 80 pixels.

    def train_method(self):

        # Title Label
        self.photo_sample_heading = Label(
            self.root,
            text="Photo Sample Training",
            font=("Ubuntu", 18, "bold"),
            foreground="white",
            background="darkcyan",
            pady=10,
        )

        self.photo_sample_heading.place(
            x=0, y=0, width=800, height=40
        )  # Position label in frame

        # Back Button
        self.back_button = CTkButton(
            self.root,
            text="Back",
            fg_color="red",
            bg_color="darkcyan",
            font=("Ubuntu", 15, "bold"),
            anchor="center",
            width=100,
            height=27,
            cursor="hand2",
            command=self.back_method,
        )
        self.back_button.place(x=680, y=6)

        """Loads and displays an image in the GUI."""
        # first image
        img1 = Image.open("college_images/top1.jpg").resize((250, 150))
        self.my_image1 = ImageTk.PhotoImage(
            img1
        )  # Store in self to prevent garbage collection

        self.img_label1 = Label(self.root, image=self.my_image1)
        self.img_label1.place(x=0, y=40, width=250, height=150)

        # second image
        img2 = Image.open("college_images/top2.jpeg").resize((300, 150))
        self.my_image2 = ImageTk.PhotoImage(img2)
        self.img_label2 = Label(
            self.root, image=self.my_image2, relief=GROOVE, bd=2, background="blue"
        )
        self.img_label2.place(x=250, y=40, width=300, height=150)

        # Third image
        img3 = Image.open("college_images/train.jpg").resize((250, 150))
        self.my_image3 = ImageTk.PhotoImage(img3)
        self.img_label3 = Label(self.root, image=self.my_image3)
        self.img_label3.place(x=550, y=40, width=250, height=150)

        """including the train data button which launches the opencv """
        buttonFrame = Frame(self.root, bg="darkcyan")
        buttonFrame.place(x=0, y=200, width=800, height=45)
        # Train Button
        self.train_data_button = CTkButton(
            buttonFrame,
            text="Train Data",
            fg_color="darkBlue",
            command=self.train_classifier,
            font=("Ubuntu", 15, "bold"),
            anchor="center",
            width=250,
            height=33,
            cursor="hand2",
        )
        self.train_data_button.pack(expand=True)

        # Background bottom Image
        img4 = Image.open("college_images/facialrecognition (1).png").resize((795, 450))
        self.my_image4 = ImageTk.PhotoImage(img4)
        self.img_label4 = Label(self.root, image=self.my_image4, background="blue")
        self.img_label4.place(x=0, y=245, width=800, height=455)

    def back_method(self):
        response = messagebox.askyesno(
            "Confirm", "Do you really want to quit?", parent=self.root
        )
        if response:
            self.root.destroy()

    def train_classifier(self):
        data_dir = "data"
        path = [os.path.join(data_dir, file) for file in os.listdir(data_dir)]
        faces = []
        ids = []
        for image in path:
            img = Image.open(image).convert("L")  # Convert Image to Grayscale
            image_np = np.array(img, "uint8")  # converting image to a numpy array
            id = int(os.path.split(image)[1].split(".")[1])

            faces.append(image_np)
            ids.append(id)
            cv2.imshow("Training", image_np)
            cv2.waitKey(1) == 13
        ids = np.array(ids)

        """============ Train the classifier and save ============"""
        classifier = cv2.face.LBPHFaceRecognizer_create()
        classifier.train(faces, ids)
        classifier.write("classifier.xml")
        cv2.destroyAllWindows()
        messagebox.showinfo("Result", "Training Datasets  Completed", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    app = Train(root)
    root.mainloop()
