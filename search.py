from tkinter import *

root = Tk("My Searcher App")

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack(side=BOTTOM)

top_buttons = list()
bot_buttons = list()

top_buttons.append(Label(topFrame, text="Click 1", fg="red", bg="red"))
top_buttons.append(Label(topFrame, text="Click 2", fg="blue", bg="blue"))
top_buttons.append(Label(topFrame, text="Click 3", fg="green", bg="green"))
bot_buttons.append(Label(bottomFrame, text="Click 4", fg="purple"))

for b in top_buttons:
    b.pack(side=LEFT, fill=X)
for b in bot_buttons:
    b.pack(side=BOTTOM)

if __name__ == '__main__':
    root.mainloop()