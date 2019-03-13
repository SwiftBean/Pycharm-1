from tkinter import *

class Application(Frame):

    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.bttn_clicks = 0
        self.create_widgets()


    def create_widgets(self):

        self.lbl1 = Label(text = "Count")
        self.lbl2 = Label(text = str(self.bttn_clicks))
        self.lbl1.grid()
        self.lbl2.grid()
        """Create button which displays number of clicks."""
        self.bttn = Button(self)
        self.bttn["text"] = "Add"
        self.bttn["command"] = self.update_count
        self.bttn.grid()

        self.bttn1 = Button(self)
        self.bttn1["text"] = "Subtract"
        self.bttn1["command"] = self.update_count2
        self.bttn1.grid()

        self.bttn2 = Button(self)
        self.bttn2["text"] = "Multiply"
        self.bttn2["command"] = self.update_count3
    def update_count(self):
        self.bttn_clicks += 1
        self.lbl2["text"] = str(self.bttn_clicks)
    def update_count2(self):
        self.bttn_clicks -= 1
        self.lbl2["text"] = str(self.bttn_clicks)
    def update_count3(self):
        self.bttn_clicks *= 2


root = Tk()
root.title("Lazy Buttons 2")
root.geometry("250x350")
app = Application(root)

root.mainloop()