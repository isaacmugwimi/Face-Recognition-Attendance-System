from PIL import Image, ImageTk
from tkinter import Tk, Label, Button
from customtkinter import *


def resize_method(imagePath, imageSize):
    currentImage = Image.open(imagePath)
    resizedImage = currentImage.resize(imageSize)
    return ImageTk.PhotoImage(resizedImage)


class Face_Recognition_System:

    def mainMethod(self):

        # first Image
        imagePath = "college_images/top1.jpg"
        imageSize = (420, 130)
        self.photoImage = resize_method(imagePath, imageSize)
        self.f_label = Label(self.root, image=self.photoImage)
        self.f_label.place(x=0, y=0, width=420, height=130)

        # second Image
        imagePath = "college_images/facialrecognition.png"
        imageSize = (420, 130)
        self.photoImage1 = resize_method(imagePath, imageSize)
        self.f_label = Label(self.root, image=self.photoImage1)
        self.f_label.place(x=420, y=0, width=420, height=130)

        # Third Image
        imagePath = "college_images/top2.jpeg"
        imageSize = (420, 130)
        self.photoImage2 = resize_method(imagePath, imageSize)
        self.f_label = Label(self.root, image=self.photoImage2)
        self.f_label.place(x=840, y=0, width=420, height=130)

        # Back ground Image
        imagePath = "college_images/wp2551980.jpg"
        imageSize = (1260, 710)
        self.bgPhotoImage3 = resize_method(imagePath, imageSize)
        self.bgimagelabel = Label(
            self.root,
            image=self.bgPhotoImage3,
        )
        self.bgimagelabel.place(x=0, y=130, width=1260, height=710)

        # System Title
        self.systemTitle = CTkLabel(
            self.bgimagelabel,
            text="FACE RECOGNITION ATTENDANCE SYSTEM SOFTWARE",
            text_color="red",
            width=1260,
            height=50,
            fg_color="white",
            font=("ubuntu", 30, "bold"),
        )
        self.systemTitle.place(
            x=-2,
            y=-2,
        )

        # Student Details Button
        imagePath = "college_images/student.jpg"
        imageSize = (180, 180)
        self.photoImage4 = resize_method(imagePath, imageSize)

        self.studentButton1 = Button(
            self.bgimagelabel,
            image=self.photoImage4,
            width=180,
            height=180,
            cursor="hand2",
            border=None,
        )
        self.studentButton1.place(x=120, y=100)

        # Student Button text
        self.studentBtn1text = Button(
            self.bgimagelabel,
            text="Student Details",
            cursor="hand2",
            border=None,
            height=50,
            bg="darkblue",
            foreground="white",
            font=("ubuntu", 13, "bold"),
            activebackground="blue",
            activeforeground="white",
        )
        self.studentBtn1text.place(x=120, y=280, width=186, height=30)

        # Face Detector Button
        imagePath = "college_images/face_detector1.jpg"
        imageSize = (180, 180)
        self.photoImage5 = resize_method(imagePath, imageSize)

        self.faceDetectorButton = Button(
            self.bgimagelabel,
            image=self.photoImage5,
            width=180,
            height=180,
            cursor="hand2",
            border=None,
        )
        self.faceDetectorButton.place(x=400, y=100)

        # Face Detector Button text
        self.faceDetectorBtn1text = Button(
            self.bgimagelabel,
            text="Face Detector",
            cursor="hand2",
            border=None,
            height=50,
            bg="darkblue",
            foreground="white",
            font=("ubuntu", 13, "bold"),
            activebackground="blue",
            activeforeground="white",
        )
        self.faceDetectorBtn1text.place(x=400, y=280, width=186, height=30)

        # Attendance Button
        imagePath = "college_images/attendace.jpg"
        imageSize = (180, 180)
        self.photoImage6 = resize_method(imagePath, imageSize)

        self.attendaceButton1 = Button(
            self.bgimagelabel,
            image=self.photoImage6,
            width=180,
            height=180,
            cursor="hand2",
            border=None,
        )
        self.attendaceButton1.place(x=690, y=100)

        # Attendance Button text
        self.attendanceBtn1text = Button(
            self.bgimagelabel,
            text="Attendance",
            cursor="hand2",
            border=None,
            height=50,
            bg="darkblue",
            foreground="white",
            font=("ubuntu", 13, "bold"),
            activebackground="blue",
            activeforeground="white",
        )
        self.attendanceBtn1text.place(x=690, y=280, width=186, height=30)

        # Help Desk Button
        imagePath = "college_images/helpdesk.jpg"
        imageSize = (180, 180)
        self.photoImage7 = resize_method(imagePath, imageSize)

        self.helpDeskButton1 = Button(
            self.bgimagelabel,
            image=self.photoImage7,
            width=180,
            height=180,
            cursor="hand2",
            border=None,
        )
        self.helpDeskButton1.place(x=970, y=100)

        # Help Desk Button text
        self.helpDeskBtn1text = Button(
            self.bgimagelabel,
            text="Help Desk",
            cursor="hand2",
            border=None,
            height=50,
            bg="darkblue",
            foreground="white",
            font=("ubuntu", 13, "bold"),
            activebackground="blue",
            activeforeground="white",
        )
        self.helpDeskBtn1text.place(x=970, y=280, width=186, height=30)

        # Train Data Button
        imagePath = "college_images/train.jpg"
        imageSize = (180, 180)
        self.photoImage8 = resize_method(imagePath, imageSize)

        self.trainDataButton1 = Button(
            self.bgimagelabel,
            image=self.photoImage8,
            width=180,
            height=180,
            cursor="hand2",
            border=None,
        )
        self.trainDataButton1.place(x=120, y=370)

        # Train Data Button  text
        self.trainDataBtn1text = Button(
            self.bgimagelabel,
            text="Train Data",
            cursor="hand2",
            border=None,
            height=50,
            bg="darkblue",
            foreground="white",
            font=("ubuntu", 13, "bold"),
            activebackground="blue",
            activeforeground="white",
        )
        self.trainDataBtn1text.place(x=120, y=550, width=186, height=30)

        # Photos Button
        imagePath = "college_images/photos.jpg"
        imageSize = (180, 180)
        self.photoImage9 = resize_method(imagePath, imageSize)

        self.photosButton = Button(
            self.bgimagelabel,
            image=self.photoImage9,
            width=180,
            height=180,
            cursor="hand2",
            border=None,
        )
        self.photosButton.place(x=400, y=370)

        # Photos Button text
        self.photosBtn1text = Button(
            self.bgimagelabel,
            text="Photos",
            cursor="hand2",
            border=None,
            height=50,
            bg="darkblue",
            foreground="white",
            font=("ubuntu", 13, "bold"),
            activebackground="blue",
            activeforeground="white",
        )
        self.photosBtn1text.place(x=400, y=550, width=186, height=30)

        # Developer Button
        imagePath = "college_images/developer.jpg"
        imageSize = (180, 180)
        self.photoImage10 = resize_method(imagePath, imageSize)

        self.developerButton1 = Button(
            self.bgimagelabel,
            image=self.photoImage10,
            width=180,
            height=180,
            cursor="hand2",
            border=None,
        )
        self.developerButton1.place(x=690, y=370)

        # Developer Button text
        self.developerBtn1text = Button(
            self.bgimagelabel,
            text="Developer",
            cursor="hand2",
            border=None,
            height=50,
            bg="darkblue",
            foreground="white",
            font=("ubuntu", 13, "bold"),
            activebackground="blue",
            activeforeground="white",
        )
        self.developerBtn1text.place(x=690, y=550, width=186, height=30)

        # Exit Button
        imagePath = "college_images/exit.jpg"
        imageSize = (180, 180)
        self.photoImage11 = resize_method(imagePath, imageSize)

        self.exitButton1 = Button(
            self.bgimagelabel,
            image=self.photoImage11,
            width=180,
            height=180,
            cursor="hand2",
            border=None,
        )
        self.exitButton1.place(x=970, y=370)

        # Exit Button text
        self.exitBtn1text = Button(
            self.bgimagelabel,
            text="Exit",
            cursor="hand2",
            border=None,
            height=50,
            bg="darkblue",
            foreground="white",
            font=("ubuntu", 13, "bold"),
            activebackground="blue",
            activeforeground="white",
        )
        self.exitBtn1text.place(x=970, y=550, width=186, height=30)

    def __init__(self, root):
        self.root = root
        self.root.geometry("1260x790+0+0")
        self.root.title("Face Recognition System")
        self.mainMethod()


if __name__ == "__main__":
    root = CTk()
    obj = Face_Recognition_System(root)
    root.mainloop()
