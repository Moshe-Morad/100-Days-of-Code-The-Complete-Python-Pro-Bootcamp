from tkinter import *

window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)

# Label

my_label = Label(text="I Am a Label", font=("Ariel", 24, "bold"))
my_label.pack()

my_label["text"] = "New Text"
my_label.config(text="New Text")


def button_clicked():
    print("I got clicked")
    new_text = entry.get()
    my_label.config(text=new_text)


# Button
button = Button(text="Click Me", command=button_clicked)
button.pack()

# Entry

entry = Entry(width=30)
entry.insert(END, string="Some text to begin with.")
print(entry.get())
entry.pack()

text = Text(height=5, width=30)
text.focus()
text.insert(END, "Example of multi-line text entry.")
print(text.get("1.0", END))
text.pack()


def spinbox_used():
    # gets the current value in spinbox
    print(spin_box.get())


spin_box = Spinbox(from_=0, to=10, width=5, command=spinbox_used)
spin_box.pack()


def scale_used(value):
    print(value)


scale = Scale(from_=0, to=100, command=scale_used)
scale.pack()


def checkbutton_used():
    # print 1 if on button checked, else 0.
    print(check_state.get())


# variable to hold on to checked state, 0 is off, 1 is on.
check_state = IntVar()
check_button = Checkbutton(text="Is On?", variable=check_state, command=checkbutton_used)
check_state.get()
check_button.pack()


def radio_used():
    print(radio_state.get())


radio_state = IntVar()
radio_button1 = Radiobutton(text="Option1", value=1, variable=radio_state, command=radio_used)
radio_button2 = Radiobutton(text="Option2", value=2, variable=radio_state, command=radio_used)
radio_button1.pack()
radio_button2.pack()


def listbox_used(event):
    # Gets current selection from listbox
    print(list_box.get(list_box.curselection()))


list_box = Listbox(height=4)
fruits = ["Apple", "Pear", "Orange", "Banana"]
for item in fruits:
    list_box.insert(fruits.index(item), item)
list_box.bind("<<ListboxSelect>>", listbox_used)
list_box.pack()




# window = Tk()
# window.title("My First GUI Program")
# window.minsize(width=500, height=300)
# window.config(padx=20, pady=20)
#
# # Label
#
# my_label = Label(text="I Am a Label", font=("Ariel", 24, "bold"))
# my_label.config(text="New Text")
# my_label.grid(column=0, row=0)
#
#
# # Button
# button = Button(text="Click Me", command=button_clicked)
# button.grid(column=1, row=1)
#
# new_button = Button(text="Click Me", command=button_clicked)
# new_button.grid(column=2, row=0)
#
# # Entry
#
# entry = Entry(width=10)
# print(entry.get())
# entry.grid(column=3, row=2)









window.mainloop()
