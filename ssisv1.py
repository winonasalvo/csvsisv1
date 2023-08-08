import tkinter as tk
from tkinter import *
from tkinter import ttk, messagebox, simpledialog
import csv

student_fields = ['idno', 'name', 'course', 'year', 'gender']
student_database = 'student1.csv'
course_database = 'course.csv'
course_fields = ['code', 'name']

root = tk.Tk()
root.geometry("1350x700+0+0")

def tab1():
    def tab2(): 
        label1.destroy()
        button1.destroy()
        detail_frame.destroy()
        main_frame.destroy()
        #search_frame.destroy()
        data_frame.destroy()

        label2 = Label(root, text="Student Information System", font=("Arial", 30, "bold"), border=12,
                       relief=tk.GROOVE)
        label2.pack(side=tk.TOP, fill=tk.X)

        detail_frame2 = tk.LabelFrame(root, text="Course Details", font=("Arial", 20), bd=12, relief=tk.GROOVE)
        detail_frame2.place(x=30, y=90, width=390, height=575)

        data_frame2 = tk.Frame(root, bd=12, relief=tk.GROOVE)
        data_frame2.place(x=420, y=90, width=890, height=575)

        # ===== Variables =====#
        course_code = tk.StringVar()
        course_name = tk.StringVar()

        cCode_lb = tk.Label(detail_frame2, text="Course Code", font=("Arial", 15))
        cCode_lb.grid(row=0, column=0, padx=2, pady=2)

        cCode_inp = tk.Entry(detail_frame2, bd=7, font=("Arial", 15), textvariable=course_code)
        cCode_inp.grid(row=0, column=1, padx=2, pady=2)

        cName_lb = tk.Label(detail_frame2, text="Course Name", font=("Arial", 15))
        cName_lb.grid(row=1, column=0, padx=2, pady=2)

        cName_inp = tk.Entry(detail_frame2, bd=7, font=("Arial", 15), textvariable=course_name)
        cName_inp.grid(row=1, column=1, padx=2, pady=2)

        def fetch_course():
            with open('course.csv') as a:
                reader = csv.DictReader(a, delimiter=',')
                for row in reader:
                    ccode = row['code']
                    cname = row['name']
                    course_table.insert("", 0, values=(ccode, cname))

        def add_course():
            ccode = course_code.get()
            cname = course_name.get()
            if(course_code == "" or course_name == ""):
                print('Error')
                messagebox.showerror("error", "there was an issue with some information")
                course_code.set("")
                course_name.set("")

            else:
                result = messagebox.askquestion("")
                if (result == 'yes'):
                    print('here')
                    with open('course.csv', 'a') as csvfile:
                        writer = csv.writer(csvfile)
                        writer.writerow([ccode,cname])
                    csvfile.close()
                else:
                    course_code.set("")
                    course_name.set("")

        def get_cursors(event):
            cursor_row2 = course_table.focus()
            content = course_table.item(cursor_row2)
            row = content['values']
            course_code.set(row[0])
            course_name.set(row[1])    

        def delete_course():
            #global student_fields
            global student_database

            roll = simpledialog.askstring("Delete Course", "Please Enter Course Code to be Deleted",
                                        parent=root)
            course_found = False
            updated_data = []
            with open(course_database, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                counter = 0
                for row in reader:
                    if len(row) > 0:
                        if roll != row[0]:
                            updated_data.append(row)
                            counter += 1
                        else:
                            course_found = True

            if course_found is True:
                with open(course_database, "w", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_data)
                print("Course ", roll, "deleted successfully")
            else:
                print("Course not found in our database")

            delete_student2(roll)    
            course_table.delete(*course_table.get_children())
            fetch_course()

        def delete_student2(roll):
            global student_database
            student_found = False
            updated_data = []
            print(roll)
            with open(student_database, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                counter = 0
                for row in reader:
                    if len(row) > 0:
                        if roll != row[2]:
                            updated_data.append(row)
                            counter += 1
                        else:
                            student_found = True

            if student_found is True:
                with open(student_database, "w", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_data)
                print("Roll no. ", roll, "deleted successfully")
            else:
                print("Roll No. not found in our database")
            messagebox.showinfo(title=None, message="Students with the said Course have been deleted.")

        def update_course():
            roll = simpledialog.askstring("Update Course", "Please Enter an Course Code to be Updated",
                                        parent=root)
            index_course = None
            updated_data = []
            with open(course_database, "r", encoding="utf-8") as f:
                reader = csv.reader(f)
                counter = 0
                for row in reader:
                    if len(row) > 0:
                        if roll == row[0]:
                            index_course = counter
                            print("Course Found: at index ",index_course)
                            course_data = []
                            for field in course_fields:
                                value = simpledialog.askstring("Input", "Enter " + field + ": ",
                                        parent=root)
                                course_data.append(value)
                            updated_data.append(course_data)
                        else:
                            updated_data.append(row)
                        counter += 1
                            
            if index_course is not None:
                with open(course_database, "w", encoding="utf-8") as f:
                    writer = csv.writer(f)
                    writer.writerows(updated_data)
            else:
                messagebox.showinfo("Information","Successfully Updated")
            course_table.delete(*course_table.get_children())
            fetch_course()

        def clear_course():
            course_code.set("")
            course_name.set("")

        btn_frame2 = tk.Frame(detail_frame2, bd=10, relief=tk.GROOVE)
        btn_frame2.place(x=10, y=400, width=345, height=120)

        add_btn2 = tk.Button(btn_frame2, text="Add", bd=7, font=("Arial", 13), width=15, command=add_course)
        add_btn2.grid(row=0, column=0, padx=2, pady=2)
        
        update_btn2 = tk.Button(btn_frame2, text="Update", bd=7, font=("Arial", 13), width=15, command=update_course)
        update_btn2.grid(row=0, column=1, padx=2, pady=2)

        delete_btn2 = tk.Button(btn_frame2, text="Delete", bd=7, font=("Arial", 13), width=15, command=delete_course)
        delete_btn2.grid(row=1, column=0, padx=2, pady=2)

        clear_btn2 = tk.Button(btn_frame2, text="Clear", bd=7, font=("Arial", 13), width=15, command=clear_course)
        clear_btn2.grid(row=1, column=1, padx=2, pady=2)

        search_frame2 = tk.Frame(data_frame2, relief=tk.GROOVE)
        search_frame2.pack(anchor=tk.SE)

        '''search_btn2 = tk.Button(search_frame2, text="Search", font=("Arial", 13), bd=9, width=14,
                                command=search_course)
        search_btn2.grid(row=0, column=2, padx=12, pady=2)'''

        main_frame2 = tk.Frame(data_frame2, bd=11, relief=tk.GROOVE)
        main_frame2.pack(fill=tk.BOTH, expand=True)

        y_scroll2 = tk.Scrollbar(main_frame2, orient=tk.VERTICAL)
        x_scroll2 = tk.Scrollbar(main_frame2, orient=tk.HORIZONTAL)

        course_table = ttk.Treeview(main_frame2, columns=("Course Code", "Course Name"),
                                    yscrollcommand=y_scroll2.set, xscrollcommand=x_scroll2.set)

        y_scroll2.config(command=course_table.yview)
        x_scroll2.config(command=course_table.xview)

        y_scroll2.pack(side=tk.RIGHT, fill=tk.Y)
        x_scroll2.pack(side=tk.BOTTOM, fill=tk.X)

        course_table.heading("Course Code", text="Course Code")
        course_table.heading("Course Name", text="Course Name")

        course_table['show'] = 'headings'

        course_table.column("Course Code", width=100)
        course_table.column("Course Name", width=100)

        course_table.pack(fill=tk.BOTH, expand=True)

        fetch_course()

        course_table.bind("<ButtonRelease-1>", get_cursors)
        
        def back():
            label2.destroy()
            button2.destroy()
            detail_frame2.destroy()
            main_frame2.destroy()
            #search_frame2.destroy()
            data_frame2.destroy()
            tab1()

        button2 = Button(root, text='STUDENT', font=('Times_New_Roman', 15), command=back)
        button2.pack(side=BOTTOM)



    label1 = tk.Label(root, text="Student Information System", font=("Arial", 30, "bold"), border=12,
                      relief=tk.GROOVE)
    label1.pack(side=tk.TOP, fill=tk.X)

    detail_frame = tk.LabelFrame(root, text="Student Details", font=("Arial", 20), bd=12, relief=tk.GROOVE)
    detail_frame.place(x=30, y=90, width=350, height=575)

    data_frame = tk.Frame(root, bd=12, relief=tk.GROOVE)
    data_frame.place(x=420, y=90, width=890, height=575)

        # ===== Variables =====#

    idno = tk.StringVar()
    name = tk.StringVar()
    course = tk.StringVar()
    year = tk.StringVar()
    gender = tk.StringVar()

    # ===== Entry =====#

    idno_lb = tk.Label(detail_frame, text="ID No.", font=("Arial", 15))
    idno_lb.grid(row=0, column=0, padx=2, pady=2)

    idno_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=idno)
    idno_inp.grid(row=0, column=1, padx=2, pady=2)

    name_lb = tk.Label(detail_frame, text="Name", font=("Arial", 15))
    name_lb.grid(row=1, column=0, padx=2, pady=2)

    name_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=name)
    name_inp.grid(row=1, column=1, padx=2, pady=2)


    year_lb = tk.Label(detail_frame, text="Year", font=("Arial", 15))
    year_lb.grid(row=2, column=0, padx=2, pady=2)

    year_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=year)
    year_inp.grid(row=2, column=1, padx=2, pady=2)

    gender_lb = tk.Label(detail_frame, text="Gender", font=("Arial", 15))
    gender_lb.grid(row=3, column=0, padx=2, pady=2)

    gender_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=gender)
    gender_inp.grid(row=3, column=1, padx=2, pady=2)

    course_lb = tk.Label(detail_frame, text="Course", font=("Arial", 15))
    course_lb.grid(row=4, column=0, padx=2, pady=2)

    course_inp = tk.Entry(detail_frame, bd=7, font=("Arial", 15), textvariable=course)
    course_inp.grid(row=4, column=1, padx=2, pady=2)

    # ================#

    # ====Functions=====#
    def fetch_data(): 
       with open('student1.csv') as a:
        reader = csv.DictReader(a, delimiter=',')
        for row in reader:
            oidno = row['idno']
            oname = row['name']
            ocourse = row['course']
            oyear = row['year']
            ogender = row['gender']
            student_table.insert("", 0, values=(oidno, oname, ocourse, oyear, ogender))
 

    def add_student():
        oidno = idno.get()
        oname = name.get()
        ocourse = course.get()
        oyear = year.get()
        ogender = gender.get()

        code = []
        with open('course.csv') as a:
            reader = csv.DictReader(a, delimiter=',')
            for row in reader:
                code.append(row['code'])

        if(idno == "" or name == "" or course == "" or year == "" or gender == ""):
            print('Error')
            messagebox.showerror("error", "there was an issue eith some information")
            idno.set("")
            name.set("")
            course.set("")
            year.set("")
            gender.set("")
        elif(ocourse not in code):
            messagebox.showerror(title='error', message="Course not in Course List")
        else:
            result = messagebox.askquestion("Submit", "You are about to enter the following data\n" + oidno + "\n" + oname + "\n" + ocourse + "\n" + oyear + "\n" + ogender + "\n")

            if (result == 'yes'):
                print('here')
                with open('student1.csv', 'a') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow([oidno,oname,ocourse,oyear,ogender])
                csvfile.close()
            else:
                clear_student()

        student_table.delete(*student_table.get_children())
        fetch_data()
        
    def get_cursor(event):
        ''' This function will fetch data of the selected row'''

        cursor_row = student_table.focus()
        content = student_table.item(cursor_row)
        row = content['values']
        idno.set(row[0])
        name.set(row[1])
        course.set(row[2])
        year.set(row[3])
        gender.set(row[4])

    def delete_student():
        global student_fields
        global student_database

        roll = simpledialog.askstring("Delete Student", "Please Enter an ID No. to be Deleted",
                                    parent=root)
        student_found = False
        updated_data = []
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if roll != row[0]:
                        updated_data.append(row)
                        counter += 1
                    else:
                        student_found = True

        if student_found is True:
            with open(student_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
            print("Roll no. ", roll, "deleted successfully")
        else:
            print("Roll No. not found in our database")

        student_table.delete(*student_table.get_children())
        fetch_data()

    def update_student():
        global student_fields
        global student_database

        roll = simpledialog.askstring("Update Student", "Please Enter an ID No. to be Updated",
                                    parent=root)
        index_student = None
        updated_data = []
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            counter = 0
            for row in reader:
                if len(row) > 0:
                    if roll == row[0]:
                        index_student = counter
                        print("Student Found: at index ",index_student)
                        student_data = []
                        for field in student_fields:
                            value = simpledialog.askstring("Input", "Enter " + field + ": ",
                                    parent=root)
                            student_data.append(value)
                        updated_data.append(student_data)
                    else:
                        updated_data.append(row)
                    counter += 1
                        
        if index_student is not None:
            with open(student_database, "w", encoding="utf-8") as f:
                writer = csv.writer(f)
                writer.writerows(updated_data)
        else:
            messagebox.showinfo("Information","Successfully Updated")
        student_table.delete(*student_table.get_children())
        fetch_data()
                    
    def clear_student():
        idno.set("")
        name.set("")
        course.set("")
        year.set("")
        gender.set("")
    '''def search_student():
        global student_fields
        global student_database


        roll = simpledialog.askstring("Search Student", "Please Enter ID No. to Search: ",
                                    parent=root)
        with open(student_database, "r", encoding="utf-8") as f:
            reader = csv.reader(f)
            for row in reader:
                if len(row) > 0:
                    if roll == row[0]:
                        messagebox.showinfo("Student Found","ID. No: " + row[0] + "\n" + "Name: " + row[1] + "\n" + "Course: " + row[2] + "\n" + "Year: " + row[3] + "\n" + "Gender: " + row[4])
                        break
            else:
                messagebox.showerror("Error", "ID No. not found in our database")
        input("Press any key to continue")'''


    # ===== Buttons =====#

    btn_frame = tk.Frame(detail_frame, bd=10, relief=tk.GROOVE)
    btn_frame.place(x=10, y=400, width=300, height=120)

    add_btn = tk.Button(btn_frame, text="Add", bd=7, font=("Arial", 13), width=12, command=add_student)
    add_btn.grid(row=0, column=0, padx=2, pady=2)
    
    clear_btn2 = tk.Button(btn_frame, text="Clear", bd=7, font=("Arial", 13), width=13, command=clear_student)
    clear_btn2.grid(row=1, column=1, padx=2, pady=2)
    
    update_btn = tk.Button(btn_frame, text="Update", bd=7, font=("Arial", 13), width=13, command=update_student)
    update_btn.grid(row=0, column=1, padx=2, pady=2)

    delete_btn = tk.Button(btn_frame, text="Delete", bd=7, font=("Arial", 13), width=12, command=delete_student)
    delete_btn.grid(row=1, column=0, padx=2, pady=2)

    # ===== Database frame =====#

    main_frame = tk.Frame(data_frame, bd=11, relief=tk.GROOVE)
    main_frame.pack(fill=tk.BOTH, expand=True)

    y_scroll = tk.Scrollbar(main_frame, orient=tk.VERTICAL)
    x_scroll = tk.Scrollbar(main_frame, orient=tk.HORIZONTAL)

    student_table = ttk.Treeview(main_frame, columns=("ID No.", "Name", "Course", "Year", "Gender"),
                                 yscrollcommand=y_scroll.set, xscrollcommand=x_scroll.set)

    y_scroll.config(command=student_table.yview)
    x_scroll.config(command=student_table.xview)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    y_scroll.pack(side=tk.RIGHT, fill=tk.Y)
    x_scroll.pack(side=tk.BOTTOM, fill=tk.X)

    student_table.heading("ID No.", text="ID No.")
    student_table.heading("Name", text="Name")  
    student_table.heading("Year", text="Year")
    student_table.heading("Gender", text="Gender")
    student_table.heading("Course", text="Course")

    student_table['show'] = 'headings'

    student_table.column("ID No.", width=100)
    student_table.column("Name", width=100)
    student_table.column("Year", width=100)
    student_table.column("Gender", width=100)
    student_table.column("Course", width=100)
    

    student_table.pack(fill=tk.BOTH, expand=True)

    fetch_data()
    student_table.bind("<ButtonRelease-1>", get_cursor)

    button1 = Button(root, text='COURSE', font=('Times_New_Roman', 15), command=tab2)
    button1.pack(side=BOTTOM)
tab1()

root.mainloop()
