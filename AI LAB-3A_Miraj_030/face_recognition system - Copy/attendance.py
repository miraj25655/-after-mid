from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
from tkinter import messagebox
import mysql.connector
import cv2
import os
import csv
from tkinter import filedialog
import datetime

mydata = []
csv_filename = ""  # To store the currently opened CSV file name

class Attendance:
    def __init__(self, root):
        self.root = root
        self.root.geometry("1530x790+0+0")
        self.root.title("Face Recognition System")

        # Variables
        self.attendanceId = StringVar()
        self.roll = StringVar()
        self.name = StringVar()
        self.dep = StringVar()
        self.time = StringVar()
        self.date = StringVar()
        self.attendance = StringVar()
        self.semester = StringVar()

        # Banner images
        img = Image.open(r"C:\Users\bixwa\Desktop\face_recognition system\college_images\banner1.jpg")
        img = img.resize((500, 130), Image.ANTIALIAS)
        self.photoimg = ImageTk.PhotoImage(img)
        f_lbl = Label(self.root, image=self.photoimg)
        f_lbl.place(x=0, y=0, width=500, height=130)

        img1 = Image.open(r"C:\Users\bixwa\Desktop\face_recognition system\college_images\banner2.jpg")
        img1 = img1.resize((550, 130), Image.ANTIALIAS)
        self.photoimg1 = ImageTk.PhotoImage(img1)
        f_lbl = Label(self.root, image=self.photoimg1)
        f_lbl.place(x=500, y=0, width=550, height=130)

        img2 = Image.open(r"C:\Users\bixwa\Desktop\face_recognition system\college_images\banner.jpg")
        img2 = img2.resize((560, 130), Image.ANTIALIAS)
        self.photoimg2 = ImageTk.PhotoImage(img2)
        f_lbl = Label(self.root, image=self.photoimg2)
        f_lbl.place(x=1000, y=0, width=560, height=130)

        # Background image
        img3 = Image.open(r"C:\Users\bixwa\Desktop\face_recognition system\college_images\banner4.jpg")
        img3 = img3.resize((1530, 700), Image.ANTIALIAS)
        self.photoimg3 = ImageTk.PhotoImage(img3)
        bg_img = Label(self.root, image=self.photoimg3)
        bg_img.place(x=0, y=110, width=1550, height=790)

        title_lbl = Label(bg_img, text="ATTENDANCE", font=("times new roman", 35, "bold"), bg="dark blue", fg="white")
        title_lbl.place(x=0, y=0, width=1550, height=45)

        main_frame = Frame(bg_img, bd=2, bg="white")
        main_frame.place(x=20, y=50, width=1485, height=700)

        # Left label frame
        Left_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Student Attendance Details", font=("times new roman", 15, "bold"))
        Left_frame.place(x=10, y=10, width=730, height=614)

        img_left = Image.open(r"C:\Users\bixwa\Desktop\face_recognition system\college_images\banner32.jpg")
        img_left = img_left.resize((720, 130), Image.ANTIALIAS)
        self.photoimg_left = ImageTk.PhotoImage(img_left)
        f_lbl = Label(Left_frame, image=self.photoimg_left)
        f_lbl.place(x=5, y=0, width=715, height=130)

        # Inside left frame
        left_inside_frame = Frame(Left_frame, bd=2, relief=RIDGE, bg="white")
        left_inside_frame.place(x=5, y=132, width=715, height=450)

        # Labels and entries
        attendanceId_label = Label(left_inside_frame, text="AttendanceID:", font=("times new roman", 15, "bold"), bg="white")
        attendanceId_label.grid(row=0, column=0, padx=10, pady=20, sticky=W)

        self.attendanceId_entry = ttk.Entry(left_inside_frame, width=16, textvariable=self.attendanceId, font=("times new roman", 15, "bold"))
        self.attendanceId_entry.grid(row=0, column=1, padx=10, pady=20, sticky=W)

        rolllabel = Label(left_inside_frame, text="Roll:", font=("times new roman", 15, "bold"), bg="white")
        rolllabel.grid(row=0, column=2, padx=10, pady=5, sticky=W)

        self.atten_roll_entry = ttk.Entry(left_inside_frame, width=16, textvariable=self.roll, font=("times new roman", 15, "bold"))
        self.atten_roll_entry.grid(row=0, column=3, padx=10, pady=5, sticky=W)

        namelabel = Label(left_inside_frame, text="Name:", font=("times new roman", 15, "bold"), bg="white")
        namelabel.grid(row=1, column=0, padx=10, pady=5, sticky=W)

        self.atten_name_entry = ttk.Entry(left_inside_frame, width=16, textvariable=self.name, font=("times new roman", 15, "bold"))
        self.atten_name_entry.grid(row=1, column=1, padx=10, pady=5, sticky=W)

        deptlabel = Label(left_inside_frame, text="Department:", font=("times new roman", 15, "bold"), bg="white")
        deptlabel.grid(row=1, column=2, padx=10, pady=5, sticky=W)

        self.atten_dept_entry = ttk.Entry(left_inside_frame, width=16, textvariable=self.dep, font=("times new roman", 15, "bold"))
        self.atten_dept_entry.grid(row=1, column=3, padx=10, pady=5, sticky=W)

        timelabel = Label(left_inside_frame, text="Time:", font=("times new roman", 15, "bold"), bg="white")
        timelabel.grid(row=2, column=0, padx=10, pady=5, sticky=W)

        self.atten_time_entry = ttk.Entry(left_inside_frame, width=16, textvariable=self.time, font=("times new roman", 15, "bold"))
        self.atten_time_entry.grid(row=2, column=1, padx=10, pady=5, sticky=W)

        datelabel = Label(left_inside_frame, text="Date:", font=("times new roman", 15, "bold"), bg="white")
        datelabel.grid(row=2, column=2, padx=10, pady=20, sticky=W)

        self.atten_date_entry = ttk.Entry(left_inside_frame, width=16, textvariable=self.date, font=("times new roman", 15, "bold"))
        self.atten_date_entry.grid(row=2, column=3, padx=10, pady=20, sticky=W)

        attendancelabel = Label(left_inside_frame, text="Attendance Status", font=("times new roman", 15, "bold"), bg="white")
        attendancelabel.grid(row=3, column=0, padx=10, pady=5, sticky=W)

        self.atten_status = ttk.Combobox(left_inside_frame, font=("times new roman", 15, "bold"), state="readonly", width=14, textvariable=self.attendance)
        self.atten_status["values"] = ("Status", "Present", "Absent")
        self.atten_status.current(0)
        self.atten_status.grid(row=3, column=1, padx=10, pady=5, sticky=W)

        # New labels and entries for Subject, Teacher, EmployeeID, and Semester
        subject_label = Label(left_inside_frame, text="Subject:", font=("times new roman", 15, "bold"), bg="white")
        subject_label.grid(row=3, column=2, padx=10, pady=5, sticky=W)

        self.subject_entry = ttk.Entry(left_inside_frame, width=16, font=("times new roman", 15, "bold"))
        self.subject_entry.grid(row=3, column=3, padx=10, pady=5, sticky=W)

        teacher_label = Label(left_inside_frame, text="Teacher:", font=("times new roman", 15, "bold"), bg="white")
        teacher_label.grid(row=4, column=0, padx=10, pady=20, sticky=W)

        self.teacher_entry = ttk.Entry(left_inside_frame, width=16, font=("times new roman", 15, "bold"))
        self.teacher_entry.grid(row=4, column=1, padx=10, pady=20, sticky=W)

        employee_id_label = Label(left_inside_frame, text="Employee ID:", font=("times new roman", 15, "bold"), bg="white")
        employee_id_label.grid(row=4, column=2, padx=10, pady=5, sticky=W)

        self.employee_id_entry = ttk.Entry(left_inside_frame, width=16, font=("times new roman", 15, "bold"))
        self.employee_id_entry.grid(row=4, column=3, padx=10, pady=5, sticky=W)

        semester_label = Label(left_inside_frame, text="Semester:", font=("times new roman", 15, "bold"), bg="white")
        semester_label.grid(row=5, column=0, padx=10, pady=5, sticky=W)

        self.semester_entry = ttk.Entry(left_inside_frame, width=16, textvariable=self.semester, font=("times new roman", 15, "bold"))
        self.semester_entry.grid(row=5, column=1, padx=10, pady=5, sticky=W)

        # Button frame
        btn_frame = Frame(left_inside_frame, bd=2, relief=RIDGE, bg="white")
        btn_frame.place(x=5, y=408, width=700, height=35)

        save_btn = Button(btn_frame, text="Import CSV", command=self.importCsv, width=15, font=("times new roman", 13, "bold"), bg="dark blue", fg="white", cursor="hand2")
        save_btn.grid(row=0, column=0)

        export_btn = Button(btn_frame, text="Export CSV", command=self.exportCsv, width=17, font=("times new roman", 13, "bold"), bg="dark blue", fg="white", cursor="hand2")
        export_btn.grid(row=0, column=1)

        update_btn = Button(btn_frame, text="Update", command=self.update_data, width=17, font=("times new roman", 13, "bold"), bg="dark blue", fg="white", cursor="hand2")
        update_btn.grid(row=0, column=2)

        reset_btn = Button(btn_frame, text="Reset", command=self.reset_data, width=17, font=("times new roman", 13, "bold"), bg="dark blue", fg="white", cursor="hand2")
        reset_btn.grid(row=0, column=3)


        # Right label frame
        Right_frame = LabelFrame(main_frame, bd=2, bg="white", relief=RIDGE, text="Attendance Details", font=("times new roman", 15, "bold"))
        Right_frame.place(x=750, y=10, width=720, height=614)

        table_frame = Frame(Right_frame, bd=2, relief=RIDGE, bg="white")
        table_frame.place(x=5, y=5, width=710, height=455)

        # Scroll Bar
        scroll_x = ttk.Scrollbar(table_frame, orient=HORIZONTAL)
        scroll_y = ttk.Scrollbar(table_frame, orient=VERTICAL)

        self.AttendanceReportTable = ttk.Treeview(table_frame, column=("id", "roll", "name", "department", "time", "date", "attendance", "subject", "teacher", "employee_id", "semester"),
                                                  xscrollcommand=scroll_x.set, yscrollcommand=scroll_y.set)

        scroll_x.pack(side=BOTTOM, fill=X)
        scroll_y.pack(side=RIGHT, fill=Y)
        scroll_x.config(command=self.AttendanceReportTable.xview)
        scroll_y.config(command=self.AttendanceReportTable.yview)

        self.AttendanceReportTable.heading("id", text="Attendance ID")
        self.AttendanceReportTable.heading("roll", text="Roll")
        self.AttendanceReportTable.heading("name", text="Name")
        self.AttendanceReportTable.heading("department", text="Department")
        self.AttendanceReportTable.heading("time", text="Time")
        self.AttendanceReportTable.heading("date", text="Date")
        self.AttendanceReportTable.heading("attendance", text="Attendance")
        self.AttendanceReportTable.heading("subject", text="Subject")
        self.AttendanceReportTable.heading("teacher", text="Teacher")
        self.AttendanceReportTable.heading("employee_id", text="Employee ID")
        self.AttendanceReportTable.heading("semester", text="Semester")
        self.AttendanceReportTable["show"] = "headings"

        self.AttendanceReportTable.column("id", width=100)
        self.AttendanceReportTable.column("roll", width=100)
        self.AttendanceReportTable.column("name", width=100)
        self.AttendanceReportTable.column("department", width=100)
        self.AttendanceReportTable.column("time", width=100)
        self.AttendanceReportTable.column("date", width=100)
        self.AttendanceReportTable.column("attendance", width=100)
        self.AttendanceReportTable.column("subject", width=100)
        self.AttendanceReportTable.column("teacher", width=100)
        self.AttendanceReportTable.column("employee_id", width=100)
        self.AttendanceReportTable.column("semester", width=100)

        self.AttendanceReportTable.pack(fill=BOTH, expand=1)
        self.AttendanceReportTable.bind("<ButtonRelease>", self.get_cursor)

    # Fetch data
    def fetchData(self, rows):
        self.AttendanceReportTable.delete(*self.AttendanceReportTable.get_children())
        for i in rows:
            self.AttendanceReportTable.insert("", END, values=i)

    # Import CSV
    def importCsv(self):
        global mydata, csv_filename
        mydata.clear()  # Clear existing data
        csv_filename = filedialog.askopenfilename(initialdir=os.getcwd(), title="Open CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), parent=self.root)
        if not csv_filename:
            messagebox.showerror("Error", "No file selected", parent=self.root)
            return
        try:
            with open(csv_filename, mode='r', newline='', encoding='utf-8-sig') as myfile:
                csvread = csv.reader(myfile, delimiter=",")
                for i in csvread:
                    if len(i) == 11:  # Ensure the row has the correct number of columns (11 with Semester)
                        mydata.append(i)
                self.fetchData(mydata)
        except Exception as es:
            messagebox.showerror("Error", f"Error reading file: {str(es)}", parent=self.root)


    def exportCsv(self):
        try:
            if len(mydata) < 1:
                messagebox.showerror("No Data", "No data found to export", parent=self.root)
                return
            export_file_path = filedialog.asksaveasfilename(initialdir=os.getcwd(), title="Save CSV", filetypes=(("CSV File", "*.csv"), ("All File", "*.*")), defaultextension=".csv", parent=self.root)
            if not export_file_path:
                return
            with open(export_file_path, mode='w', newline='', encoding='utf-8-sig') as myfile:
                exp_write = csv.writer(myfile, delimiter=",")
                exp_write.writerow(["Attendance ID", "Roll", "Name", "Department", "Time", "Date", "Attendance", "Subject", "Teacher", "Employee ID", "Semester"])  # Add headers
                for i in mydata:
                    exp_write.writerow(i)
                messagebox.showinfo("Data Export", "Your data has been exported to " + os.path.basename(export_file_path) + " successfully")
        except Exception as es:
            messagebox.showerror("Error", f"Error exporting data: {str(es)}", parent=self.root)



    # Reset data
    def reset_data(self):
        self.attendanceId.set("")
        self.roll.set("")
        self.name.set("")
        self.dep.set("")
        self.time.set("")
        self.date.set("")
        self.attendance.set("Status")
        self.subject_entry.delete(0, END)
        self.teacher_entry.delete(0, END)
        self.employee_id_entry.delete(0, END)
        self.semester.set("")

    # Cursor function
    def get_cursor(self, event=""):
        cursor_row = self.AttendanceReportTable.focus()
        content = self.AttendanceReportTable.item(cursor_row)
        rows = content["values"]
        self.attendanceId.set(rows[0])
        self.roll.set(rows[1])
        self.name.set(rows[2])
        self.dep.set(rows[3])
        self.time.set(rows[4])
        self.date.set(rows[5])
        self.attendance.set(rows[6])
        self.subject_entry.delete(0, END)
        self.subject_entry.insert(0, rows[7])
        self.teacher_entry.delete(0, END)
        self.teacher_entry.insert(0, rows[8])
        self.employee_id_entry.delete(0, END)
        self.employee_id_entry.insert(0, rows[9])
        self.semester.set(rows[10])

    # Update data
    def update_data(self):
        global csv_filename
        if self.attendanceId.get() == "" or self.roll.get() == "" or self.name.get() == "" or self.dep.get() == "" or self.attendance.get() == "Status":
            messagebox.showerror("Error", "All fields are required", parent=self.root)
        else:
            try:
                new_entry = [
                    self.attendanceId.get(),
                    self.roll.get(),
                    self.name.get(),
                    self.dep.get(),
                    datetime.datetime.now().strftime("%H:%M:%S"),  # Current time
                    datetime.datetime.now().strftime("%Y-%m-%d"),  # Current date
                    self.attendance.get(),
                    self.subject_entry.get(),
                    self.teacher_entry.get(),
                    self.employee_id_entry.get(),
                    self.semester.get()
                ]
                mydata.append(new_entry)
                self.fetchData(mydata)

                # Write the new entry directly to the CSV file
                if csv_filename:
                    with open(csv_filename, mode='a', newline="") as myfile:
                        csv_writer = csv.writer(myfile, delimiter=",")
                        csv_writer.writerow(new_entry)
                    messagebox.showinfo("Success", "New record added and saved to the CSV file", parent=self.root)
                else:
                    messagebox.showerror("Error", "No CSV file loaded", parent=self.root)
            except Exception as es:
                messagebox.showerror("Error", f"Error updating data: {str(es)}", parent=self.root)

if __name__ == "__main__":
    root = Tk()
    obj = Attendance(root)
    root.mainloop()
