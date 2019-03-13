from tkinter import *

class Application(Frame):

    def __init__(self, master):
        """Initialize the frame."""
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        #create instruction label
        self.inst_lbl = Label(self, text = "Enter password fo the secret life")
        self.inst_lbl.grid(row = 1, column = 0, columnspan = 2, sticky = W)
        #create password
        self.pw_lbl = Label(self, text = "Password: ")
        self.pw_lbl.grid(row = 2, column = 0, sticky = W)

        self.pw_ent = Entry(self)
        self.pw_ent.grid(row = 3, column = 1, sticky = W)

        self.submit_buttn = Button(self, text = "Submit", command = self.reveal)
        self.submit_buttn.grid(row= 3, column = 0, sticky = W)

        #create text widget to display message
        self.secret_txt = Text(self, width = 35, height = 5, wrap = WORD)
        self.secret_txt.grid(row = 4, column = 0, columnspan = 2, sticky = W)


    def reveal(self):
        contents = self.pw_ent.get()
        if contents == "secret":
            message = "42"
        else:
            message = "That's not the correct password, so I can't share the secret with you."
        self.secret_txt.delete(0.0, END)
        self.secret_txt.insert(0.0, message)



root = Tk()
root.title("Secret of Life")
root.geometry("350x345")

app = Application(root)

root.mainloop()