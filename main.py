import rook

import sqlite_class
from sqlite_class import SQlite
from tkinter import *


class BSTPython(object):

    # total frame
    def __init__(self):
        self.miles_enter = None
        self.weather_enter = None
        self.hours_enter = None
        self.wage_enter = None
        self.user_app = None
        self.user_local = None
        self.user_query = None
        self.exp_local = None
        self.exp_user_personal = None
        self.exp_gas = None

    def user_total(self):
        total_window = Toplevel(root)
        total_window.title("Total")
        total_window.geometry("400x300")

        display = Label(total_window, text=self.user_query.get() + ",")
        display.place(relx=0.30, rely=0.05, relwidth=1.0, anchor='n')

        display = Label(total_window, text="Before expenses you made: $0.00" + self.wage_enter.get())
        display.place(relx=0.30, rely=0.15, relwidth=1.0, anchor='n')

        miles = Label(total_window,
                      text="You drove: " + self.miles_enter.get() + " miles @ *.46 = $ " + self.miles_enter.get())
        miles.place(relx=0.30, rely=0.25, relwidth=1.0, anchor='n')

        gas = Label(total_window, text="On gas you spent: -$ " + self.exp_gas.get())
        gas.place(relx=0.30, rely=0.35, relwidth=1.0, anchor='n')

        personal = Label(total_window, text="Personal expenses: -$ " + self.exp_user_personal.get())
        personal.place(relx=0.30, rely=0.45, relwidth=1.0, anchor='n')

    # user expense frame
    def user_expense(self):
        self.exp_gas = StringVar()
        self.exp_user_personal = StringVar()
        self.exp_local = StringVar()

        expense_window = Toplevel(root)
        expense_window.title("Expenses")
        expense_window.geometry("400x300")

        display = Label(expense_window, text=self.user_query.get() + ",\n Income Made: " + self.wage_enter.get())
        display.place(relx=0.30, rely=0.05, relwidth=1.0, anchor='n')

        # local         
        location_label = Label(expense_window, text="What Store?")
        location_label.place(relx=0.26, rely=0.22, relwidth=0.48, anchor='n')
        location_entry = Entry(expense_window, textvariable=self.exp_local)
        location_entry.place(relx=0.68, rely=0.22, relwidth=0.30, anchor='n')

        # expense personal        
        expense_label = Label(expense_window, text="How much did you spend?")
        expense_label.place(relx=0.26, rely=0.32, relwidth=0.48, anchor='n')
        expense_entry = Entry(expense_window, textvariable=self.exp_user_personal)
        expense_entry.place(relx=0.68, rely=0.32, relwidth=0.30, anchor='n')

        # expense gas         
        expense_label = Label(expense_window, text="How much did you spend on gas?")
        expense_label.place(relx=0.26, rely=0.42, relwidth=0.48, anchor='n')
        gas_entry = Entry(expense_window, textvariable=self.exp_gas)
        gas_entry.place(relx=0.68, rely=0.42, relwidth=0.30, anchor='n')

        # buttons 
        button_expense = Button(expense_window, text="Total", command=self.user_total)
        button_expense.place(relx=0.25, rely=0.70, relwidth=0.25, anchor='n')
        button_cancel = Button(expense_window, text="Submit", command=self.main_frame)
        button_cancel.place(relx=0.65, rely=0.70, relwidth=0.25, anchor='n')

        # driver code
        location_entry.insert(0, "HY-Vee")
        expense_entry.insert(0, 4.20)
        gas_entry.insert(0, 45.5)

    # user income frame
    def user_income(self):
        self.user_local = StringVar()
        self.user_app = StringVar()
        self.wage_enter = StringVar()
        self.hours_enter = StringVar()
        self.miles_enter = StringVar()
        self.weather_enter = StringVar()

        income_window = Toplevel(root)
        income_window.title("Wages")
        income_window.geometry("400x300")

        display = Label(income_window, text="Hello, " + self.user_query.get())
        display.place(relx=0.30, rely=0.05, relwidth=1.0, anchor='n')

        # local         
        location_label = Label(income_window, text="What Location did you work today?")
        location_label.place(relx=0.26, rely=0.12, relwidth=0.48, anchor='n')
        location_entry = Entry(income_window, textvariable=self.user_local)
        location_entry.place(relx=0.68, rely=0.12, relwidth=0.30, anchor='n')

        # app used
        user_app_label = Label(income_window, text="What App did you use? ")
        user_app_label.place(relx=0.18, rely=0.20, relwidth=0.40, anchor='n')
        app_entry = Entry(income_window, textvariable=self.user_app)
        app_entry.place(relx=0.68, rely=0.20, relwidth=0.30, anchor='n')

        # wage
        user_wage_label = Label(income_window, text="How much did you make? ")
        user_wage_label.place(relx=0.20, rely=0.30, relwidth=0.40, anchor='n')
        wage_entry = Entry(income_window, text=self.wage_enter)
        wage_entry.place(relx=0.68, rely=0.30, relwidth=0.30, anchor='n')

        # hours grinded
        user_hours_label = Label(income_window, text="How many hours did you grind? ")
        user_hours_label.place(relx=0.24, rely=0.40, relwidth=0.44, anchor='n')
        hours_entry = Entry(income_window, textvariable=self.hours_enter)
        hours_entry.place(relx=0.68, rely=0.40, relwidth=0.30, anchor='n')

        # miles rolled
        user_miles_label = Label(income_window, text="How many miles did you roll? ")
        user_miles_label.place(relx=0.22, rely=0.50, relwidth=0.40, anchor='n')
        miles_entry = Entry(income_window, textvariable=self.miles_enter)
        miles_entry.place(relx=0.68, rely=0.50, relwidth=0.30, anchor='n')

        # weather
        user_weather_label = Label(income_window, text="What was the weather like? ")
        user_weather_label.place(relx=0.20, rely=0.60, relwidth=0.40, anchor='n')
        weather_entry = Entry(income_window, textvariable=self.weather_enter)
        weather_entry.place(relx=0.68, rely=0.60, relwidth=0.30, anchor='n')

        # buttons 
        button_expense = Button(income_window, text="Expense", command=self.user_expense)
        button_expense.place(relx=0.25, rely=0.70, relwidth=0.25, anchor='n')
        button_cancel = Button(income_window, text="Submit", command=self.main_frame)
        button_cancel.place(relx=0.65, rely=0.70, relwidth=0.25, anchor='n')

    # main frame
    def main_frame(self, root):
        self.user_query = StringVar()

        root.title("BreadStix Tracker")
        root.geometry("400x200")

        # user enter 
        user_label = Label(root, text="Who do I have the pleasure of helping?")
        user_label.place(relx=0.30, rely=0.05, relwidth=1.0, anchor='n')
        user_name = Label(root, text="Username: ")
        user_name.place(relx=0.15, rely=0.18, relwidth=1.0, anchor='n')
        user_entry = Entry(root, textvariable=self.user_query)

        user_entry.place(relx=0.45, rely=0.18, relwidth=0.4, anchor='n')

        button_user = Button(root, text="Submit", command=self.user_income)
        button_user.place(relx=0.45, rely=0.34, relwidth=0.25, anchor='n')
        # driver code
        user_entry.insert(0, "Test Driver")


if __name__ == "__main__":
    rook.start(token='eaffdcffc205a2a475278a038ef15c86feae68ce0d9fff73630e56837ca78549', labels={"env": "dev"})
    root = Tk()
    app = BSTPython()
    app.main_frame(root)
    root.mainloop()
