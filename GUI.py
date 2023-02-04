from tkinter import ttk
from tkinter import *
from PIL import ImageTk, Image

window = Tk()
window.geometry("600x400")
window.title("Youtube Downloader")
window.configure(background='#252525')

s = ttk.Style()
s.configure('TFrame', background='#252525')

frame = ttk.Frame(window,padding=5)
frame.grid(row=0, column=0)
frame.place(relx=.5, rely=0.5, anchor=CENTER)

imge = Image.open("Youtube-logo-vector-PNG.png")
ytlogo = imge.resize((300,300))
img = ImageTk.PhotoImage(ytlogo)

label = Label(frame, image = img, background='#252525').grid(column=0, row=0, columnspan=3, pady=0, padx=50)

field = ttk.Entry(frame)                   
field.grid(column=0, row=1, columnspan=3, sticky="nsew", ipady=5)

ttk.Button(frame, text="New Download", command=lambda:field.delete(0,'end'), padding=4).grid(column=0, row=2, sticky="W", pady=5)
ttk.Button(frame, text="360p", command=lambda:field.delete(0,'end'), padding=4).grid(column=1, row=2, sticky="E", pady=5)
ttk.Button(frame, text="720p", command=lambda:field.delete(0,'end'), padding=4).grid(column=2, row=2, sticky="WE", pady=5)

window.minsize(600,400)
window.maxsize(600,400)
window.mainloop()