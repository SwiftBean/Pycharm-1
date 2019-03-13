#Clock Using tkinter
#Zach
###########################################################################################
#imports
from tkinter import *
from datetime import datetime
import time
###########################################################################################
#Defining The Root
root = Tk()
root.geometry("500x500")
###########################################################################################
#Creating The Clock
time1 = ''
clock = Label(root, font=('Helvetica', 20, 'bold'), bg='black', foreground = "White")
clock.pack(fill=BOTH, expand=1)
###########################################################################################
#Displaying The Clock
def tick():
    global time1
    # receives the current time
    now = datetime.now()
    now.strftime("%m/%d/Y, %I:%M:%S")
    # if time string has changed, update it
    if now != time1:
        time1 = now
        clock.config(text=now)
    clock.after(200, tick)
tick()
root.mainloop(  )