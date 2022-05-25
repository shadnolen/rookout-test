
from tkinter import *
from tkinter import messagebox
from tkinter import ttk

from main import root


class User:
    def __init__(self, user_name, date_used):
        self.user = user_name
        self.date = date_used


class App:
    def __init__(self, app_used, amount_made, hours_worked, daily_weather):
        self.app = app_used
        self.amount = amount_made
        self.hours = hours_worked
        self.weather = daily_weather


class Vehicle:
    def __init__(self, miles_driven, cost_per_gal, gas_total, maintenance_cost):
        self.miles = miles_driven
        self.cpg = cost_per_gal
        self.gasTotal = gas_total
        self.mainCost = maintenance_cost


class OtherCost:
    def __init__(self, misc_cost, store_name):
        self.cost = misc_cost
        self.place = store_name


class BST(root):
    User()

    def main_frame(self):
        self.title("BSTracker")
        self.geometry("400x140")
        # user
        user_lbl = Label(self, text="Who do I have the pleasure of helping?")
        user_lbl.place(relx=0.28, rely=0.15, relwidth=0.8, anchor='n')
        user_entry = Entry(self, textvariable=self.userName)
        user_entry.place(relx=0.7, rely=0.15, relwidth=0.3, anchor='n')
        user_entry.insert(0, "Micky Mouse")
        # buttons
        btn_submit = Button(self, text="Submit", command=self.wage_frame)
        btn_submit.place(relx=0.25, rely=0.70, relwidth=0.25, anchor='n')
        btn_quit = Button(self, text="Quit", command=quit)
        btn_quit.place(relx=0.65, rely=0.70, relwidth=0.25, anchor='n')


if __name__ == "__main__":
    root = Tk()
    app = BST()
    app.main_frame()
    root.mainloop()
    