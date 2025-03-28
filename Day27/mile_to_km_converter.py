import math
from tkinter import *

window = Tk()
window.title("Miles to Kilometer Converter")
window.config(padx=20, pady=20)
#window.minsize(300,300)

miles_input = Entry(width=7)
miles_input.grid(row=1, column=2)

miles_label = Label(text="Miles")
miles_label.grid(row=1, column=3)

equal_label =  Label(text="is equal to")
equal_label.grid(row=2, column=1)

result_label =  Label(text="0")
result_label.grid(row=2, column=2)

km_label =  Label(text="Km")
km_label.grid(row=2, column=3)

def convert_units():
    miles = float(miles_input.get())
    km = round(miles * 1.609)
    result_label.config(text=f"{km}")

calculate_button = Button(text="Calculate", command=convert_units)
calculate_button.grid(row=3, column=2)

window.mainloop()