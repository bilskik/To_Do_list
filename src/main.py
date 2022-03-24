from tkinter import *
import os.path
from PIL import Image, ImageTk
import numpy

WIDTH = 600
HEIGHT = 600
LIST_Y = 40




class to_do_list():
    def __init__(self,list):
        self.list = list
        self.data = {}
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
        new_list_add = Button(window, text="Create new list", font=("Arial",30), bg="#00BFFF" ,command =
        lambda : [create_list(self.data).top(), self.add_to_list(), self.create_button_list(window)])
        new_list_add.place(x=30,y=520)
    def add_to_list(self):
        pass
    def create_button_list(self,window):
        global LIST_Y
        LIST_Y += 80
        List_button = Button(window,text= 'Lista_1' , font=("Arial",30), bg="#00BFFF", command = lambda : [self.read_from_file(), create_list(self.data).top()])
        List_button.place(x=30,y = LIST_Y)
    def read_from_file(self):
        self.data = numpy.load('created_data/1.txt.npy', allow_pickle='TRUE').item()
        print(self.data)

class create_list():
    def __init__(self,data):
        self.list =[]
        self.ENTRY_X = 20
        self.ENTRY_Y  = 75
        self.entry_list  = []
        self.sub_list = []
        self.data =  data
        self.counter =  0
        self.number_list = []
        self.NUMBER_INDEX =  0
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
        self.check_if_data_not_empty(nw)
        self.buttons(nw)

    def check_if_data_not_empty(self,nw):
        if self.data:
            for i in range(0,len(self.data)):
                self.ENTRY_Y += 35
                entry = Entry(nw, font=('Arial', 15), width=45, state=NORMAL)
                entry.insert(0,self.data[i])
                entry.config(state=DISABLED)
                self.entry_list.append(entry)
                sub_but = Button(nw, text='submit', command=lambda: self.data_add(entry))
                self.sub_list.append(sub_but)
                sub_but.place(x=520, y=self.ENTRY_Y)
                entry.place(x=40, y=self.ENTRY_Y)
                self.counter += 1
                self.numbernig(nw, 'add')

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
        quit_but = Button(nw, text = 'save&quit',font=("Arial",20),bg="#3ADF00",command = lambda : self.save_quit(nw))
        quit_but.place(x= 450, y =30)
    def save_quit(self,nw):
        numpy.save('created_data/1.txt',self.data)
        self.data.clear()
        nw.destroy()
    def entry_managment(self,nw, button):
        print(len(self.data))
        if button == 'add':
            self.data[self.counter]=''
            self.ENTRY_Y += 35
            entry = Entry(nw, font=('Arial', 15), width=45, state=DISABLED)
            self.entry_list.append(entry)
            sub_but = Button(nw,text='submit',command= lambda : self.data_add(entry))
            self.sub_list.append(sub_but)
            sub_but.place(x = 520, y = self.ENTRY_Y )
            entry.place(x=40, y=self.ENTRY_Y)
            self.counter += 1
            self.numbernig(nw,button)
        elif button == 'remove':
            if len(self.entry_list) == 0:
                pass
            else:
                for i in range(0,len(self.number_list)):
                    if self.number_list[i]['bg'] == '#FE2E2E':
                        if len(self.number_list) - 1 == i:
                            self.sub_list[i].destroy()
                            self.sub_list.pop(i)
                            self.entry_list[i].destroy()
                            self.entry_list.pop(i)
                            self.remove_data(i)
                            self.numbernig(nw,button)
                        else:
                            self.remove_data(i)
                            self.sub_list[i].destroy()
                            self.sub_list.pop(i)
                            self.entry_list[i].destroy()
                            self.entry_list.pop(i)
                            tmp = len(self.number_list) - i - 1
                            self.ENTRY_Y = self.ENTRY_Y - 35*tmp
                            list_length = len(self.sub_list) - 1
                            for j in range(i,len(self.number_list)):
                                if j > list_length:
                                    self.ENTRY_Y-=35
                                    break
                                self.sub_list[j].place(x = 520, y = self.ENTRY_Y)
                                self.entry_list[j].place(x = 40, y = self.ENTRY_Y)
                                self.ENTRY_Y += 35
                            self.number_list[-1].destroy()
                            self.number_list.pop()
                            break
        elif button == 'edit':
            if not len(self.entry_list) == 0:
                self.entry_list[self.NUMBER_INDEX-1].config(state=NORMAL)

    def remove_data(self,index):
        self.data.pop(index)
        self.counter -= 1
        a = len(self.data)
        dict = {}
        list_of_values = list(self.data.values())
        for i in range(0,a):
            dict[i] = ''
        for x in range(0,a):
            dict[x] = list_of_values[x]
        self.data = dict
        print(self.data)
    def data_add(self,entry):
        for i in range(0,len(self.number_list)):
            if self.number_list[i]['bg'] == '#FE2E2E':
                self.data[i] = entry.get()
                entry.config(state=DISABLED)
                break
        
    def numbernig(self,nw,button):
        if button == 'add':
            number = str(len(self.entry_list))
            label = Label(nw,text = number,font=('Arial',15), fg = 'black', bg = '#FE2E2E')
            label.place(x=10, y = self.ENTRY_Y)
            self.number_list.append(label)

            if not len(self.number_list) == 0:
                for i in range(0,len(self.number_list)):
                    if i == len(self.number_list) - 1:
                        self.number_list[i].config(bg='#FE2E2E')
                        break
                    else:
                        self.number_list[i].config(bg = '#2EFEF7')
                self.NUMBER_INDEX = len(self.number_list)
            else:
                self.NUMBER_INDEX += 1
        else:
            self.NUMBER_INDEX -= 1
            self.number_list[-1].destroy()
            self.number_list.pop()

            if not len(self.number_list) == 0:
                for i in range(0, len(self.number_list)):
                    if i == len(self.number_list) - 1:
                        self.number_list[i].config(bg='#FE2E2E')
                        break
                    else:
                        self.number_list[i].config(bg='#2EFEF7')
                self.NUMBER_INDEX = len(self.number_list)
            self.ENTRY_Y -= 35


    def choose_entry(self,nw, direction):
        if direction == 'up':
            if len(self.number_list) == self.NUMBER_INDEX:
                pass
            else:
                self.NUMBER_INDEX += 1
                for i in range(0,len(self.number_list)):
                    if i + 1 == self.NUMBER_INDEX:
                        self.number_list[i].config(bg='#FE2E2E')
                    else:
                        self.number_list[i].config(bg='#2EFEF7')
        elif direction == 'down':
            if self.NUMBER_INDEX == 1:
                pass
            else:
                self.NUMBER_INDEX -= 1
                for i in range(0, len(self.number_list)):
                    if i + 1 == self.NUMBER_INDEX:
                        self.number_list[i].config(bg='#FE2E2E')
                    else:
                        self.number_list[i].config(bg='#2EFEF7')

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