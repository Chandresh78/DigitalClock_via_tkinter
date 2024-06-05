# we will use Tkinter Library: used for developing simple apps
from tkinter import Label, Tk
import time
app_window = Tk()
app_window.title("Digital Clock by Chandresh Rajpoot")
app_window.geometry("420x150") #by default in pixels
app_window.resizable(1,1)
text_font = ("Boulder", 70, 'bold')
background = "#2897e0"
foreground = "#1710e8"
border_width = 25

#Defining Grid
label = Label(app_window, font = text_font, bg = background, 
              fg = foreground, bd = border_width)
label.grid(row = 0, column = 1)

def digital_clock():
    time_live = time.strftime("%H:%M:%S")
    label.config(text = time_live)
    label.after(200, digital_clock)

digital_clock()
app_window.mainloop()
