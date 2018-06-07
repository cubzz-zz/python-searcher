from tkinter import *

tker = Tk("My Searcher App")
frame = Frame(tker, width=900, height=850)

labels = list()


def print_name(event):
    print("Hi")


def print_name_2(event):
    print("Hi-yo")


label_1 = Label(frame, text="name:")
label_2 = Label(frame, text="password:")
entry_1 = Entry(frame)
entry_2 = Entry(frame)
c = Checkbutton(frame, text="Keep me logged in")
button = Button(frame, text="press")
button.bind("<Control-Button-1>", print_name)
button.bind("<Button-1>", print_name_2)

frame.grid()
label_1.grid(row=0, sticky=E)
label_2.grid(row=1, sticky=E)
entry_1.grid(row=0, column=1)
entry_2.grid(row=1, column=1)
c.grid(row=2, columnspan=2)
button.grid(row=3, column=1, columnspan=2)


if __name__ == '__main__':
    tker.mainloop()