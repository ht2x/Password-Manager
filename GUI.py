from tkinter import ttk         #importing tkinter for GUI
from tkinter import *           #//
from tkinter import messagebox  #//
from PIL import ImageTk, Image  #importing PILLOW for image editing
from Downloader import InitailizeDownload, DownloadInProgress #importing our custom module to download youtube videos
import os; username = os.getlogin() #import os library to get the username of the user

window = Tk()   #initializing the window
window.geometry("600x400") #setting the window size
window.title("Youtube Downloader") #setting the window's title
window.configure(background='#252525') #setting the window's background color to dark gray (#252525)

s = ttk.Style() #initializing the style object to make every object's background color as dark gray
s.configure('TFrame', background='#252525') #creating the master Frame style, so every frame have the same background by default
s.configure('First.TFrame', background='#FFFFFF') #creating a child Frame style which makes the desired Frame White
ttk.Style().configure("TButton", padding=4, background="#252525") #creating the master Button style

frame = ttk.Frame(window,padding=5) #creating the frame
frame.grid(row=0, column=0) #assign the frame to the grid
frame.place(relx=.5, rely=0.5, anchor=CENTER) #place the frame in the center

original_image = Image.open("Youtube-logo-vector-PNG.png") #open the image file in the program : PIL
ytlogo = original_image.resize((300,300)) #modify the image size to 300p x 300p and assign it to 'ytlogo'
img = ImageTk.PhotoImage(ytlogo) #turn the 'ytlogo' object to be compatible with TKinter
label = Label(frame, image = img, background='#252525').grid(column=0, row=0, columnspan=3, pady=0, padx=50) #create a label object and assign the image to it

field = ttk.Entry(frame) #making an entry field to allow the user to copy and paste the Link in
field.grid(column=0, row=1, columnspan=3, sticky="nsew", ipady=5) #assing the field to the grid and making it span over 3 columns

def EvaluateOutcome(metaData): #function to allow error handling by a code 
    if metaData.code == 200: # success
        try:
            if DownloadInProgress(metaData.videos, metaData.quality) == 200: #Download the video then evaluate the code
                os.system(f'start {os.path.realpath(f"C:/Users/{username}/Videos")}') #open the file location
            else:
                messagebox.showerror("error", "There was an error while downloading the video.\n Please check your internet connection. (error code: 503)")
        except:
            messagebox.showerror("error", "There was an error while downloading the video.\n Please check your internet connection. (error code: 511)")
    elif metaData.code == 400: # faliure
        messagebox.showerror("error", f"There was a connection error.\n(error code: {metaData.code})")
    elif metaData.code == 401: # faliure
        messagebox.showerror("error", f"You cannot submit an empty link.\n (error code: {metaData.code})")
    elif metaData.code == 402: # faliure
        messagebox.showerror("error", f"You can only download from 'youtube.com'.\n (error code: {metaData.code})")
    else: # faliure
        messagebox.showerror("error", f"there was an unknown error, Please contact developer.\n (error code: {metaData.code})")

ttk.Button(frame, text="New Download", command=lambda:field.delete(0,'end')).grid(column=0, row=2, sticky="W", pady=5) #make a button
ttk.Button(frame, text="360p", command=lambda:EvaluateOutcome(InitailizeDownload(field.get(), 360))).grid(column=1, row=2, sticky="E", pady=5) #make a button
ttk.Button(frame, text="720p", command=lambda:EvaluateOutcome(InitailizeDownload(field.get(), 720))).grid(column=2, row=2, sticky="WE", pady=5) #make a button

window.minsize(600,400) #set the minimum size of the window
window.maxsize(600,400) #set the maximum size of the window
window.mainloop() # START THE PROGRAM