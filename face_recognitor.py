from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image, ImageDraw
import cv2
import mysql.connector


class Face_Detector:
    def __init__(self, root):
        self.root = root
        # self.root.geometry("1200x700+20+20")
        self.root.title("Face Recognition System")
        self.root.configure(background="darkblue")
        self.root.wm_overrideredirect(True)
        self.frame_position()

        # System Title
        systemTitle = Label(
            self.root,
            text="FACE RECOGNITION",
            foreground="blue",
            bg="white",
            font=("Times new roman", 27, "bold"),
        )
        systemTitle.place(x=0, y=0, width=1200, height=50)

        back_button = Button(
            self.root,
            text="Back",
            foreground="white",
            background="darkcyan",
            font=("Ubuntu", 16, "bold"),
            anchor="center",
            cursor="hand2",
            command=self.back_method,
            activeforeground="red",
        )
        back_button.place(
            x=1070,
            y=10,
            width=120,
            height=35,
        )

        main_frame = Frame(
            self.root,
            bg="blue",
            borderwidth=2,
        )
        main_frame.place(x=0, y=50, width=1195, height=650)

        left_image = Image.open(r"college_images/face_detector1.jpg").resize((400, 645))
        self.my_image = ImageTk.PhotoImage(left_image)

        left_image_label = Label(main_frame, image=self.my_image)
        left_image_label.place(x=0, y=0, height=645, width=400)

        right_image = Image.open(r"college_images/facedetector2.jpg").resize((800, 645))
        self.my_image2 = ImageTk.PhotoImage(right_image)

        right_image_label = Label(main_frame, image=self.my_image2)
        right_image_label.place(x=405, y=0, height=645, width=800)

        # face detector button
        self.back_button = Button(
            right_image_label,
            text="Face Detector",
            foreground="white",
            background="darkblue",
            relief=RAISED,
            activebackground="darkcyan",
            activeforeground="darkblue",
            font=("Ubuntu", 15, "bold"),
            anchor="center",
            cursor="hand2",
            command=self.face_dection_method,
        )
        self.back_button.place(x=320, y=570, width=170, height=40)

    def frame_position(self):
        # Get screen width and height

        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Window dimensions
        window_width = 1200
        window_height = 700

        # Calculate x and y positions to center the window
        x_position = (screen_width // 2) - (window_width // 2)
        y_position = (screen_height // 2) - (window_height // 2)
        self.root.geometry(f"{window_width}x{window_height}+{x_position}+{y_position}")

    """ ===============Face recognition==============="""

    def face_dection_method(self):
        def draw_boundary(
            img, classifier, scalefactor, min_neighbour, color, text, clf
        ):
            gray_image = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
            features = classifier.detectMultiScale(
                gray_image, scalefactor, min_neighbour
            )
            coordinate = []
            for x, y, w, h in features:
                cv2.rectangle(
                    img,
                    (x, y),
                    (x + w, y + h),
                    (0, 255, 0),
                    3,
                )
                id, predict = clf.predict(gray_image[y : y + h, x : x + w])

                confidence = int((100 * (1 - predict / 300)))

                conn = mysql.connector.connect(
                    host="localhost", user="root", password="isaac"
                )
                cursor = conn.cursor()
                cursor.execute("use students")

                cursor.execute(
                    f"select studentName from student_details where studentId={id}"
                )
                name = cursor.fetchone()
                name = "+".join(name) if name else "Unknown"

                cursor.execute(
                    f"select rollNo from student_details where studentId={id}"
                )
                rollNo = cursor.fetchone()
                rollNo = "+".join(map(str,rollNo)) if rollNo else "Unknown"

                cursor.execute(
                    f"select department from student_details where studentId={id}"
                )
                department = cursor.fetchone()
                department = "+".join(department) if department else "Unknown"

                if confidence > 77:
                    cv2.putText(
                        img,
                        f"Roll:{rollNo}",
                        (x, y - 55),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        color=(139, 0, 0),
                        thickness=3,
                    )
                    cv2.putText(
                        img,
                        f"Name:{name}",
                        (x, y - 30),
                        cv2.FONT_HERSHEY_COMPLEX,
                        0.8,
                        color=(139, 0, 0),
                        thickness=3,
                    )
                    cv2.putText(
                        img,
                        f"Department:{department}",
                        org=(x, y - 5),
                        fontFace=cv2.FONT_HERSHEY_COMPLEX,
                        fontScale=0.8,
                        color=(139, 0, 0),
                        thickness=3,
                    )

                else:
                    cv2.rectangle(img, (x, y), (x + w, y + h), (0, 0, 255), 3)
                    cv2.putText(
                        img,
                        f"Unknown Face",
                        org=(x, y - 5),
                        fontFace=cv2.FONT_HERSHEY_DUPLEX,
                        fontScale=0.8,
                        color=(0, 128, 0),
                        thickness=3,
                    )

                coordinate = [x, y, w, h]

            return coordinate

        def recognize(img, clf, faceCascade):
            coordinate = draw_boundary(
                img,
                faceCascade,
                1.1,
                10,
                (255, 25, 255),
                "Face",
                clf,
            )
            return img

        face_cascade = cv2.CascadeClassifier("haarcascade_frontalface_default.xml")
        clf = cv2.face.LBPHFaceRecognizer_create()
        # Local Binary Pattern Histogram (LBPH) Face Recognition
        clf.read("classifier.xml")
        video_capture = cv2.VideoCapture(0)

        while True:
            ret, img = video_capture.read()

            if not ret or img is None:
                print("Error: Failed to capture image from webcam")
                continue  # Skip this iteration if there's no valid frame

            img = recognize(img, clf, face_cascade)
            cv2.imshow("Welcome to Face Recognition", img)
            if cv2.waitKey(1) == 13:
                break
        video_capture.release()
        cv2.destroyAllWindows()

    def back_method(self):
        # self.root.destroy()
        response = messagebox.askyesno(
            "Confirm", "Do you really want to quit?", parent=self.root
        )
        if response:
            self.root.grab_release()
            self.root.destroy()


if __name__ == "__main__":
    root = Tk()
    obj = Face_Detector(root)
    root.mainloop()
