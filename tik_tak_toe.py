import tkinter as tk
from threading import Thread
import random
import time
import datetime


class Game(tk.Tk):
    def __init__(self,player):
        super().__init__()
        self.title("Tik Tak Toe")
        #main.geometry("450x450")
        if player=="X" or player=='x':
            self.player="X"
            self.color="green"
            self.Trun=False
        elif player=="O" or player=='o':
            self.player="O"
            self.color='blue'
            self.Trun=True
        else:
            raise Exception('player must be x , X , o , O')
        self.Status=True
        self.configure(background="light green")
        self.fr=tk.Frame(master=self,width=450,height=450,)
        self.cells=[[square(self.fr,text='',width=10,height=5,bg='white',x=i,y=j) for i in range(3)] for j in range(3)]
        

    def start_new_game(self):
        self.cells=[[square(self.fr,text='',width=10,height=5,bg='white',x=i,y=j) for i in range(3)] for j in range(3)]

    def check_game(self):
        pass



class square(tk.Label):
    def __init__(self,master,text='',width=30,height=15,bg='red',x=0,y=0):
        super().__init__(master=master,text=text,width=width,height=height,bg=bg)
        self.text=text
        #self.width=width
        #self.height=height
        #self.bg=bg
        self.x=x
        self.y=y
        #self.active=False
        self.bind('<Button-1>', self.mouve)
    
    def mouve(self,*args):
        # print(args)
        # print(self.x,self.y,self.freeze)
        if (self.master.Turn):
            if self.text=='':
                self.text=self.master.player
                self['bg']=self.master.color
                self.master.

            if self.master.master.check_game():
                """
                self.master.master.end=time.strftime('%c')
                f=open('score.txt','a')
                f.write(self.master.master.start+'\t'+self.master.master.end+'\n')
                self.master.master.start_new_game()
                """


            
class My_game(tk.Tk,Thread):
    def __init__(self):
        super().__init__()
        self.title("Square Game")
        #main.geometry("450x450")
        self.configure(background="light green")
        self.fr=tk.Frame(master=self,width=450,height=450,bg='white')

    def start_new_game(self):
        self.start=time.strftime('%c')
        self.fr.destroy()
        self.fr=tk.Frame(main,width=450,height=450,bg='white')
        num=list(range(1,9))
        rand_num=[]
        for i in range(8):
            ch=random.choice(num)
            num.remove(ch)
            rand_num.append(ch)
        self.numbers=[square(self.fr,text=str(rand_num[i]),width=10,height=5,bg='red',x=i//3,y=i%3) for i in range(8)]
        for i,j in enumerate(self.numbers):
            j.grid(row=i//3,column=i%3,padx=5,pady=5)
        self.fr.pack()

    def check_game(self):
        for j in self.numbers:
            print(str((j.x*3+j.y)+1),j.text)
            if str((j.x*3+j.y)+1)!=j.text:
                return False
        return True

main=My_game()
main.start_new_game()
main.mainloop()