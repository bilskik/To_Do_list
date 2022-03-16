
from tkinter import *
import os.path
from PIL import Image, ImageTk

WIDTH = 600
HEIGHT = 600

class to_do_list():
    def __init__(self):
        pass
    def main_setting(self):
        window = Tk()
        window.geometry("600x600")
        window.title("To Do list")
        back_photo = (Image.open(os.path.join('bg.jpg')))
        resize = back_photo.resize((WIDTH,HEIGHT), Image.ANTIALIAS)
        new_image = ImageTk.PhotoImage(resize)
        my_canvas = Canvas(window, width = 600, height=600)
        my_canvas.pack(fill="both", expand=True)
        my_canvas.create_image(0,0,image=new_image, anchor="nw")
        my_canvas.create_text(300,50,text="To Do List", font=('Arial',40), fill="white")
        my_canvas.create_line(0,100,600,100,width='5')
        self.buttons(window)


        window.mainloop()

    def buttons(self, window):
        new_list_add = Button(window, text="Create new list", font=("Arial",30), bg="#00BFFF" ,command = lambda : create_list.top(window))
        new_list_add.place(x=30,y=520)

class create_list():
    def __init__(self,window):
        self.window = window
    def top(self):
        nw = Toplevel()
        nw.geometry("600x600")
        nw.title("list")
        self.buttons(nw)

    def buttons(self, nw):
        add_butt = Button(nw, text="Add", font=('Arial', 30), bg="#3ADF00", command=lambda: self.add_to_list())
        add_butt.place(x=300, y=200)

    def add_to_list(self):
        pass

def main():
    main_window = to_do_list()
    main_window.main_setting()
if __name__ == "__main__":
        main()