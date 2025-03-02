from tkinter import *
from customtkinter import *
from PIL import Image, ImageTk

def resize_method(imagePath, imageSize):
    currentImage = Image.open(imagePath)
    resizedImage = currentImage.resize(imageSize, Image.LANCZOS)  # Use LANCZOS for better quality
    return ImageTk.PhotoImage(resizedImage)  # Convert to Tkinter-compatible image


class TrainClass:
    def __init__(self, root):
        self.root = root
        self.root.wm_overrideredirect(True)
        self.frame_position()
        self.root.title("Face Recognition System")

        # Set root background to dark cyan (optional but improves UI)
        self.root.configure(bg="darkcyan")

        self.train_method()

    # Positioning the frame at the center of the screen
    def frame_position(self):
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Window dimensions
        window_width = 800
        window_height = 790

        # Calculate x and y positions to center the window
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    def train_method(self):
        # # Create the main frame that fills the entire window
        # self.main_frame = Frame(self.root, background="darkcyan")
        # self.main_frame.place(x=0, y=0, relheight=1, relwidth=1)  # Fill entire window

        # # Title Label
        # self.photo_sample_heading = Label(
        #     self.main_frame,
        #     text="Photo Sample Training",
        #     font=("Ubuntu", 18, "bold"),
        #     foreground="white",
        #     background="darkcyan",
        #     pady=10
        # )
        # self.photo_sample_heading.place(x=0, y=0, width=800, height=40)  # Position label in frame

        # # Back Button
        # self.back_button = CTkButton(
        #     self.main_frame, text="Back", fg_color="red",
        #     font=("Ubuntu", 12, "bold"), anchor="center", width=100, height=30
        # )
        # self.back_button.place(x=680, y=10)

       

         # first Image
        imagePath = "college_images/top1.jpg"
        imageSize = (420, 130)
        self.photoImage = resize_method(imagePath, imageSize)
        self.f_label = Label(self.root, image=self.photoImage)
        self.f_label.place(x=0, y=0, width=420, height=130)

        


if __name__ == "__main__":
    root = CTk()
    TrainClass(root)
    root.mainloop()
