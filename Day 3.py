# Day - 3

from tkinter import *

top = Tk()

top.geometry("700x500")
top.configure(background="white")
top.title("Employee")


name_label = Label(top, text='Employee Name : ',
                   pady=10, padx=70, font=("Helvetica", "11"), background="white").grid(row=0, column=0)

name = Entry(top, highlightbackground="black",
             highlightthickness=1, font=("Helvetica", "10"), relief='flat', background="white").grid(row=0, column=1)

id_label = Label(top, text='Employee ID : ',
                 pady=10, padx=70, font=("Helvetica", "11"), background="white").grid(row=1, column=0)

id = Entry(top, highlightbackground="black",
           highlightthickness=1, font=("Helvetica", "10"), relief='flat', background="white").grid(row=1, column=1)

email_label = Label(top, text='Employee mail : ',
                    pady=10, padx=70, font=("Helvetica", "11"), background="white").grid(row=2, column=0)

email = Entry(top, highlightbackground="black",
              highlightthickness=1, font=("Helvetica", "10"), relief='flat', background="white").grid(row=2, column=1)

phone_label = Label(top, text='Employee mobile no : ',
                    pady=10, padx=70, font=("Helvetica", "11"), background="white").grid(row=3, column=0)

phone = Entry(top, highlightbackground="black",
              highlightthickness=1, font=("Helvetica", "10"), relief='flat', background="white").grid(row=3, column=1)

address_label = Label(top, text='Employee address : ',
                      pady=10, padx=70, font=("Helvetica", "11"), background="white").grid(row=4, column=0)

address = Text(top, width=20, height=5, highlightbackground="black",
               highlightthickness=1, font=("Helvetica", "10"), relief='flat', background="white").grid(row=4, column=1)

pl = IntVar()
pl_label = Label(top, text='Programming Language : ',
                 pady=10, padx=70, font=("Helvetica", "11"), background="white").grid(row=5, column=0)

pl1 = Radiobutton(top, text="Java", background="white",
                  variable=pl, value=1).grid(row=5, column=1)

pl2 = Radiobutton(top, text="C++", variable=pl, background="white",
                  value=2).grid(row=5, column=2)

pl3 = Radiobutton(top, text="Python", background="white", padx=10, variable=pl,
                  value=3).grid(row=5, column=3)

dept = StringVar()
dept.set("UI/UX")
dept_options = ["UI/UX", "Android", "Web"]
dept_label = Label(top, text='Department : ',
                   pady=10, padx=70, font=("Helvetica", "11"), background="white").grid(row=6, column=0)

dept_menu = OptionMenu(top, dept, *dept_options).grid(row=6, column=1)


sal_label = Label(top, text='Salary : ',
                  pady=10, padx=70, font=("Helvetica", "11"), background="white").grid(row=7, column=0)

salary = Entry(top, highlightbackground="black",
               highlightthickness=1, font=("Helvetica", "10"), relief='flat', background="white").grid(row=7, column=1)

dob_label = Label(top, text='Date of birth : ',
                  pady=10, padx=70, font=("Helvetica", "11"), background="white").grid(row=8, column=0)

dob = Entry(top, highlightbackground="black",
            highlightthickness=1, font=("Helvetica", "10"), relief='flat', background="white").grid(row=8, column=1)

password_label = Label(top, text='Password : ',
                       pady=10, padx=70, font=("Helvetica", "11"), background="white").grid(row=9, column=0)

password = Entry(top, highlightbackground="black",
                 highlightthickness=1, font=("Helvetica", "10"), relief='flat', background="white").grid(row=9, column=1)

submit = Button(top, text="Submit").grid(row=10, column=1)

top.mainloop()
