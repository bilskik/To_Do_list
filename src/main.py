from tkinter import *
import os.path
from PIL import Image, ImageTk

WIDTH = 600
HEIGHT = 600
ENTRY_X = 20
ENTRY_Y = 75
LIST_Y = 40
entry_list = []
sub_list = []
data = []
number_list = []
NUMBER_INDEX = 0

class to_do_list():
    def __init__(self,list):
        self.list = list
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

        new_list_add = Button(window, text="Create new list", font=("Arial",30), bg="#00BFFF" ,command = lambda : [create_list(list).top(), self.add_to_list(), self.create_button_list(window)])
        new_list_add.place(x=30,y=520)

    def add_to_list(self):
        pass
    def create_button_list(self,window):
        global LIST_Y
        LIST_Y += 80
        List_button = Button(window,text= 'Lista_1' , font=("Arial",30), bg="#00BFFF")
        List_button.place(x=30,y = LIST_Y)
class create_list():
    def __init__(self, list):
        self.list = list
    def top(self):
        global back_photo
        global img
        global back_canvas
        nw = Toplevel()
        nw.geometry("600x600")
        nw.title("list")
        back_photo = (Image.open(os.path.join('note.png')))
        resize = back_photo.resize((WIDTH, HEIGHT), Image.ANTIALIAS)
        img = ImageTk.PhotoImage(resize)
        back_canvas = Canvas(nw, width=600, height=600)
        back_canvas.pack()
        back_canvas.create_image(0,0,image=img,anchor='nw')
        back_canvas.image = img
        back_canvas.create_text(150,50,text="Lista 1: ", font=('Arial',30),fill='black')
        self.buttons(nw)

    def buttons(self,nw):
        add_butt = Button(nw, text="Add", font=('Arial', 30), bg="#3ADF00",command = lambda : self.entry_managment(nw,'add'))
        add_butt.place(x=50, y=500)
        edit_butt = Button(nw,text="Edit", font=('Arial',30),bg="#3ADF00", command=lambda : self.entry_managment(nw,'edit'))
        edit_butt.place(x=150,y=500)
        remove_butt = Button(nw, text = "Remove", font=("Arial",30),bg="#3ADF00", command = lambda : self.entry_managment(nw,'remove'))
        remove_butt.place(x=250,y=500)
        up_butt = Button(nw, text = '\u2191',bg="#3ADF00", command = lambda : self.choose_entry(nw,'up'))
        up_butt.place(x=450,y=500)
        down_butt = Button(nw, text = '\u2193',bg="#3ADF00",command = lambda : self.choose_entry(nw,'down'))
        down_butt.place(x=450,y=530)
        #quit_but = Button(nw, text = 'save&quit',font=("Arial",20),bg="#3ADF00",command = lambda : self.save_quit(nw))
       # quit_but.place(x= 450, y =30)
    '''
    def save_quit(self,nw):
        global entry_list
        global data
        global number_list
        global sub_list
        global NUMBER_INDEX
        data.clear()
        number_list.clear()
        sub_list.clear()
        NUMBER_INDEX = 0
        nw.destroy()
    '''
    def entry_managment(self,nw, button):
        global ENTRY_Y
        global entry_list
        global data
        global number_list
        global NUMBER_INDEX
        print(len(data))
        if button == 'add':
            ENTRY_Y += 35
            entry = Entry(nw, font=('Arial', 15), width=45, state=DISABLED)
            entry_list.append(entry)
            sub_but = Button(nw,text='submit',command= lambda : self.data_add(entry))
            sub_list.append(sub_but)
            sub_but.place(x = 520, y = ENTRY_Y )
            entry.place(x=40, y=ENTRY_Y)
            self.numbernig(nw,button)
        elif button == 'remove':
            if len(entry_list) == 0:
                pass
            else:
                for i in range(0,len(number_list)):
                    if number_list[i]['bg'] == '#FE2E2E':
                        if len(number_list) - 1 == i:
                            sub_list[i].destroy()
                            sub_list.pop(i)
                            entry_list[i].destroy()
                            entry_list.pop(i)
                            self.numbernig(nw,button)
                        else:
                            sub_list[i].destroy()
                            sub_list.pop(i)
                            entry_list[i].destroy()
                            entry_list.pop(i)
                            tmp = len(number_list) - i - 1
                            ENTRY_Y = ENTRY_Y - 35*tmp
                            list_length = len(sub_list) - 1
                            for j in range(i,len(number_list)):
                                if j > list_length:
                                    ENTRY_Y-=35
                                    break
                                sub_list[j].place(x = 520, y = ENTRY_Y)
                                entry_list[j].place(x = 40, y =ENTRY_Y)
                                ENTRY_Y += 35
                            number_list[-1].destroy()
                            number_list.pop()
                            break
        elif button == 'edit':
            if not len(entry_list) == 0:
                entry_list[NUMBER_INDEX-1].config(state=NORMAL)

    def data_add(self,entry):
        global data
        global sub_list
        data.append(entry.get())
        entry.config(state=DISABLED)
    def numbernig(self,nw,button):
        global entry_list
        global ENTRY_Y
        global number_list
        global NUMBER_INDEX
        if button == 'add':
            number = str(len(entry_list))
            label = Label(nw,text = number,font=('Arial',15), fg = 'black', bg = '#FE2E2E')
            label.place(x=10, y = ENTRY_Y)
            number_list.append(label)

            if not len(number_list) == 0:
                for i in range(0,len(number_list)):
                    if i == len(number_list) - 1:
                        number_list[i].config(bg='#FE2E2E')
                        break
                    else:
                        number_list[i].config(bg = '#2EFEF7')
                NUMBER_INDEX = len(number_list)
            else:
                NUMBER_INDEX += 1
        else:
            NUMBER_INDEX -= 1
            number_list[-1].destroy()
            number_list.pop()

            if not len(number_list) == 0:
                for i in range(0, len(number_list)):
                    if i == len(number_list) - 1:
                        number_list[i].config(bg='#FE2E2E')
                        break
                    else:
                        number_list[i].config(bg='#2EFEF7')
                NUMBER_INDEX = len(number_list)
            ENTRY_Y -= 35


    def choose_entry(self,nw, direction):
        global entry_list
        global number_list
        global NUMBER_INDEX
        global data
        if direction == 'up':
            if len(number_list) == NUMBER_INDEX:
                pass
            else:
                NUMBER_INDEX += 1
                for i in range(0,len(number_list)):
                    if i + 1 == NUMBER_INDEX:
                        number_list[i].config(bg='#FE2E2E')
                    else:
                        number_list[i].config(bg='#2EFEF7')
        elif direction == 'down':
            if NUMBER_INDEX == 1:
                pass
            else:
                NUMBER_INDEX -= 1
                for i in range(0, len(number_list)):
                    if i + 1 == NUMBER_INDEX:
                        number_list[i].config(bg='#FE2E2E')
                    else:
                        number_list[i].config(bg='#2EFEF7')

class Node:
    def __init__(self,data,index):
        self.data = data
        self.index = index
        self.next = None
        self.prev = None
class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
    def append_last(self,data,index):
        newnode = Node(data,index)
        newnode.next = None
        if self.head is None:
            newnode.prev = None
            self.head = newnode
            return
        last = self.head
        while(last.next is not None):
            last = last.next
        last.next = newnode
        newnode.prev = last
        return

def main():
    main_list = DoublyLinkedList()
    main_window = to_do_list(main_list)
    main_window.main_setting()
if __name__ == "__main__":
        main()