import tkinter
from tkinter import messagebox
from PIL import Image, ImageTk
from tkinter import Tk, Label, Button, Toplevel
from customtkinter import *
import tk
from Student import Student
from train import Train
from attendance import Attendance
from developer import Developer
from help import Help
from time import strftime
from datetime import datetime
from face_recognitor import Face_Detector



def resize_method(imagePath, imageSize):
    currentImage = Image.open(imagePath)
    resizedImage = currentImage.resize(imageSize, Image.LANCZOS)
    return ImageTk.PhotoImage(resizedImage)


class FaceRecognitionSystem:

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
        imageSize = (1260, 700)
        self.bgPhotoImage3 = resize_method(imagePath, imageSize)
        self.bgimagelabel = Label(
            self.root,
            image=self.bgPhotoImage3, borderwidth=2, relief=GROOVE
        )
        self.bgimagelabel.place(x=0, y=130, width=1260, height=800)

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
            x=0,
            y=0,
        )

        """ Adding time method"""
        def time_method():
            string =strftime("%H:%M:%S %p")
            time_label.config(text = string)
            time_label.after(1000, time_method)

        time_label = Label(self.bgimagelabel, font=("times new roman", 17, "bold"), background="white", foreground="blue")
        time_label.place(x=10, y=0, width=135, height=50)
        time_method()

        # Student Details Button
        imagePath = "college_images/student.jpg"
        imageSize = (180, 180)
        self.photoImage4 = resize_method(imagePath, imageSize)

        self.studentButton1 = Button(
            self.bgimagelabel, command=self.student_details_method,
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
            command=self.student_details_method,
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
            border=None, command=self.face_detector_method
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
            activeforeground="white",command=self.face_detector_method
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
            border=None, command=self.attendance_method
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
            activeforeground="white", command=self.attendance_method
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
            command=self.help_method
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
            command=self.help_method
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
            command=self.train_data_method

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
            command=self.train_data_method
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
            command=self.open_image
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
            command=self.open_image
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
            command=self.developer_method,
            border=None,
        )
        self.developerButton1.place(x=690, y=370)

        # Developer Button text
        self.developerBtn1text = Button(
            self.bgimagelabel,
            text="Developer",
            cursor="hand2",
            border=None,
            command=self.developer_method,
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
            border=None,command=self.exit_method
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
            activeforeground="white", command=self.exit_method
        )
        self.exitBtn1text.place(x=970, y=550, width=186, height=30)

    def __init__(self):
        self.root = Tk()
        self.root.wm_overrideredirect(True)
        # self.root.geometry("1260x790+0+0")
        self.frame_position()
        self.root.title("Face Recognition System")
        self.root.grab_set()
        self.mainMethod()
        self.root.mainloop()


    # Positioning the frame at the center of the screen
    def frame_position(self):
        # Get screen width and height
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Window dimensions
        window_width = 1260
        window_height = 750

        # Calculate x and y positions to center the window
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)-100
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")




    # **********************************Functions buttons*********************************

    def student_details_method(self):
        self.student = Toplevel(self.root)
        Student(self.student)

    def face_detector_method(self):
        self.face_detector = Toplevel(self.root)
        Face_Detector(self.face_detector)

        # self.developer = Toplevel(self.root)
        # ImageTester(self.developer)

    def open_image(self):
        os.startfile("data")

    def train_data_method(self):
        self.train_window =Toplevel(self.root)
        Train(self.train_window)
        
        
    def attendance_method(self):
        self.attendance = Toplevel(self.root)
        Attendance(self.attendance)

    def developer_method(self):
        self.developer = Toplevel(self.root)
        Developer(self.developer)

        


    def help_method(self):
        self.help = Toplevel(self.root)
        Help(self.help)


    def exit_method(self):
        self.exit_method = messagebox.askyesno("Face Recognition", "Are you sure to exit this project?")
        if self.exit_method>0:
            self.root.destroy()
        else:
            return



if __name__ == "__main__":
        FaceRecognitionSystem()
    
