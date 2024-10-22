from tkinter import W, Frame, ttk
from tkinter.font import Font
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from tkinter import Entry, Tk, Label, Button, LabelFrame
from customtkinter import CTk, CTkLabel, CTkFrame


def resize_method(imagePath, imageSize):
    currentImage = Image.open(imagePath)
    resizedImage = currentImage.resize(imageSize)
    return ImageTk.PhotoImage(resizedImage)


class Student:
    def mainMethod(self):
        # first Image
        imagePath = "college_images/students1.jpg"
        imageSize = (420, 130)
        self.photoImage = resize_method(imagePath, imageSize)
        self.f_label = Label(self.window, image=self.photoImage)
        self.f_label.place(x=0, y=0, width=420, height=130)

        # second Image
        imagePath = "college_images/facialrecognition.png"
        imageSize = (420, 130)
        self.photoImage1 = resize_method(imagePath, imageSize)
        self.f_label = Label(self.window, image=self.photoImage1)
        self.f_label.place(x=420, y=0, width=420, height=130)

        # Third Image
        imagePath = "college_images/students2.jpg"
        imageSize = (420, 130)
        self.photoImage2 = resize_method(imagePath, imageSize)
        self.f_label = Label(self.window, image=self.photoImage2)
        self.f_label.place(x=840, y=0, width=420, height=130)

        # Background Image
        imagePath = "college_images/wp2551980.jpg"
        imageSize = (1260, 710)
        self.bgPhotoImage3 = resize_method(imagePath, imageSize)
        self.bgimagelabel = Label(
            self.window,
            image=self.bgPhotoImage3,
        )
        self.bgimagelabel.place(x=0, y=130, width=1260, height=710)

        # System Title
        self.systemTitle = CTkLabel(
            self.bgimagelabel,
            text="STUDENT MANAGEMENT SYSTEM",
            text_color="white",
            width=1260,
            height=40,
            fg_color="darkblue",
            font=("ubuntu", 25, "bold"),
        )
        self.systemTitle.place(
            x=-2,
            y=-2,
        )

        # creating the Main Frame inside the "self.bgImagelabel"
        self.student_Main_Frame = CTkFrame(
            self.bgimagelabel,
            fg_color="darkblue",
            border_width=2,
            width=1240,
            height=600,
        )

        self.student_Main_Frame.place(
            x=10,
            y=45,
        )
        frameFont = Font(family="ubuntu", size=13, weight="bold")

        # **************************************************************************************************
        # left Frame
        self.studentInfoFrame = LabelFrame(
            self.student_Main_Frame,
            text="Student Information",
            font=frameFont,
            bg="darkblue",
            fg="magenta",
        )
        self.studentInfoFrame.place(x=10, y=10, width=530, height=580)

        imageSize = (510, 140)
        imagePath = "college_images/students4.jpeg"
        self.studentphoto1 = resize_method(imagePath, imageSize)

        self.studentLabelPhoto = Label(
            self.studentInfoFrame, image=self.studentphoto1, bd=None
        )
        self.studentLabelPhoto.grid(row=0, column=0, padx=5)

        # Current Course Information
        self.courseInfoFrame = LabelFrame(
            self.studentInfoFrame,
            text="Current Course Information",
            fg="green",
            border=3,
            font=("ubuntu", 10, "bold"),
        )
        self.courseInfoFrame.grid(
            row=1,
            column=0,
            pady=20,
            padx=0,
        )

        # courseInfoFrame details
        self.departmentLabel = Label(
            self.courseInfoFrame, text="Department:", font=("ubuntu", 10)
        )
        self.departmentLabel.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky=W)

        self.departmentCombobox = Combobox(
            self.courseInfoFrame,
            values=["Select department", "BScIT", "BBIT", "CS", "SE"],
            state="readonly",
            foreground="darkblue",
            background="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        self.departmentCombobox.current(0)
        self.departmentCombobox.grid(row=0, column=1, padx=(0, 10), pady=(10, 0))

        self.coursesLabel = Label(
            self.courseInfoFrame, text="Courses:", font=("ubuntu", 10)
        )
        self.coursesLabel.grid(row=0, column=2, padx=(20, 0), pady=(10, 0), sticky=W)

        self.coursesCombobox = Combobox(
            self.courseInfoFrame,
            values=["Select Courses", "BScIT", "BBIT", "CS", "SE"],
            state="readonly",
            foreground="darkblue",
            background="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        self.coursesCombobox.current(0)
        self.coursesCombobox.grid(row=0, column=3, padx=(0, 10), pady=(10, 0))

        self.yearLabel = Label(
            self.courseInfoFrame,
            text="Year:",
            font=("ubuntu", 10),
        )
        self.yearLabel.grid(row=1, column=0, padx=(10, 0), pady=(10, 10), sticky=W)

        self.yearCombobox = Combobox(
            self.courseInfoFrame,
            values=["Select Year", "I", "II", "III", "IV"],
            state="readonly",
            foreground="darkblue",
            font=("ubuntu", 10, "bold"),
        )

        self.yearCombobox.current(0)
        self.yearCombobox.grid(row=1, column=1, padx=(0, 10), pady=(10, 10), sticky=W)

        self.semesterLabel = Label(
            self.courseInfoFrame, text="Semester:", font=("ubuntu", 10)
        )
        self.semesterLabel.grid(row=1, column=2, padx=(20, 0), pady=(10, 10), sticky=W)

        self.semesterCombobox = Combobox(
            self.courseInfoFrame,
            values=["Select Semester", "I", "II", "III"],
            state="readonly",
            foreground="darkblue",
            background="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        self.semesterCombobox.current(0)
        self.semesterCombobox.grid(row=1, column=3, padx=(0, 10), pady=(10, 10))

        # **********************************

        # student class information frame

        self.studentClassInfoFrame = LabelFrame(
            self.studentInfoFrame,
            text="Student Class Information Frame",
            fg="green",
            border=3,
            font=("ubuntu", 10, "bold"),
        )
        self.studentClassInfoFrame.grid(
            row=2,
            column=0,
        )

        self.studentIdNoLabel = Label(
            self.studentClassInfoFrame,
            text="Id No:",
            font=("ubuntu", 10),
        )
        self.studentIdNoLabel.grid(row=0, column=0, padx=(10, 0), pady=(5, 5), sticky=W)

        self.idNoEntry = Entry(
            self.studentClassInfoFrame,
            width=25,
            fg="darkblue",
            borderwidth=0,
            bg="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        self.idNoEntry.grid(
            row=0, column=1, padx=(0, 10), pady=(5, 5), ipady=2, sticky=W
        )

        self.studentNameLabel = Label(
            self.studentClassInfoFrame,
            text="Name:",
            font=("ubuntu", 10),
        )
        self.studentNameLabel.grid(row=0, column=2, padx=(10, 0), pady=(5, 5), sticky=W)

        self.studentNameLabelEntry = Entry(
            self.studentClassInfoFrame,
            width=25,
            borderwidth=0,
            bg="darkgrey",
            fg="darkblue",
            font=("ubuntu", 10, "bold"),
        )
        self.studentNameLabelEntry.grid(
            row=0,
            column=3,
            padx=(0, 15),
            pady=(5, 5),
            ipady=2,
        )

        self.genderLabel = Label(
            self.studentClassInfoFrame,
            text="Gender:",
            font=("ubuntu", 10),
        )
        self.genderLabel.grid(row=1, column=0, padx=(10, 0), pady=(5, 5), sticky=W)

        self.genderCombobox = Combobox(
            self.studentClassInfoFrame,
            values=["Male", "Female", "Other"],
            width=25,
            state="readonly",
            foreground="darkblue",
            font=("ubuntu", 8, "bold"),
        )
        self.genderCombobox.current(0)
        self.genderCombobox.grid(
            row=1, column=1, padx=(0, 10), pady=(5, 5), ipady=2, sticky=W
        )

        self.dobLabel = Label(
            self.studentClassInfoFrame,
            text="DOB:",
            font=("ubuntu", 10),
        )
        self.dobLabel.grid(row=1, column=2, padx=(10, 0), pady=(5, 5), sticky=W)

        self.dobLabelEntry = Entry(
            self.studentClassInfoFrame,
            width=25,
            borderwidth=0,
            bg="darkgrey",
            fg="darkblue",
            font=("ubuntu", 10, "bold"),
        )

        self.dobLabelEntry.grid(
            row=1,
            column=3,
            padx=(0, 15),
            pady=(5, 5),
            ipady=2,
        )

        self.emailLabel = Label(
            self.studentClassInfoFrame,
            text="Email:",
            font=("ubuntu", 10),
        )
        self.emailLabel.grid(row=2, column=0, padx=(10, 0), pady=(5, 5), sticky=W)

        self.emailEntry = Entry(
            self.studentClassInfoFrame,
            width=25,
            fg="darkblue",
            borderwidth=0,
            bg="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        self.emailEntry.grid(
            row=2, column=1, padx=(0, 10), pady=(5, 5), ipady=2, sticky=W
        )

        self.phoneNoLabel = Label(
            self.studentClassInfoFrame,
            text="Phone:",
            font=("ubuntu", 10),
        )
        self.phoneNoLabel.grid(row=2, column=2, padx=(10, 0), pady=(5, 5), sticky=W)

        self.phoneNoLabelEntry = Entry(
            self.studentClassInfoFrame,
            width=25,
            borderwidth=0,
            bg="darkgrey",
            fg="darkblue",
            font=("ubuntu", 10, "bold"),
        )

        self.phoneNoLabelEntry.grid(
            row=2,
            column=3,
            padx=(0, 15),
            pady=(5, 5),
            ipady=2,
        )

        self.locationLabel = Label(
            self.studentClassInfoFrame,
            text="Location:",
            font=("ubuntu", 10),
        )
        self.locationLabel.grid(row=3, column=0, padx=(10, 0), pady=(5, 5), sticky=W)

        self.locationEntry = Entry(
            self.studentClassInfoFrame,
            width=25,
            borderwidth=0,
            bg="darkgrey",
            fg="darkblue",
            font=("ubuntu", 10, "bold"),
        )

        self.locationEntry.grid(
            row=3,
            column=1,
            padx=(0, 15),
            pady=(5, 5),
            ipady=2,
        )

        self.photosample = ttk.Radiobutton(
            self.studentClassInfoFrame, text="Take Photo Sample", value="Yes"
        )
        self.photosample.grid(row=4, column=0, padx=10, columnspan=2, pady=(0, 10))

        self.photosample1 = ttk.Radiobutton(
            self.studentClassInfoFrame, text="No Photo Sample", value="Yes"
        )
        self.photosample1.grid(row=4, column=1, padx=10, columnspan=4, pady=(0, 10))

        # **********************************************
        # adding the frame to hold buttons
        self.buttonsFrame = Frame(
            self.studentClassInfoFrame, background="cyan", height=95
        )
        self.buttonsFrame.grid(row=5, column=0, columnspan=5, pady=(0, 3))

        self.saveButton = Button(
            self.buttonsFrame,
            text="Save",
            width=14,
            anchor="center",
            foreground="white",
            background="darkcyan",
            font=("ubuntu", 10, "bold"),activebackground="orange",
            activeforeground="white",
        
        )
        self.saveButton.grid(row=0, column=0, padx=(1, 5), pady=(10, 0))

        self.updateButton = Button(
            self.buttonsFrame,
            text="Update",
            width=14,
            anchor="center",
            foreground="white",
            background="darkcyan",
            font=("ubuntu", 10, "bold"),activebackground="orange",
            activeforeground="white",
        
        )
        self.updateButton.grid(row=0, column=1, padx=(0, 5), pady=(10, 0))

        self.deleteButton = Button(
            self.buttonsFrame,
            text="Delete",
            width=14,
            anchor="center",
            foreground="white",
            background="darkcyan",
            font=("ubuntu", 10, "bold"),activebackground="orange",
            activeforeground="white",
        
        )
        self.deleteButton.grid(row=0, column=2, padx=(0, 5), pady=(10, 0))

        self.resetButton = Button(
            self.buttonsFrame,
            text="Reset",
            width=14,
            anchor="center",
            foreground="white",
            background="darkcyan",
            font=("ubuntu", 10, "bold"),
            activebackground="orange",
            activeforeground="white",
        
        )
        self.resetButton.grid(row=0, column=3, padx=(0, 1), pady=(10, 0))

        # adding the frame2 to hold buttons
        self.buttonsFrame2 = Frame(self.buttonsFrame, background="cyan", height=20)
        self.buttonsFrame2.grid(row=1, column=0, columnspan=4, pady=(0, 3))

        self.addPhotoButton = Button(
            self.buttonsFrame2,
            text="Add Photo Sample",
            width=28,
            anchor="center",
            foreground="white",
            background="darkcyan",
            font=("ubuntu", 10, "bold"),
            activebackground="orange",
            activeforeground="white",
        )
        self.addPhotoButton.grid(row=0, column=0, pady=(5, 5), padx=(5, 10))

        self.updatePhotoButton = Button(
            self.buttonsFrame2,
            text="Update Photo Sample",
            width=28,
            anchor="center",
            foreground="white",
            background="darkcyan",
            font=("ubuntu", 10, "bold"),
            activebackground="orange",
            activeforeground="white",
        )
        self.updatePhotoButton.grid(row=0, column=1, padx=(0, 10))

        # **************************************************************************************************

        # right frame
        self.studentDetailsFrame = LabelFrame(
            self.student_Main_Frame,
            text="Student Details",
            font=frameFont,
            fg="magenta",
            bg="darkblue",
        )
        self.studentDetailsFrame.place(x=550, y=10, width=680, height=580)

    # **************************************************************************************************

    def __init__(self):
        self.window = CTk()
        self.window.geometry("1260x1024+0+0")
        self.mainMethod()
        self.window.mainloop()


if __name__ == "__main__":
    main_student_window = Student()
