from tkinter import ttk
from tkinter import *
from tkinter import messagebox
from PIL import ImageTk, Image
from Downloader import *
import os; username = os.getlogin()

window = Tk()
window.geometry("600x400")
window.title("Youtube Downloader")
window.configure(background='#252525')

s = ttk.Style()
s.configure('TFrame', background='#252525')
s.configure('First.TFrame', background='#FFFFFF')
ttk.Style().configure("TButton", padding=4, background="#252525")

frame = ttk.Frame(window,padding=5)
frame.grid(row=0, column=0)
frame.place(relx=.5, rely=0.5, anchor=CENTER)

imge = Image.open("Youtube-logo-vector-PNG.png")
ytlogo = imge.resize((300,300))
img = ImageTk.PhotoImage(ytlogo)
label = Label(frame, image = img, background='#252525').grid(column=0, row=0, columnspan=3, pady=0, padx=50)

field = ttk.Entry(frame)
field.grid(column=0, row=1, columnspan=3, sticky="nsew", ipady=5)

def InitializePopUp(title:str, message:str):
    top = Toplevel(window)
    top.title("success")
    top.geometry("300x150")
    top.minsize(300,150)
    top.maxsize(300,150)

    popUpFrame = ttk.Frame(top, style='First.TFrame')
    popUpFrame.place(relx=.5, rely=0.5, anchor=CENTER)

    field.delete(0,'end')
    Label(popUpFrame, text=f"Your download is finished.\n You can find the file in: C:/Users/{username}/Videos").grid(column=0, row=0, columnspan=2)
    ttk.Button(popUpFrame, text= "Close", command=top.destroy).grid(column=0, row=1, padx=5)
    ttk.Button(popUpFrame, text= "Open File Location", command=lambda:os.system(f'start {os.path.realpath(f"C:/Users/{username}/Videos")}')).grid(column=1, row=1, padx=5)

def EvaluateOutcome(code:int):
    if code == 200:
        InitializePopUp("success", f"Your download is finished.\n You can find the file in: C:/Users/{username}/Videos")
    elif code == 400:
        messagebox.showerror("error", f"There was a connection error.\n(error code {code})")
    elif code == 401:
        messagebox.showerror("error", f"You cannot submit an empty link.\n (error code {code})")
    elif code == 402:
        messagebox.showerror("error", f"You can only download from 'youtube.com'.\n (error code {code})")
    else:
        messagebox.showerror("error", f"there was an unknown error, Please contact developer.\n (error code {code})")

ttk.Button(frame, text="New Download", command=lambda:field.delete(0,'end')).grid(column=0, row=2, sticky="W", pady=5)
ttk.Button(frame, text="360p", command=lambda:EvaluateOutcome(DownloadVideo(field.get(), 360))).grid(column=1, row=2, sticky="E", pady=5)
ttk.Button(frame, text="720p", command=lambda:EvaluateOutcome(DownloadVideo(field.get(), 720))).grid(column=2, row=2, sticky="WE", pady=5)

window.minsize(600,400)
window.maxsize(600,400)
window.mainloop()