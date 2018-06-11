from tkinter import *
from tkinter import ttk

root = Tk("My Searcher App")
content = ttk.Frame(root, padding=(3,3,12,12))
graph = ttk.Frame(content)

sel = StringVar()

dsp_cb = ttk.Radiobutton(content, text="DSP", variable=sel, value='d')
asp_cb = ttk.Radiobutton(content, text="A*", variable=sel, value='a')
start = ttk.Button(content, text="Start")

node_buttons = list()
config_buttons = list()

graph.grid(row=0, column=0, columnspan=3, rowspan=3, sticky=(N, S, E, W))
content.grid(column=0, row=0, sticky=(N, S, E, W))
graph.grid(column=0, row=0, columnspan=3, rowspan=2, sticky=(N, S, E, W))

dsp_cb.grid(column=0, row=3)
asp_cb.grid(column=1, row=3)
start.grid(column=3, row=3)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
graph.columnconfigure(0, weight=3)
graph.columnconfigure(1, weight=3)
graph.columnconfigure(2, weight=1)


if __name__ == '__main__':
    root.mainloop()
