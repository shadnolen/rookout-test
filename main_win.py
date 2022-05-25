# Import the library tkinter
from tkinter import *

# Create a GUI app
app = Tk()

# Give a title to your app
app.title("Breadstix App")

# Constructing the first frame, frame1
frame1 = LabelFrame(app, text="Date", bg="grey", fg="white", padx=40, pady=10)
frame2 = LabelFrame(app, text="App Used", bg="grey", fg="white", padx=40, pady=10)
frame3 = LabelFrame(app, text="Weather", bg="grey", fg="white", padx=40, pady=10)

frame4 = LabelFrame(app, text="Hours Worked", bg="grey", fg="white", padx=40, pady=10)
frame5 = LabelFrame(app, text="Miles Driven", bg="grey", fg="white", padx=40, pady=10)
frame6 = LabelFrame(app, text="Income Made", bg="grey", fg="white", padx=40, pady=10)

frame7 = LabelFrame(app, text="Other Expenses", bg="grey", fg="white", padx=40, pady=10)
frame8 = LabelFrame(app, text="Price Per Gallon of Gas", bg="grey", fg="white", padx=40, pady=10)
frame9 = LabelFrame(app, text="Gallons Of Gas", bg="grey", fg="white", padx=40, pady=10)

# Displaying the frame1 in row 0 and column 0
frame1.grid(row=0, column=0)
frame2.grid(row=0, column=1)
frame3.grid(row=0, column=2, padx=4, pady=4)
frame4.grid(row=1, column=0)
frame5.grid(row=1, column=1)
frame6.grid(row=1, column=2, padx=4, pady=4)
frame7.grid(row=2, column=0)
frame8.grid(row=2, column=1)
frame9.grid(row=2, column=2, padx=4, pady=4)

# Constructing the button b1 in frame1
b1 = Text(frame1)
b2 = Text(frame2)
b3 = Text(frame3)
b4 = Text(frame4)
b5 = Text(frame5)
b6 = Text(frame6)
b7 = Text(frame7)
b8 = Text(frame8)
b9 = Text(frame9)
# Displaying the button b1
b1.pack()
b2.pack()
b3.pack()
b4.pack()
b5.pack()
b6.pack()
b7.pack()
b8.pack()
b9.pack()
# Make the loop for displaying app
app.mainloop()