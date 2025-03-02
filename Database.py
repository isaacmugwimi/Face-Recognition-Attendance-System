import pymysql


def create_table():
    conn = pymysql.connect(host="localhost", user="root", password="isaac")
    cursor = conn.cursor()
    cursor.execute("create database if not exists students")
    cursor.execute("use students")
    query = """ create table if not exists student_details( department varchar(50), course varchar(50),
                                     year varchar(50),
                                     semester varchar(20),
                                     studentId int primary key not null,
                                     studentName varchar(50),
                                     rollNo int,
                                     gender varchar(50),
                                     dob DATE,
                                     email varchar(50),
                                     phoneNo varchar(50),
                                     address varchar(50),
                                     photo varchar(50)) """

    cursor.execute(query)
    conn.commit()
    conn.close()


def update_database(
    department,
    course_dropdown,
    year,
    semester,
    studentIdNo,
    studentName,
    rollNo,
    gender,
    selectedDate,
    email,
    phoneNo,
    address,
    var_radio,
):
    conn = pymysql.connect(host="localhost", user="root", password="isaac")
    cursor = conn.cursor()
    cursor.execute("use students")
    query = """ update student_details set department = %s, course = %s, year = %s, semester = %s, studentName = %s, rollNo = %s, 
    gender = %s, dob = %s, email = %s, phoneNo = %s, address = %s, photo = %s where studentId=%s"""

    values = (
        department,
        course_dropdown,
        year,
        semester,
        studentName,
        int(rollNo),
        gender,
        selectedDate,
        email,
        int(phoneNo),
        address,
        var_radio,
        int(studentIdNo),
    )

    print(f"Executing query: {query} with values: {values}")

    cursor.execute(query, values)
    conn.commit()

    conn.close()


def checking_user_existence(studentIdNo):
    conn = pymysql.connect(host="localhost", user="root", password="isaac")
    cursor = conn.cursor()
    cursor.execute("use students")
    query = """ select * from student_details where studentId = %s """
    cursor.execute(query, (studentIdNo,))
    rows = cursor.fetchone()
    conn.close()
    return rows


def inserting_into_Database(
    department,
    course_dropdown,
    year,
    semester,
    studentIdNo,
    studentName,
    rollNo,
    gender,
    selectedDate,
    email,
    phoneNo,
    address,
    var_radio,
):
    conn = pymysql.connect(host="localhost", user="root", password="isaac")
    cursor = conn.cursor()
    cursor.execute("use students")
    query = """INSERT INTO student_details 
        (department, course, year, semester, studentId, studentName, rollNo, gender, dob, email, phoneNo, address, photo) 
        VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    """
    values = (
        department,
        course_dropdown,
        year,
        semester,
        int(studentIdNo),
        studentName,
        int(rollNo),
        gender,
        selectedDate,
        email,
        int(phoneNo),
        address,
        var_radio,
    )

    cursor.execute(query, values)
    conn.commit()
    conn.close()


def data_fetching_from_database():
    conn = pymysql.connect(host="localhost", user="root", password="isaac")
    cursor = conn.cursor()
    cursor.execute("use students")
    query = """select * from student_details """
    cursor.execute(query)
    data = cursor.fetchall()
    conn.commit()
    conn.close()
    return data


def delete_user(studentID):
    conn = pymysql.connect(host="localhost", user="root", password="isaac")
    cursor = conn.cursor()
    cursor.execute("use students")
    query = """delete from student_details where studentId = %s"""
    cursor.execute(query, studentID)
    conn.commit()
    conn.close()
