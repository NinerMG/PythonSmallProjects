from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)


#Label

my_label = Label(text="I am a label", font=("Arial", 24, "bold"))
my_label.grid(row=0, column=1)

my_label["text"] = "New Text"
my_label.config(text="Test")

#Button
def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click me", command=button_clicked)
button.grid(row=2, column=2)

button_two = Button(text="New Button")
button_two.grid(row=1, column=3)

#Entry

input = Entry(width=10)
input.grid(row=3, column=4)
print(input.get())

window.mainloop()