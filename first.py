from tkinter import *

class Window(Frame):
    def __init__(self, master=None):
        root.geometry('300x300')
        Frame.__init__(self, master)
        self.master = master
        Label(root,text ="Bienvenue dans YTDown, taper le nom de la vidéo que vous voulez télécharger ")
        Label(root,text = "URL" ).grid(row =0)
        ent1= Entry(root)
        ent1.grid(row=0, column=1) 
# initialize tkinter
root = Tk()
app = Window(root)

# set window title
root.wm_title("YTDown")

# show window
root.mainloop()