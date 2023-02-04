from tkinter import ttk
from tkinter import *

window = Tk()
window.geometry("900x500")

frame = ttk.Frame(window, padding=20)
frame.place(relx=0.5, rely=0.5, anchor=CENTER)

ttk.Label(frame, text="Hello World!")                   .grid(column=0, row=0)
ttk.Button(frame, text="Quit", command=window.destroy)  .grid(column=1, row=0)

window.minsize(900,500)
window.mainloop()