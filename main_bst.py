from sqlite3.dbapi2 import Cursor

from tkinter import *
from tkinter import messagebox
from tkcalendar import Calendar, DateEntry
from tkinter import ttk
from datetime import datetime
import sqlite3
import math

import calendar


class BSTP(object):

    def __init__(self):
        self.user_name = None

    def user_var(self):
        self.userName = StringVar()
        self.wageLocal = StringVar()
        self.apps = StringVar()
        self.wage = IntVar()
        self.weather = StringVar()
        self.milesDriven = IntVar()
        self.gasPG = DoubleVar()
        self.galAmount = DoubleVar()
        self.otherCost = IntVar()
        self.costLocal = StringVar()
        self.gasTotal = IntVar()

    # database
    def db(self):
        self.user_name = self.userName.get()
        # wages 
        self.wage_local = self.wageLocal.get()
        self.wage_wk_dt = self.wageWkDt.get()
        self.wage_app = self.appUsed.get()
        self.wage_wage = self.wage.get()
        self.wage_weather = self.weather.get()
        # expenses
        self.miles_driven = self.milesDriven.get()
        self.miles_per_gallon = self.milesPerGallon.get()
        self.exp_gas_cost = self.gasPG.get()
        self.exp_gal = self.galAmount.get()
        self.exp_local = self.costLocal.get()
        self.exp_other_cost = self.otherCost.get()
        self.exp_date = self.expDate.get()
        self.exp_time = self.expTime.get()
        self.exp_dcrip = self.expDiscrip.get()
        self.conn = sqlite3.connect('bst.db')
        with self.conn:
            cursor = self.conn.cursor()
        cursor.execute('CREATE TABLE IF NOT EXISTS Users(userName TEXT)')
        cursor.execute('INSERT INTO Users(userName) VALUES(?)', (self.user_name,))
        self.conn.commit()
        self.conn.close()

    def results(self):
        try:
            self.miles_r = float(self.miles)
            self.mpg_r = float(self.mpg)
            self.gas_price_r = float(self.gas_price)
            self.gallons = float(self.gas_gal)
            self.gas_total_amount = (self.gas_price_r * self.gallons)
            self.gas_total_amount.delete(0, 100000000)
            self.gas_total_amount.insert(0, '{0:.2f'.format(self.gas_total_amount) + 'TeST')
        except ValueError:
            messagebox.showerror('Error 1x2', "Numbers Only Please")

    def check(self):
        self.miles = self.milesDriven.get()
        self.mpg = self.milesPerGallon.get()
        self.gas_price = self.gasPG.get()
        self.gas_gal = self.gasTotal.get()
        # self.local = self.costLocal.get()
        # self.other_cost = self.otherCost.get()
        # self.date_exp = self.expDate.get()
        # self.time_of = self.expTime.get()
        # self.dcrip = self.expDiscrip.get()
        if self.miles and self.mpg and self.gas_price and self.gas_gal:
            self.results()
        if not self.miles and self.mpg and self.gas_price and self.gas_gal:
            messagebox.showerror('0x1', 'Test Error 1')
        elif not self.mpg and self.gas_price and self.gas_gal and self.miles:
            messagebox.showerror('0x2', 'Test Error 2')
        elif not self.gas_price and self.gas_gal and self.miles and self.mpg:
            messagebox.showerror('0x3', 'Test Error 3')
        elif not self.gas_gal and self.miles and self.mpg and self.gas_price:
            messagebox.showerror('0x4', 'Test Error 4')
        if not self.miles and self.mpg and self.gas_price and self.gas_gal:
            messagebox.showerror('1x1', 'Test Error Main')

    ### Total # Frame #####
    def total_frame(self):
        tf = Toplevel(root)
        tf.title("Totals")
        tf.geometry("400x300")

        # get data
        # user
        user_name = Label(tf, text="Hay " + self.userName.get() + ",")
        user_name.place(relx=0.3, rely=0.1, relwidth=0.40, anchor='n')
        # local worked, app used, & weather
        local_wk = Label(tf,
                         text="Looks Like You Worked In The " + self.wageLocal.get() + " Area. Using " + self.apps.get())
        local_wk.place(relx=.5, rely=0.2, relwidth=1, anchor='n')
        weather = Label(tf, text="Sounds Like the Weather was " + self.weather.get())
        weather.place(relx=0.3, rely=0.26, relwidth=0.8, anchor='n')
        # wage
        wages = Label(tf, text="Making")
        wages.place(relx=0.14, rely=0.32, relwidth=0.2, anchor='n')
        money_sign = Label(tf, text="$")
        money_sign.place(relx=0.64, rely=0.32, relwidth=0.02, anchor='n')
        wage_amt = Label(tf, text=self.wage.get())
        wage_amt.place(relx=0.68, rely=0.32, relwidth=0.06, anchor='n')

        # miles driven 
        miles = Label(tf, text="You Drove ")
        miles.place(relx=0.14, rely=0.38, relwidth=0.2, anchor='n')
        money_sign = Label(tf, text="$")
        money_sign.place(relx=0.64, rely=0.38, relwidth=0.02, anchor='n')
        miles_num = Label(tf, text=self.milesDriven.get())
        miles_num.place(relx=0.68, rely=0.38, relwidth=0.06, anchor='n')

        # cpg
        cpg = Label(tf, text=" Gas Was ")
        cpg.place(relx=.14, rely=0.44, relwidth=0.2, anchor='n')
        money_sign = Label(tf, text="$")
        money_sign.place(relx=0.64, rely=0.44, relwidth=0.02, anchor='n')
        cpg_amount = Label(tf, text=self.gasPG.get())
        cpg_amount.place(relx=0.68, rely=0.44, relwidth=0.06, anchor='n')

        # gallons
        gallons = Label(tf, text="Gallons ")
        gallons.place(relx=0.14, rely=0.5, relwidth=0.2, anchor='n')
        money_sign = Label(tf, text="$")
        money_sign.place(relx=0.64, rely=0.5, relwidth=0.02, anchor='n')
        gal_amt = Label(tf, text=self.galAmount.get())
        gal_amt.place(relx=0.68, rely=0.5, relwidth=0.06, anchor='n')

        # total cost 
        """ total_gas = Label(tf, text="Gas Total:")
        total_gas.place(relx=0.2, rely=0.56, relwidth=0.2, anchor='n')
        money_sign = Label(tf, text="$")
        money_sign.place(relx=0.64, rely=0.56, relwidth=0.02, anchor='n') 
        wage_amt = Label(tf, text=self.gas_total)
        wage_amt.place(relx=0.68, rely=0.555, relwidth=1, anchor='n')  """

        # date
        # self.date_lbl = Label(tf, text=self.grad_date )
        # self.date_lbl.place(relx=0.2, rely=0.56, relwidth=1, anchor='n')

        # other
        other = Label(tf, text="Other Cost:")
        other.place(relx=0.14, rely=0.62, relwidth=0.2, anchor='n')
        money_sign = Label(tf, text="$")
        money_sign.place(relx=0.64, rely=0.62, relwidth=0.02, anchor='n')
        oth_amt = Label(tf, text=self.wage.get())
        oth_amt.place(relx=0.68, rely=0.62, relwidth=0.06, anchor='n')
        # cost local
        cost_local = Label(tf, text="From " + self.costLocal.get())
        cost_local.place(relx=0.14, rely=0.7, relwidth=0.26, anchor='n')

        # buttons
        btn_submit = Button(tf, text="Back", command=self.wage_frame)
        btn_submit.place(relx=0.25, rely=0.9, relwidth=0.25, anchor='n')
        btn_quit = Button(tf, text="Quit", command=quit)
        btn_quit.place(relx=0.65, rely=0.9, relwidth=0.25, anchor='n')

        ### Wage # Frame #####

    def wage_frame(self):
        wage_frame = Toplevel(root)
        wage_frame.title("Wages")
        wage_frame.geometry("600x400")
        # get user from main frame
        user_name = Label(wage_frame, text="Hay " + self.userName.get() + ",")
        user_name.place(relx=0.1, rely=0.05, relwidth=0.18, anchor='n')
        # location
        local_lbl = Label(wage_frame, text="Location Worked:")
        local_lbl.place(relx=0.1, rely=0.2, relwidth=0.28, anchor='n')
        local_ent = Entry(wage_frame, textvariable=self.wageLocal)
        local_ent.place(relx=0.45, rely=0.2, relwidth=0.18, anchor='n')
        # app used 
        app_list_1 = ["UberEats", "Doordash", "Grubhub", "Instacart", "Other"]
        app_list = OptionMenu(wage_frame, self.apps, *app_list_1)
        app_list.config(width=20)
        self.apps.set('App Used')
        app_list.place(relx=0.65, rely=0.18, relwidth=0.17, anchor='n')
        # weather
        weather_list = ["Sunny", "Overcast", "Drizzle", "Rain", "Sleet", "Snow"]
        weather_dd = OptionMenu(wage_frame, self.weather, *weather_list)
        weather_dd.config(width=20)
        self.weather.set('Weather')
        weather_dd.place(relx=0.85, rely=0.18, relwidth=0.17, anchor='n')
        # wage
        wage_lbl = Label(wage_frame, text="Wages:")
        wage_lbl.place(relx=0.1, rely=0.3, relwidth=0.28, anchor='n')
        wage_ent = Entry(wage_frame, textvariable=self.wage)
        wage_ent.place(relx=0.448, rely=0.3, relwidth=0.18, anchor='n')
        # date picker
        cal_lbl = Label(wage_frame, text="Pick Your Work Date: ")
        cal_lbl.place(relx=0.77, rely=0.28, relwidth=0.4, anchor='n')
        cal = Calendar(wage_frame, selectmode='day', year=2021, month=9, day=11)
        cal.place(relx=0.77, rely=0.35, relwidth=0.4, anchor='n')
        ### expense # area #####
        # miles 
        miles_lbl = Label(wage_frame, text="Miles Driven:")
        miles_lbl.place(relx=0.1, rely=0.4, relwidth=0.28, anchor='n')
        miles_driven = Entry(wage_frame, textvariable=self.milesDriven)
        miles_driven.place(relx=0.448, rely=0.4, relwidth=0.18, anchor='n')
        # gas per gallon 
        gas_lbl = Label(wage_frame, text="Cost Per Gallon: ")
        gas_lbl.place(relx=0.1, rely=0.5, relwidth=0.28, anchor='n')
        gas_ent = Entry(wage_frame, textvariable=self.gasPG)
        gas_ent.place(relx=0.448, rely=0.5, relwidth=0.18, anchor='n')
        # how many gallons
        gal_amt_lbl = Label(wage_frame, text="How Many Gallons:")
        gal_amt_lbl.place(relx=0.1, rely=0.6, relwidth=0.28, anchor='n')
        gal_amt = Entry(wage_frame, textvariable=self.galAmount)
        gal_amt.place(relx=0.448, rely=0.6, relwidth=0.18, anchor='n')
        # other cost
        other_cost_lbl = Label(wage_frame, text="Snacks/Drinks/Etc.")
        other_cost_lbl.place(relx=0.1, rely=0.7, relwidth=0.28, anchor='n')
        other_cost_ent = Entry(wage_frame, textvariable=self.otherCost)
        other_cost_ent.place(relx=0.448, rely=0.7, relwidth=0.18, anchor='n')
        # gas station/store
        gas_local_lbl = Label(wage_frame, text="Gas Station/Store:")
        gas_local_lbl.place(relx=0.1, rely=0.8, relwidth=0.28, anchor='n')
        gas_local = Entry(wage_frame, textvariable=self.costLocal)
        gas_local.place(relx=0.448, rely=0.8, relwidth=0.18, anchor='n')
        # buttons
        btn_submit = Button(wage_frame, text="Submit", command=self.total_frame)
        btn_submit.bind('<Button-1>', self.check)
        btn_submit.place(relx=0.25, rely=0.9, relwidth=0.25, anchor='n')
        btn_quit = Button(wage_frame, text="Quit", command=quit)
        btn_quit.place(relx=0.65, rely=0.9, relwidth=0.25, anchor='n')

        # driver code
        local_ent.insert(0, "Columbia, Mo")
        wage_ent.insert(0, 126.54)
        miles_driven.insert(0, 164.5)

        other_cost_ent.insert(0, 8.9)
        gas_local.insert(0, "Petro Mart")

        ### Main # Frame #####

    def main_frame(self, root):
        self.user_var()
        root.title("BSTracker")
        root.geometry("400x140")
        # user 
        user_lbl = Label(root, text="Who do I have the pleasure of helping?")
        user_lbl.place(relx=0.28, rely=0.15, relwidth=0.8, anchor='n')
        user_entry = Entry(root, textvariable=self.userName)
        user_entry.place(relx=0.7, rely=0.15, relwidth=0.3, anchor='n')
        user_entry.insert(0, "Micky Mouse")
        # buttons 
        btn_submit = Button(root, text="Submit", command=self.wage_frame)
        btn_submit.place(relx=0.25, rely=0.70, relwidth=0.25, anchor='n')
        btn_quit = Button(root, text="Quit", command=quit)
        btn_quit.place(relx=0.65, rely=0.70, relwidth=0.25, anchor='n')


if __name__ == "__main__":
    root = Tk()
    app = BSTP()
    app.main_frame(root)
    root.mainloop()
