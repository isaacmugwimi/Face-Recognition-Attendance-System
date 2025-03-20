from tkinter import *
from tkinter import ttk
from PIL import ImageTk, Image
from tkinter import messagebox
import os
import csv
from tkinter import filedialog

# def resize_method(imagePath, imageSize):
#     currentImage = Image.open(imagePath)
#     resizedImage = currentImage.resize(imageSize, Image.LANCZOS)
#     print("hi")
#     return ImageTk.PhotoImage(resizedImage)

mydata = []


class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1200x700+20+20")
        self.root.title("Face Recognition System")

        """"adding variables"""
        self.var_attendance_id = StringVar()
        self.var_attendance_roll = StringVar()
        self.var_attendance_name = StringVar()
        self.var_attendance_department = StringVar()
        self.var_attendance_time = StringVar()
        self.var_attendance_date = StringVar()
        self.var_attendance_status = StringVar()

        # adding Top Images

        # first image
        # imagePath = "college_images/students1.jpg"
        # imageSize = (400, 120)
        # self.img1 =resize_method(imagePath, imageSize)
        # img_label1 = Label(self.root, image=self.img1)
        # img_label1.place(x=0, y=0, width=400, height=120)

        self.img1 = Image.open("college_images/students1.jpg").resize((400, 120))
        self.my_image1 = ImageTk.PhotoImage(
            self.img1
        )  # Store in self to prevent garbage collection

        img_label1 = Label(self.root, image=self.my_image1)
        img_label1.place(x=0, y=0, width=400, height=120)

        # second image
        img2 = Image.open("college_images/students2.jpg").resize((400, 120))
        self.my_image2 = ImageTk.PhotoImage(img2)
        img_label2 = Label(self.root, image=self.my_image2, relief=GROOVE, bd=2)
        img_label2.place(x=400, y=0, width=400, height=120)

        # Third image
        img3 = Image.open("college_images/students3.jpg").resize((400, 120))
        self.my_image3 = ImageTk.PhotoImage(img3)
        img_label3 = Label(self.root, image=self.my_image3)
        img_label3.place(x=800, y=0, width=400, height=120)

        # Back ground Image
        imagePath = "college_images/wp2551980.jpg"
        imageSize = (1200, 600)
        bg_img = Image.open(imagePath).resize(imageSize)
        self.my_bg_img = ImageTk.PhotoImage(bg_img)

        bgimagelabel = Label(
            self.root, image=self.my_bg_img, borderwidth=2, relief=GROOVE
        )
        bgimagelabel.place(x=0, y=120, width=1200, height=600)

        # System Title
        systemTitle = Label(
            bgimagelabel,
            text="ATTENDANCE MANAGEMENT SYSTEM",
            foreground="green",
            width=1200,
            height=0,
            bg="white",
            font=("Times new roman", 20, "bold"),
        )
        systemTitle.place(x=0, y=0, width=1200, height=40)

        #  Adding Main Frame to hold the widgets
        main_frame = Frame(bgimagelabel, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1165, height=600)

        """Adding the left frame"""
        left_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief="ridge",
            text="Student Attendance Details",
            font=("mv boli", 13, "bold"),
            foreground="dark blue",
        )
        left_frame.place(x=10, y=10, width=550, height=510)

        img_left = Image.open("college_images/face-recognition.png")
        img_left = img_left.resize((540, 140), Image.LANCZOS)
        self.my_img_left = ImageTk.PhotoImage(img_left)
        left_img_label = Label(left_frame, image=self.my_img_left, bd=3, fg="red")
        left_img_label.place(x=5, y=0, width=540, height=140)

        # adding the left inside frame
        left_inside_frame = Frame(left_frame, bd=2, bg="white", relief="ridge")
        left_inside_frame.place(x=5, y=155, width=540, height=300)

        # adding the widgets
        # Attendance ID no
        attendance_id_label = Label(
            left_inside_frame,
            text="AttendanceId:",
            font=("ubuntu", 10, "bold"),
            background="white",
        )
        attendance_id_label.grid(row=0, column=0, padx=(10), pady=(5), sticky=W)

        attendance_id_entry = Entry(
            left_inside_frame,
            textvariable=self.var_attendance_id,
            width=20,
            fg="darkblue",
            borderwidth=0,
            bg="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        attendance_id_entry.grid(row=0, column=1, padx=0, pady=(5), sticky=W)

        # Attendance roll no
        attendance_roll_no_label = Label(
            left_inside_frame,
            text="Roll:",
            font=("ubuntu", 10, "bold"),
            background="white",
        )
        attendance_roll_no_label.grid(row=0, column=2, padx=(30, 0), pady=(5), sticky=W)

        attendance_roll_no_entry = Entry(
            left_inside_frame,
            textvariable=self.var_attendance_roll,
            width=22,
            fg="darkblue",
            borderwidth=0,
            bg="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        attendance_roll_no_entry.grid(row=0, column=3, padx=0, pady=(5), sticky=W)

        # Attendance Name
        attendance_name_label = Label(
            left_inside_frame,
            text="Name:",
            font=("ubuntu", 10, "bold"),
            background="white",
        )
        attendance_name_label.grid(row=1, column=0, padx=(10), pady=(5), sticky=W)

        attendance_name_entry = Entry(
            left_inside_frame,
            textvariable=self.var_attendance_name,
            width=20,
            fg="darkblue",
            borderwidth=0,
            bg="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        attendance_name_entry.grid(row=1, column=1, padx=0, pady=(5), sticky=W)

        # Attendance department
        attendance_department_label = Label(
            left_inside_frame,
            text="Department:",
            font=("ubuntu", 10, "bold"),
            background="white",
        )
        attendance_department_label.grid(
            row=1, column=2, padx=(30, 0), pady=(5), sticky=W
        )

        attendance_department_entry = Entry(
            left_inside_frame,
            textvariable=self.var_attendance_department,
            width=22,
            fg="darkblue",
            borderwidth=0,
            bg="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        attendance_department_entry.grid(row=1, column=3, padx=0, pady=(5), sticky=W)

        # Attendance time
        attendance_time_label = Label(
            left_inside_frame,
            text="Time:",
            font=("ubuntu", 10, "bold"),
            background="white",
        )
        attendance_time_label.grid(row=2, column=0, padx=(10), pady=(5), sticky=W)

        attendance_time_entry = Entry(
            left_inside_frame,
            textvariable=self.var_attendance_time,
            width=20,
            fg="darkblue",
            borderwidth=0,
            bg="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        attendance_time_entry.grid(row=2, column=1, padx=0, pady=(5), sticky=W)

        # Attendance date
        attendance_date_label = Label(
            left_inside_frame,
            text="Date:",
            font=("ubuntu", 10, "bold"),
        )
        attendance_date_label.grid(row=2, column=2, padx=(30, 0), pady=(5), sticky=W)

        attendance_date_entry = Entry(
            left_inside_frame,
            textvariable=self.var_attendance_date,
            width=22,
            fg="darkblue",
            borderwidth=0,
            bg="darkgrey",
            font=("ubuntu", 10, "bold"),
        )
        attendance_date_entry.grid(row=2, column=3, padx=0, pady=(5), sticky=W)

        # Attendance status
        attendance_status_label = Label(
            left_inside_frame,
            text="Attendance Status:",
            font=("ubuntu", 10, "bold"),
            background="white",
        )
        attendance_status_label.grid(
            row=3,
            columnspan=2,
            padx=(30, 0),
            pady=(5),
        )

        attendance_status_combobox = ttk.Combobox(
            left_inside_frame,
            textvariable=self.var_attendance_status,
            values=["Status", "Present", "Absent"],
            width=13,
            state="readonly",
            foreground="darkblue",
            font=("ubuntu", 8, "bold"),
        )

        attendance_status_combobox.grid(row=3, padx=10, pady=(5), column=2)

        attendance_status_combobox.current(0)

        """Buttons Frame"""
        btn_frame = Frame(
            left_inside_frame,
            bd=2,
            relief=RIDGE,
            bg="white",
        )
        btn_frame.place(
            x=5,
            y=250,
            width=525,
            height=35,
        )

        # adding the buttons
        imort_csv_btn = Button(
            btn_frame,
            text="Import csv",
            command=self.import_csv,
            width=12,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        imort_csv_btn.grid(row=0, column=0)
        export_csv_btn = Button(
            btn_frame,
            text="Export csv",
            command=self.export_csv,
            width=12,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        export_csv_btn.grid(row=0, column=1)

        update_btn = Button(
            btn_frame,
            text="Update",
            command=self.update_data,
            width=12,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        update_btn.grid(row=0, column=2)
        reset_btn = Button(
            btn_frame,
            text="Reset",
            width=12,
            command=self.reset_data,
            font=("times new roman", 13, "bold"),
            bg="blue",
            fg="white",
        )
        reset_btn.grid(row=0, column=3)

        """Adding the right frame"""
        right_frame = LabelFrame(
            main_frame,
            bd=2,
            bg="white",
            relief="ridge",
            text="Attendance Details",
            font=("mv boli", 13, "bold"),
            foreground="dark blue",
        )
        right_frame.place(x=610, y=10, width=530, height=510)

        # adding the table frame
        table_frame = Frame(right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=515, height=255)

        # Scroll bar table
        x_scroll_bar = ttk.Scrollbar(table_frame, orient="horizontal")
        y_scroll_bar = ttk.Scrollbar(table_frame, orient="vertical")

        self.attendance_report_table = ttk.Treeview(
            table_frame,
            column=("id", "roll", "name", "department", "time", "date", "attendance"),
            xscrollcommand=x_scroll_bar.set,
            yscrollcommand=y_scroll_bar.set,
            show="headings",
        )

        x_scroll_bar.pack(side=BOTTOM, fill=X)
        x_scroll_bar.config(command=self.attendance_report_table.xview)
        y_scroll_bar.pack(side=RIGHT, fill=Y)
        y_scroll_bar.config(command=self.attendance_report_table.yview)

        # styling the heading of the columns in the table
        style = ttk.Style(self.root)
        style.theme_use("clam")
        style.configure("Treeview", bordercolor="blue", borderwidth=1, relief="solid")
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

        self.attendance_report_table.heading("id", text="Attendance ID")
        self.attendance_report_table.heading("roll", text="Roll")
        self.attendance_report_table.heading("name", text="Name")
        self.attendance_report_table.heading("department", text="Department")
        self.attendance_report_table.heading("time", text="Time")
        self.attendance_report_table.heading("date", text="Date")
        self.attendance_report_table.heading("attendance", text="Attendance")

        # configuring width of the columns
        self.attendance_report_table.column("id", stretch=False, width=100)
        self.attendance_report_table.column("roll", stretch=False, width=100)
        self.attendance_report_table.column("name", stretch=False, width=150)
        self.attendance_report_table.column("department", stretch=False, width=150)
        self.attendance_report_table.column("time", stretch=False, width=100)
        self.attendance_report_table.column("date", stretch=False, width=100)
        self.attendance_report_table.column("attendance", stretch=False, width=120)

        # when user selects a row the entries should be updated usin the the code below
        self.attendance_report_table.bind("<ButtonRelease>", self.get_table_content)

        self.attendance_report_table.pack(fill=BOTH, expand=True)

    def fetch_data(self, rows):
        self.attendance_report_table.delete(
            *self.attendance_report_table.get_children()
        )
        for i in rows:
            self.attendance_report_table.insert("", "end", values=i)

    def import_csv(self):
        # remember csv means comma seperated values.

        global mydata
        mydata.clear()
        file_name = filedialog.askopenfilename(
            initialdir=os.getcwd(),
            title="Open CSV",
            filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
            parent=self.root,
        )

        # initialdir=os.getcwd() → Starts in the current working directory.
        # title="Open CSV" → Sets the dialog title.
        # filetypes=(("CSV File", "*.csv"), ("All File", "*.*")) → Allows only CSV files by default but also supports all file types.
        # parent=self.root → Attaches the file dialog to the main window.

        if not file_name:  # if the user cancels the file dialog stop the execution
            return

        with open(file_name) as myfile:
            csvread = csv.reader(myfile, delimiter=",")
            for i in csvread:
                mydata.append(i)  # Store each row in mydata
            self.fetch_data(mydata)  # Update the table with new data

        """ below is a brief description of some functions used in this method"""
        # filedialog.askopenfilename() → Opens file selection dialog.
        # csv.reader() → Reads CSV file row by row.
        # mydata.append(i) → Stores each row in a global list.
        # fetch_data(mydata) → Updates the table with new data.

    def export_csv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror(
                    "Error", "No data found to export", parent=self.root
                )
                return False
            file_name = filedialog.asksaveasfilename(
                defaultextension=".csv",
                initialdir=os.getcwd(),
                title="Save CSV",
                filetypes=(("CSV File", "*.csv"), ("All File", "*.*")),
                parent=self.root,
            )

            if not file_name:
                return

            with open(file_name, mode="w", newline="") as myfile:
                export_write = csv.writer(myfile, delimiter=",")
                for i in mydata:
                    export_write.writerow(i)
                messagebox.showinfo(
                    "Success",
                    f"Your data exported to {os.path.basename(file_name)} successfully",
                )

        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def get_table_content(self, event=""):
        table_row = self.attendance_report_table.focus()
        content = self.attendance_report_table.item(table_row)
        rows = content["values"]
        self.var_attendance_id.set(rows[0])
        self.var_attendance_roll.set(rows[1])
        self.var_attendance_name.set(rows[2])
        self.var_attendance_department.set(rows[3])
        self.var_attendance_time.set(rows[4])
        self.var_attendance_date.set(rows[5])
        self.var_attendance_status.set(rows[6])

    def reset_data(self):
        self.var_attendance_id.set("")
        self.var_attendance_roll.set("")
        self.var_attendance_name.set("")
        self.var_attendance_department.set("")
        self.var_attendance_time.set("")
        self.var_attendance_date.set("")
        self.var_attendance_status.set("")

        # for clearing the table folow the below code
        # for row in self.attendance_report_table.get_children():
        #     self.attendance_report_table.delete(row)

    def update_data(self):
        selected_item = self.attendance_report_table.focus()
        if not selected_item:
            messagebox.showerror(
                "Failed!", "No item selected to update", parent=self.root
            )
            return

        else:
            try:
                attendance_id = self.var_attendance_id.get()
                attendance_roll = self.var_attendance_roll.get()
                attendance_name = self.var_attendance_name.get()
                attendance_department = self.var_attendance_department.get()
                attendance_time = self.var_attendance_time.get()
                attendance_date = self.var_attendance_date.get()
                attendance_status = self.var_attendance_status.get()

                # validating data before updating it in the treeview

                if (
                    attendance_id == ""
                    or attendance_roll == ""
                    or attendance_name == ""
                    or attendance_department == ""
                    or attendance_time == ""
                    or attendance_date == ""
                    or attendance_status == ""
                ):
                    messagebox.showerror("Error", "All field are required!")

                else:
                    self.attendance_report_table.item(
                        selected_item,
                        values=(
                            attendance_id,
                            attendance_roll,
                            attendance_name,
                            attendance_department,
                            attendance_time,
                            attendance_date,
                            attendance_status,
                        ),
                    )
                    messagebox.showinfo(
                        "Success",
                        "Attendance record updated successfully!",
                        parent=self.root,
                    )

            except Exception as e:
                messagebox.showerror("Error", f"Failed due to: {e}", parent=self.root)


if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
