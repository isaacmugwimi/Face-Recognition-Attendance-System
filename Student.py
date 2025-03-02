import os
from tkinter import *
import re
from tkinter import RIDGE, W, Frame, StringVar, messagebox, ttk
from tkinter.font import Font
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
from tkinter import Entry, Tk, Label, Button, LabelFrame
from customtkinter import CTk, CTkLabel, CTkFrame
import tkinter as tk
import customtkinter
from tkcalendar import DateEntry
import Database
import cv2
import pymysql


def resize_method(imagePath, imageSize):
    currentImage = Image.open(imagePath)
    resizedImage = currentImage.resize(imageSize)
    return ImageTk.PhotoImage(resizedImage)


def is_email_valid(email):
    email_regex = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(email_regex, email)


class Student:

    def mainMethod(self):

        # -------------------- VARIABLES ---------------------
        self.var_dep = StringVar()
        self.var_course = StringVar()
        self.var_year = StringVar()
        self.var_semester = StringVar()
        self.var_studentID = StringVar()
        self.var_student_Name = StringVar()
        self.var_roll_No = StringVar()
        self.var_gender = StringVar()
        self.var_dob = StringVar()
        self.var_email = StringVar()
        self.var_phone = StringVar()
        self.var_address = StringVar()
        self.var_photo = StringVar()
        # ----------------------------------------------------

        # first Image

        imageSize = (420, 130)
        self.photoImage = resize_method("college_images/students1.jpg", imageSize)
        Label(self.window, image=self.photoImage, text="").place(
            x=0, y=0, width=420, height=130
        )

        # second Image
        imageSize = (420, 130)
        self.photoImage1 = resize_method(
            "college_images/facialrecognition.png", imageSize
        )
        Label(self.window, image=self.photoImage1, text="").place(
            x=420, y=0, width=420, height=130
        )

        # # Third Image
        imageSize = (420, 130)
        self.photoImage2 = resize_method("college_images/students2.jpg", imageSize)
        Label(self.window, image=self.photoImage2, text="").place(
            x=840, y=0, width=420, height=130
        )

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
        self.backButton = customtkinter.CTkButton(
            self.bgimagelabel,
            text="Back",
            command=self.back_method,
            text_color="#FFFFFF",
            bg_color="#FFF",
            fg_color="#36719F",
            height=25,
            corner_radius=25,
            width=130,
            cursor="hand2",
            hover_color="#FF4505",
            font=("arial", 14),
        )
        self.backButton.place(x=1170, y=-2)

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
        # Department
        self.departmentLabel = Label(
            self.courseInfoFrame, text="Department:", font=("ubuntu", 10)
        )
        self.departmentLabel.grid(row=0, column=0, padx=(10, 0), pady=(10, 0), sticky=W)

        self.departmentCombobox = Combobox(
            self.courseInfoFrame,
            textvariable=self.var_dep,
            values=["Select department", "BScIT", "BBIT", "CS", "SE"],
            state="readonly",
            foreground="darkblue",
            background="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        self.departmentCombobox.current(0)
        self.departmentCombobox.grid(row=0, column=1, padx=(0, 10), pady=(10, 0))

        # Course
        self.coursesLabel = Label(
            self.courseInfoFrame, text="Courses:", font=("ubuntu", 10)
        )
        self.coursesLabel.grid(row=0, column=2, padx=(20, 0), pady=(10, 0), sticky=W)

        self.coursesCombobox = Combobox(
            self.courseInfoFrame,
            textvariable=self.var_course,
            values=["Select Courses", "BScIT", "BBIT", "CS", "SE"],
            state="readonly",
            foreground="darkblue",
            background="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        self.coursesCombobox.current(0)
        self.coursesCombobox.grid(row=0, column=3, padx=(0, 10), pady=(10, 0))

        # Year
        self.yearLabel = Label(
            self.courseInfoFrame,
            text="Year:",
            font=("ubuntu", 10),
        )
        self.yearLabel.grid(row=1, column=0, padx=(10, 0), pady=(10, 10), sticky=W)

        self.yearCombobox = Combobox(
            self.courseInfoFrame,
            textvariable=self.var_year,
            values=["Select Year", "I", "II", "III", "IV"],
            state="readonly",
            foreground="darkblue",
            font=("ubuntu", 10, "bold"),
        )

        self.yearCombobox.current(0)
        self.yearCombobox.grid(row=1, column=1, padx=(0, 10), pady=(10, 10), sticky=W)

        # Semester
        self.semesterLabel = Label(
            self.courseInfoFrame, text="Semester:", font=("ubuntu", 10)
        )
        self.semesterLabel.grid(row=1, column=2, padx=(20, 0), pady=(10, 10), sticky=W)

        self.semesterCombobox = Combobox(
            self.courseInfoFrame,
            textvariable=self.var_semester,
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
        self.studentClassInfoFrame.grid(row=2, column=0, sticky="nsew")

        # ID no
        self.studentIdNoLabel = Label(
            self.studentClassInfoFrame,
            text="Id No:",
            font=("ubuntu", 10),
        )
        self.studentIdNoLabel.grid(row=0, column=0, padx=(10, 0), pady=(5, 5), sticky=W)

        self.studentidNoEntry = Entry(
            self.studentClassInfoFrame,
            textvariable=self.var_studentID,
            width=25,
            fg="darkblue",
            borderwidth=0,
            bg="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        self.studentidNoEntry.grid(
            row=0, column=1, padx=(0, 10), pady=(5, 5), ipady=2, sticky=W
        )

        # Student Name

        self.studentNameLabel = Label(
            self.studentClassInfoFrame,
            text="Name:",
            font=("ubuntu", 10),
        )
        self.studentNameLabel.grid(row=0, column=2, padx=(10, 0), pady=(5, 5), sticky=W)

        self.studentNameEntry = Entry(
            self.studentClassInfoFrame,
            textvariable=self.var_student_Name,
            width=25,
            borderwidth=0,
            bg="darkgrey",
            fg="darkblue",
            font=("ubuntu", 10, "bold"),
        )
        self.studentNameEntry.grid(
            row=0,
            column=3,
            padx=(0, 15),
            pady=(5, 5),
            ipady=2,
        )

        # Gender
        self.genderLabel = Label(
            self.studentClassInfoFrame,
            text="Gender:",
            font=("ubuntu", 10),
        )
        self.genderLabel.grid(row=1, column=0, padx=(10, 0), pady=(5, 5), sticky=W)

        self.genderCombobox = Combobox(
            self.studentClassInfoFrame,
            textvariable=self.var_gender,
            values=["Select Gender", "Male", "Female", "Other"],
            width=25,
            state="readonly",
            foreground="darkblue",
            font=("ubuntu", 8, "bold"),
        )
        self.genderCombobox.current(0)
        self.genderCombobox.grid(
            row=1, column=1, padx=(0, 10), pady=(5, 5), ipady=2, sticky=W
        )

        # DOB
        self.dobLabel = Label(
            self.studentClassInfoFrame,
            text="DOB:",
            font=("ubuntu", 10),
        )
        self.dobLabel.grid(row=1, column=2, padx=(10, 0), pady=(5, 5), sticky=W)

        self.dobEntry = DateEntry(
            self.studentClassInfoFrame,
            textvariable=self.var_dob,
            background="dark blue",
            foreground="white",
            width=25,
            borderwidth=0,
            font=("ubuntu", 8),
            date_pattern="dd-MM-yyyy",
            showweeknumbers=False,
            year=2000,
            selectbackground="lightblue",
            selectforeground="black",
            weekendforeground="red",
        )

        self.dobEntry.grid(
            row=1,
            column=3,
            padx=(0, 15),
            pady=(5, 5),
            ipady=2,
        )

        # Email

        self.emailLabel = Label(
            self.studentClassInfoFrame,
            text="Email:",
            font=("ubuntu", 10),
        )
        self.emailLabel.grid(row=2, column=0, padx=(10, 0), pady=(5, 5), sticky=W)

        self.emailEntry = Entry(
            self.studentClassInfoFrame,
            textvariable=self.var_email,
            width=25,
            fg="darkblue",
            borderwidth=0,
            bg="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        self.emailEntry.grid(
            row=2, column=1, padx=(0, 10), pady=(5, 5), ipady=2, sticky=W
        )

        # Phone

        self.phoneNoLabel = Label(
            self.studentClassInfoFrame,
            text="Phone:",
            font=("ubuntu", 10),
        )
        self.phoneNoLabel.grid(row=2, column=2, padx=(10, 0), pady=(5, 5), sticky=W)

        self.phoneNoEntry = Entry(
            self.studentClassInfoFrame,
            textvariable=self.var_phone,
            width=25,
            borderwidth=0,
            bg="darkgrey",
            fg="darkblue",
            font=("ubuntu", 10, "bold"),
        )

        self.phoneNoEntry.grid(
            row=2,
            column=3,
            padx=(0, 15),
            pady=(5, 5),
            ipady=2,
        )

        # address
        self.addressLabel = Label(
            self.studentClassInfoFrame,
            text="Address:",
            font=("ubuntu", 10),
        )
        self.addressLabel.grid(row=3, column=0, padx=(10, 0), pady=(5, 5), sticky=W)

        self.addressEntry = Entry(
            self.studentClassInfoFrame,
            width=25,
            borderwidth=0,
            bg="darkgrey",
            fg="darkblue",
            font=("ubuntu", 10, "bold"),
        )

        self.addressEntry.grid(
            row=3,
            column=1,
            padx=(0, 15),
            pady=(5, 5),
            ipady=2,
        )

        # Roll number
        self.roll_no_Label = Label(
            self.studentClassInfoFrame,
            text="Roll No:",
            font=("ubuntu", 10),
        )
        self.roll_no_Label.grid(row=3, column=2, padx=(10, 0), pady=(5, 5), sticky=W)

        self.roll_no_Entry = Entry(
            self.studentClassInfoFrame,
            width=25,
            borderwidth=0,
            bg="darkgrey",
            fg="darkblue",
            font=("ubuntu", 10, "bold"),
        )

        self.roll_no_Entry.grid(
            row=3,
            column=3,
            padx=(0, 15),
            pady=(5, 5),
            ipady=2,
        )

        self.photosample = ttk.Radiobutton(
            self.studentClassInfoFrame,
            variable=self.var_photo,
            text="Take Photo Sample",
            value="Yes",
        )
        self.photosample.grid(row=4, column=0, padx=10, columnspan=2, pady=(0, 10))

        self.photosample1 = ttk.Radiobutton(
            self.studentClassInfoFrame,
            variable=self.var_photo,
            text="No Photo Sample",
            value="No",
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
            command=self.save_to_database_method,
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
            command=self.update_method,
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
            command=self.delete_method,
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
            command=self.reset_method,
        )
        self.resetButton.grid(row=0, column=3, padx=(0, 1), pady=(10, 0))

        # adding the frame2 to hold buttons
        self.buttonsFrame2 = Frame(self.buttonsFrame, background="cyan", height=20)
        self.buttonsFrame2.grid(row=1, column=0, columnspan=4, pady=(0, 3))

        self.addPhotoButton = Button(
            self.buttonsFrame2,
            text="Add Photo Sample",
            width=28,
            command= self.generate_dataset,
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
            command=self.fetch_data,
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
        except tk.TclError:
            print("The active theme does not support changing border color:")

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
        self.student_table.column("department", stretch=False, width=100)
        self.student_table.column("course", stretch=False, width=100)
        self.student_table.column("year", stretch=False, width=100)
        self.student_table.column("semester", stretch=False, width=100)
        self.student_table.column("studentID", stretch=False, width=100)
        self.student_table.column("student_Name", stretch=False, width=150)
        self.student_table.column("roll_No", stretch=False, width=100)
        self.student_table.column("gender", stretch=False, width=100)
        self.student_table.column("dob", stretch=False, width=100)
        self.student_table.column("email", stretch=False, width=120)
        self.student_table.column("phone", stretch=False, width=100)
        self.student_table.column("address", stretch=False, width=100)
        self.student_table.column("photo", stretch=False, width=150)
        self.student_table.bind(
            "<ButtonRelease>", lambda event: self.display_data(event)
        )
        self.student_table.pack(fill="both", expand=1)

    # **************************************************************************************************

    # ********************** fUNCTION DECLARATION ********************

    def back_method(self):
        self.window.destroy()

    def data_insertion(self):  # for inserting data into the table...

        # for data in self.student_table.get_children():
        #     self.student_table.delete(data)

        self.student_table.insert(
            "",
            "end",
            values=(
                self.department,
                self.course_dropdown,
                self.year,
                self.semester,
                self.student_id_no,
                self.student_name,
                self.roll_no,
                self.gender,
                self.selectedDate,
                self.email,
                self.phoneNo,
                self.address,
                self.var_radio,
            ),
        )

    # reset_method
    def reset_method(self):
        self.departmentCombobox.current(0)
        self.coursesCombobox.current(0)
        self.yearCombobox.current(0)
        self.semesterCombobox.current(0)
        self.studentidNoEntry.delete(0, END)
        self.studentNameEntry.delete(0, END)
        self.roll_no_Entry.delete(0, END)
        self.genderCombobox.current(0)
        self.dobEntry.delete(0, END)
        self.dobEntry.set_date("01/01/2000")
        self.emailEntry.delete(0, END)
        self.phoneNoEntry.delete(0, END)
        self.addressEntry.delete(0, END)
        self.var_photo.set("")

        # clearing the table
        for row in self.student_table.get_children():
            self.student_table.delete(row)

    def reset_method2(self):
        self.departmentCombobox.current(0)
        self.coursesCombobox.current(0)
        self.yearCombobox.current(0)
        self.semesterCombobox.current(0)
        self.studentidNoEntry.delete(0, END)
        self.studentNameEntry.delete(0, END)
        self.roll_no_Entry.delete(0, END)
        self.genderCombobox.current(0)
        self.dobEntry.delete(0, END)
        self.dobEntry.set_date("01/01/2000")
        self.emailEntry.delete(0, END)
        self.phoneNoEntry.delete(0, END)
        self.addressEntry.delete(0, END)
        self.var_photo.set("")

    # Display Data method
    def display_data(self, event):
        selected_item = self.student_table.focus()
        if selected_item:
            row = self.student_table.item(selected_item)["values"]
            self.reset_method2()
            self.departmentCombobox.set(row[0])
            self.coursesCombobox.set(row[1])
            self.yearCombobox.set(row[2])
            self.semesterCombobox.set(row[3])
            self.studentidNoEntry.insert(0, row[4])
            self.studentNameEntry.insert(0, row[5])
            self.roll_no_Entry.insert(0, row[6])
            self.genderCombobox.set(row[7])
            self.dobEntry.delete(0, END)
            self.dobEntry.insert(0, row[8])
            self.emailEntry.insert(0, row[9])
            self.phoneNoEntry.insert(0, row[10])
            self.addressEntry.insert(0, row[11])
            self.var_photo.set(row[12])

    #  save to database method
    def save_to_database_method(self):
        self.department = self.departmentCombobox.get()
        self.course_dropdown = self.coursesCombobox.get()
        self.year = self.yearCombobox.get()
        self.semester = self.semesterCombobox.get()
        self.student_id_no = self.studentidNoEntry.get()
        self.student_name = self.studentNameEntry.get()
        self.roll_no = self.roll_no_Entry.get()
        self.gender = self.genderCombobox.get()
        self.selectedDate = self.dobEntry.get_date()
        self.email = self.emailEntry.get()
        self.phoneNo = self.phoneNoEntry.get()
        self.address = self.addressEntry.get()
        self.var_radio = self.var_photo.get()

        # self.searchEntry = self.searchEntry.get()

        # validating data before inserting it to the database

        # if (
        #     self.departmentCombobox.current() == 0
        #     or self.yearCombobox.current() == 0
        #     or self.semesterCombobox.current() == 0
        #     or self.coursesCombobox.current() == 0
        #     or self.student_id_no == ""
        #     or self.genderCombobox.current() == 0
        #     or self.email == ""
        #     or self.student_name == ""
        #     or self.phoneNo == ""
        # ):
        #     messagebox.showerror("Error", "Please fill all the fields")
        #     return

        # # Checking student id number
        # if not self.student_id_no.isdigit():
        #     messagebox.showerror("Error", "Student ID number must be an integer")
        #     return

        # # checking email
        # if not is_email_valid(self.email):
        #     messagebox.showerror("Error", "Invalid email format")
        #     return

        # phone number checking
        if not self.phoneNo.isdigit():
            messagebox.showerror("Error", "Phone number should be a valid integer")
            return

        else:

            try:
                Database.create_table()
                if not Database.checking_user_existence(self.student_id_no):
                    self.data_insertion()
                    Database.inserting_into_Database(
                        self.department,
                        self.course_dropdown,
                        self.year,
                        self.semester,
                        self.student_id_no,
                        self.student_name,
                        self.roll_no,
                        self.gender,
                        self.selectedDate,
                        self.email,
                        self.phoneNo,
                        self.address,
                        self.var_radio,
                    )

                    messagebox.showinfo("success", "Student details added successfully")
                    self.reset_method2()

                else:
                    messagebox.showerror("Error", "user already Exists")

            except Exception as e:
                print(e)
                messagebox.showerror("Error", f"{e}")

    # delete Method
    def delete_method(self):
        selected_item = self.student_table.focus()

        if not selected_item:
            messagebox.showerror("Error", "Please select a record to delete")
            return
        else:
            response = messagebox.askyesno(
                "Confirm",
                "Do you really want to delete the record? \n Note: The record will be deleted permanently",
            )

            if response:
                try:
                    results = self.student_table.item(selected_item, "values")[4]
                    Database.delete_user(results)
                    self.reset_method()
                    self.fetch_data()
                except Exception as e:
                    print(e)
                    messagebox.showerror("Error", f"{e}")

    # update method
    def update_method(self):

        selected_item = self.student_table.focus()
        if not selected_item:
            messagebox.showerror(
                "Failed!", "Please select in the table a student to update."
            )
        else:
            try:

                # Retrieve updated values from entry fields BEFORE validation
                self.student_id_no = self.studentidNoEntry.get()
                self.student_name = self.studentNameEntry.get()
                self.department = self.departmentCombobox.get()
                self.course_dropdown = self.coursesCombobox.get()
                self.year = self.yearCombobox.get()
                self.semester = self.semesterCombobox.get()
                self.roll_no = self.roll_no_Entry.get()
                self.gender = self.genderCombobox.get()
                self.selectedDate = self.dobEntry.get()
                self.email = self.emailEntry.get()
                self.phoneNo = self.phoneNoEntry.get()
                self.address = self.addressEntry.get()
                self.var_radio = self.var_photo.get()

                # validating data before inserting it to the database

                if (
                    self.departmentCombobox.current() == 0
                    or self.yearCombobox.current() == 0
                    or self.semesterCombobox.current() == 0
                    or self.coursesCombobox.current() == 0
                    or self.student_id_no == ""
                    or self.genderCombobox.current() == 0
                    or self.email == ""
                    or self.student_name == ""
                    or self.phoneNo == ""
                ):
                    messagebox.showerror("Error", "Please fill all the fields")
                    return

                # # Checking student id number
                if not self.student_id_no.isdigit():
                    messagebox.showerror(
                        "Error", "Student ID number must be an integer"
                    )
                    return

                # # checking email
                if not is_email_valid(self.email):
                    messagebox.showerror("Error", "Invalid email format")
                    return

                # phone number checking
                if not self.phoneNo.isdigit():
                    messagebox.showerror(
                        "Error", "Phone number should be a valid integer"
                    )
                    return

                else:

                    Database.update_database(
                        self.department,
                        self.course_dropdown,
                        self.year,
                        self.semester,
                        self.student_id_no,
                        self.student_name,
                        self.roll_no,
                        self.gender,
                        self.selectedDate,
                        self.email,
                        self.phoneNo,
                        self.address,
                        self.var_radio,
                    )
                    # inserting the updated data in to the table
                    self.data_insertion()
                    messagebox.showinfo(
                        "Success",
                        f"{self.student_name} with {self.student_id_no}, updated successfully!",
                    )
                    print("succcessfully!!!!!!!")
            except Exception as e:
                print(e)
                messagebox.showerror("Error", f"{e}")

    # fetch data method
    def fetch_data(self):
        data = Database.data_fetching_from_database()
        if len(data) != 0:
            self.student_table.delete(
                *self.student_table.get_children()
            )  # deletes all the rows in the tables
            for i in data:
                self.student_table.insert("", END, values=i)

    # Generate data set or take photo samples
    def generate_dataset(self):
        self.student_id_no = self.studentidNoEntry.get()
        self.student_name = self.studentNameEntry.get()
        self.department = self.departmentCombobox.get()
        self.course_dropdown = self.coursesCombobox.get()
        self.year = self.yearCombobox.get()
        self.semester = self.semesterCombobox.get()
        self.roll_no = self.roll_no_Entry.get()
        self.gender = self.genderCombobox.get()
        self.selectedDate = self.dobEntry.get()
        self.email = self.emailEntry.get()
        self.phoneNo = self.phoneNoEntry.get()
        self.address = self.addressEntry.get()
        self.var_radio = self.var_photo.get()

        # validating data before inserting it to the database

        if (
            self.departmentCombobox.current() == 0
            or self.yearCombobox.current() == 0
            or self.semesterCombobox.current() == 0
            or self.coursesCombobox.current() == 0
            or self.student_id_no == ""
            or self.genderCombobox.current() == 0
            or self.email == ""
            or self.student_name == ""
            or self.phoneNo == ""
        ):
            messagebox.showerror("Error", "Please fill all the fields")
            return
        else:
    #         try:
    #             conn = pymysql.connect(host="localhost", user="root", password="isaac")
    #             cursor = conn.cursor()
    #             cursor.execute("use students")
    #             cursor.execute("select * from student_details")
    #             results = cursor.fetchall()
    #             id = 0
    #             for x in results:
    #                 id += 1

    #             query = """ update student_details set department = %s, course = %s, year = %s, semester = %s, studentName = %s, rollNo = %s, 
    # gender = %s, dob = %s, email = %s, phoneNo = %s, address = %s, photo = %s where studentId=%s"""

    #             values = (
    #                     self.department,
    #                     self.course_dropdown,
    #                     self.year,
    #                     self.semester,
    #                     self.student_id_no ==id+1,
    #                     self.student_name,
    #                     self.roll_no,
    #                     self.gender,
    #                     self.selectedDate,
    #                     self.email,
    #                     self.phoneNo,
    #                     self.address,
    #                     self.var_radio,
    #             )
    #             cursor.execute(query, values)
    #             conn.commit()
    #             self.reset_method()
    #             self.fetch_data()
    #             conn.close()
                

                # ***************************** Loading predefined data on face frontals from opencv ***************
                face_classifier = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
                def face_cropped(img):
                    gray =cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
                    faces = face_classifier.detectMultiScale(gray, 1.3, 5)
                    # faces = is a list of detected faces in an image.
                    # detectMultiScale() detects faces
                    # scalling factor = 1.3
                    # minimum neighbour = 5
                    for (x,y,w,h) in faces:
                        # x, y → Top-left corner of the face.
                        # w, h → Width and height of the face.
                        face_cropped =img[y:y+h, x:x+w] # Crop the detected face
                        # The notation img[startY:endY, startX:endX] is array slicing in NumPy
                        return face_cropped # Return only the face
                    
                capture = cv2.VideoCapture(0) # starting the webcam
                img_id = 0  #counter for numbering saved images.

                while True:
                    return_status, my_frame = capture.read() # Capture a frame from the webcam
                    # return_status = bolean i.e true or false
                    #  myframe = actual frame/image

                    # remember capture.read() always return two values, that is return and the frame 
                    # return i.e return_status for checking if the camera is working, or is it busy and it return a bolean
                    
                    if not return_status or my_frame is None:
                        print("Failed to capture image from camera.")
                        break # Stop if no frame is captured

                    cropped_face = face_cropped(my_frame)
                    
                    if cropped_face is not None:
                        img_id += 1 # Increment image ID

                        face = cv2.resize(cropped_face, (450, 450))  # Resize face to 450x450 pixels
                        face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY)  # Convert face to grayscale
                        
                        file_name_path = "data/user." + str(self.student_id_no) + "." + str(img_id) + ".jpg"
                        cv2.imwrite(file_name_path, face)  # Save the cropped face image    
                        
                        cv2.putText(face, str(img_id), (50, 50), cv2.FONT_HERSHEY_COMPLEX, 2, (0, 255, 0), 2)
                        cv2.imshow("Cropped Face", face)

                    if cv2.waitKey(1) == 13 or int(img_id) == 20:
                        break

                capture.release()
                cv2.destroyAllWindows()
                messagebox.showinfo("Results", "Taking Photo Samples Completed!!!!")

   

    # *********************************** END OF FUNCTION DECLARATION***********************************

    def __init__(self, mainWindow):
        self.student_id_no = ""
        self.window = mainWindow
        self.window.geometry("1260x1000+0+0")
        self.mainMethod()
        self.window.mainloop()


if __name__ == "__main__":
    root = CTk()
    Student(root)
