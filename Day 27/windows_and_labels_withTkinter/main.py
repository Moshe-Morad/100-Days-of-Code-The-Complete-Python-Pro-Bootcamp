from tkinter import *


def button_clicked():
    print("I got clicked")
    mile = int(entry.get())
    km = mile * 1.609344
    label_2.config(text=km)


window = Tk()
window.title("My First GUI Program")
window.minsize(width=500, height=300)
window.config(padx=20, pady=20)

# Label

label_0 = Label(text="Miles", font=("Ariel", 24, "bold"))
label_0.grid(column=2, row=0)

label_1 = Label(text="is equal to ", font=("Ariel", 24, "bold"))
label_1.grid(column=0, row=1)

label_2 = Label(text=" ", font=("Ariel", 24, "bold"))
label_2.grid(column=1, row=1)

label_3 = Label(text="Km", font=("Ariel", 24, "bold"))
label_3.grid(column=2, row=1)


# Button
button = Button(text="Calculate", command=button_clicked)
button.grid(column=1, row=2)


# Entry

entry = Entry(width=10)
print(entry.get())
entry.grid(column=1, row=0)






window.mainloop()
