from tkinter import RIDGE, W, Frame, ttk
from tkinter.font import Font
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from tkinter import Entry, Tk, Label, Button, LabelFrame
from customtkinter import CTk, CTkLabel, CTkFrame
import tkinter as tk


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
            font=("ubuntu", 10, "bold"),
            activebackground="orange",
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
            font=("ubuntu", 10, "bold"),
            activebackground="orange",
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
            font=("ubuntu", 10, "bold"),
            activebackground="orange",
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

        # adding the top image in the right frame
        imageSize = (660, 140)
        imagePath = "college_images/student.jpg"
        self.studentphoto2 = resize_method(imagePath, imageSize)

        self.studentLabelPhoto = Label(
            self.studentDetailsFrame, image=self.studentphoto2, bd=None
        )
        self.studentLabelPhoto.grid(row=0, column=0, padx=5)

        # adding the next label frame to hold student details

        self.studentDetailsMainFrame = LabelFrame(
            self.studentDetailsFrame,
            text="view student details & search system",
            font=frameFont,
            fg="magenta",
            bg="darkblue",
        )
        self.studentDetailsMainFrame.grid(row=1, column=0, padx=5)

        # adding the seacrh by label
        self.searchLabel = Label(
            self.studentDetailsMainFrame,
            text="Search By:",
            bg="#F9040A",
            font=("ubuntu", 12, "bold"),
            fg="white",
        )
        self.searchLabel.grid(row=0, column=0, padx=10, pady=10)

        # adding option Combobox
        self.optionCombobox = Combobox(
            self.studentDetailsMainFrame,
            state="readonly",
            values=["Select", "Roll_No", "Phone_No"],
            font=("ubuntu", 10, "bold"),
            width=15,
            foreground="darkblue",
        )
        self.optionCombobox.current(0)
        self.optionCombobox.grid(row=0, column=1, padx=5, pady=10, sticky=W)

        # adding search Entry
        self.searchEntry = Entry(
            self.studentDetailsMainFrame,
            width=15,
            borderwidth=0,
            bg="darkgrey",
            fg="darkblue",
            font=("ubuntu", 11, "bold"),
        )
        self.searchEntry.grid(row=0, column=2, padx=5, pady=10, ipady=2)

        # adding the search and show all button
        self.searchButton = Button(
            self.studentDetailsMainFrame,
            text="SEARCH",
            fg="white",
            bg="blue",
            width=12,
            font=("Ubuntu", 10, "bold"),
        )
        self.searchButton.grid(row=0, column=3, padx=5, pady=10)

        self.showAllButton = Button(
            self.studentDetailsMainFrame,
            text="SHOW ALL",
            fg="white",
            bg="blue",
            width=14,
            font=("Ubuntu", 10, "bold"),
        )
        self.showAllButton.grid(row=0, column=4, padx=5, pady=10)

        # **********************************adding the tables Frame**********************************
        self.tablesframe = Frame(
            self.studentDetailsFrame,
            bd=2,
            bg="white",
            width=660,
            height=300,
            relief=RIDGE,
        )
        # self.tablesframe.grid(row=2, column=0, padx=5, pady=13)
        self.tablesframe.place(
            x=5,
            y=230,
            width=660,
            height=300,
        )

        #  adding the x scroll bar

        scroll_x = ttk.Scrollbar(self.tablesframe, orient="horizontal")
        scroll_y = ttk.Scrollbar(self.tablesframe, orient="vertical")

        # defining the table
        self.student_table = ttk.Treeview(
            self.tablesframe,
            columns=(
                "department",
                "course",
                "year",
                "semester",
                "studentID",
                "student_Name",
                "roll_No",
                "gender",
                "dob",
                "email",
                "phone",
                "address",
                "photo",
            ),
            xscrollcommand=scroll_x.set,
            yscrollcommand=scroll_y.set,
            show="headings",
        )

        scroll_x.pack(side="bottom", fill="x")
        scroll_y.pack(side="right", fill="y")
        scroll_x.config(command=self.student_table.xview)
        scroll_y.config(command=self.student_table.yview)

        # styling the heading of the columns in the table
        style = ttk.Style(self.window)
        style.theme_use("clam")

        style.configure("Treeview", borderwidth=1, relief="solid")

        style.configure(
            "Treeview.Heading",
            font=("Ubuntu", 10, "bold"),
            foreground="white",
            background="darkcyan",
            borderwidth=1,
            relief="solid",
            
        )
        style.map(
            "Treeview.Heading",
            background=[("active", "orange")],
            foreground=[("active", "black")],
        )
        try:
            style.configure("Treeview", bordercolor="blue")
        except tk as e:
            print("The active theme does not support changing border color:", e)

        # adding the table's headings
        self.student_table.heading("department", text="Department")
        self.student_table.heading("course", text="Course")
        self.student_table.heading("year", text="Year")
        self.student_table.heading("semester", text="Semester")
        self.student_table.heading("studentID", text="Student ID")
        self.student_table.heading("student_Name", text="Student Name")
        self.student_table.heading("roll_No", text="Roll No")
        self.student_table.heading("gender", text="Gender")
        self.student_table.heading("dob", text="DOB")
        self.student_table.heading("email", text="Email")
        self.student_table.heading("phone", text="Phone")
        self.student_table.heading("address", text="Address")
        self.student_table.heading("photo", text="Photo Sample Status")
        # self.student_table["show"]="headings"

        # configuring the width of the columns
        self.student_table.column("department", stretch=False,  width=100)
        self.student_table.column("course", stretch=False,  width=100)
        self.student_table.column("year", stretch=False,  width=100)
        self.student_table.column("semester", stretch=False,  width=100)
        self.student_table.column("studentID", stretch=False,  width=100)
        self.student_table.column("student_Name", stretch=False,  width=150)
        self.student_table.column("roll_No", stretch=False,  width=100)
        self.student_table.column("gender", stretch=False,  width=100)
        self.student_table.column("dob", stretch=False,  width=100)
        self.student_table.column("email", stretch=False,  width=120)
        self.student_table.column("phone", stretch=False,  width=100)
        self.student_table.column("address", stretch=False,  width=100)
        self.student_table.column("photo", stretch=False,  width=150)

        self.student_table.pack(fill="both", expand=1)

    # **************************************************************************************************

    def __init__(self):
        
        self.window = CTk()
        self.window.geometry("1260x1024+0+0")
        self.mainMethod()
        self.window.mainloop()


if __name__ == "__main__":
    main_student_window = Student()
