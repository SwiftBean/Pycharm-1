# Simple GUI
#Demonstrates creating a window

from tkinter import *

#create the root window
root = Tk()

#modify the window
#photo = PhotoImage(file = "Blue-And-Black-Wallpaper-21-1920x1080.jpg")
#label = Label(root, image = photo)
root.title("Simple GUI")
root.geometry("500x300")
root.configure(bg = "green")
#root.wm_iconbitmap("")

app = Frame(root)
app.grid()

#create a label in the frame
label = Label(app, text = "This is a fancy Label")
lbl = Label(app, text = "I'm a label!")
lbl2= Label(app, text = "Another one!",)
lbl2.grid()
label.grid()
lbl.grid()
label.config(font = ("Courier", 44))
label.config(bg = "black")
label.config(foreground = "red")

#kick off the window's event-loop
root.mainloop()
