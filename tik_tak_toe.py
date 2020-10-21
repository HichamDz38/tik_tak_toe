import tkinter as tk
import tkinter.messagebox
from threading import Thread
import random
import time
import datetime

class Game(tk.Tk):
    def __init__(self,player):
        super().__init__()
        self.title("Tik Tak Toe")
        # main.geometry("450x450")
        if player=="X" or player=='x':
            self.player="X"
            self.color="green"
            self.Turn=False
        elif player=="O" or player=='o':
            self.player="O"
            self.color='blue'
            self.Turn=True
        else:
            raise Exception('player must be x , X , o , O')
        self.Status=True
        self.configure(background="light green")
        self.fr=tk.Frame(master=self,width=450,height=450,)
        self.cells=[[square(self.fr,text=' ',width=10,height=5,bg='white',x=i,y=j) for i in range(3)] for j in range(3)]

    def start_new_game(self,*args):
        self.fr.destroy()
        self.fr=tk.Frame(main,width=450,height=450,bg='light green')
        self.cells=[[square(self.fr,text=' ',width=10,height=5,bg='white',x=i,y=j) for i in range(3)] for j in range(3)]
        
        for i in range(3):
            for j in range(3):
                self.cells[i][j].grid(row=i,column=j,padx=5,pady=5)
        self.fr.pack()

    def check_game(self,*args):
        print("chck game called")
        for i in range(3):
            # print(self.cells[i][0]['text'],self.cells[i][1]['text'],self.cells[i][2]['text'])
            # print(self.cells[0][i]['text'],self.cells[1][i]['text'],self.cells[2][i]['text'])

            # print(self.cells[i][0]['text']==self.cells[i][1]['text']==self.cells[i][2]['text'] and self.cells[i][0]['text']!=' ')
            # print(self.cells[0][i]['text']==self.cells[1][i]['text']==self.cells[2][i]['text'] and self.cells[i][0]['text']!=' ')

            if self.cells[i][0]['text']==self.cells[i][1]['text']==self.cells[i][2] and self.cells[i][0]['text']!=' ':
                print('horizental match')
                self.Status=False
                return True
            
            elif (self.cells[0][i]['text']==self.cells[1][i]['text']==self.cells[2][i]['text'] and self.cells[0][i]['text']!=' '):
                print('virtical match')
                self.Status=False
                return True
        # print(self.cells[0][0]['text']==self.cells[1][1]['text']==self.cells[2][2]['text'] and self.cells[i][0]['text']!=' ')
        # print(self.cells[0][2]['text']==self.cells[1][1]['text']==self.cells[2][0]['text'] and self.cells[i][0]['text']!=' ')
        if self.cells[0][0]['text']==self.cells[1][1]['text']==self.cells[2][2]['text'] and self.cells[0][0]['text']!=' ':
                self.Status=False
                print('diagonal match')
                return True
        
        elif self.cells[0][2]['text']==self.cells[1][1]['text']==self.cells[2][0]['text'] and self.cells[2][0]['text']!=' ':
                self.Status=False
                print('diagonal2 match')
                return True
        return False

    def profile(self,*args):
        try:
            f=open("setting.txt","r")
            data=f.read()
            print(data)
            if not(data):
                data=' '
            f.close()
        except:
            data=' '
        self.fr.destroy()
        self.fr=tk.Frame(main,width=450,height=450,bg='light green')
        self.lbl1=tk.Label(master=self.fr,text='Name',width=30,height=1,bg='magenta')
        self.lbl1.pack(padx=5,pady=5)
        self.ent1=tk.Entry(master=self.fr,width=30,bg='white')
        self.ent1.insert(0,data)
        self.ent1.pack(padx=5,pady=5)
        self.btn1=tk.Button(master=self.fr,text='Save',width=30,height=1,bg='magenta')
        self.btn1.pack(padx=5,pady=5)
        self.btn1.bind('<Button-1>', self.Save_profile)
        self.btn2=tk.Button(master=self.fr,text='Return',width=30,height=1,bg='magenta')
        self.btn2.pack(padx=5,pady=5)
        self.btn2.bind('<Button-1>', self.Menu)
        self.lbl1.pack()
        self.ent1.pack()
        self.btn1.pack()
        self.btn2.pack()
        self.fr.pack()

    def Save_profile(self,*args):
        f=open("setting.txt","w")
        f.write(self.ent1.get())
        f.close()
        tkinter.messagebox.showinfo(message='profile name has been saved')

    def Menu(self,*args):
        self.fr.destroy()
        self.fr=tk.Frame(main,width=450,height=450,bg='light green')
        lbl1=tk.Button(master=self.fr,text='Start New GAmE',width=30,height=3,bg='magenta')
        lbl2=tk.Button(master=self.fr,text='Join Another gAmE',width=30,height=3,bg='magenta')
        lbl3=tk.Button(master=self.fr,text='Watch GaME',width=30,height=3,bg='magenta')
        lbl4=tk.Button(master=self.fr,text='Profile',width=30,height=3,bg='magenta')
        lbl5=tk.Button(master=self.fr,text='Quit GaMe',width=30,height=3,bg='magenta')
        lbl1.pack(padx=5,pady=5)
        lbl1.bind('<Button-1>', self.start_new_game)
        lbl2.pack(padx=5,pady=5)
        lbl3.pack(padx=5,pady=5)
        lbl4.pack(padx=5,pady=5)
        lbl4.bind('<Button-1>', self.profile)
        lbl5.pack(padx=5,pady=5)
        lbl5.bind('<Button-1>', lambda x:self.destroy())
        self.fr.pack()

class square(tk.Label):
    def __init__(self,master,text=' ',width=30,height=15,bg='red',fg='black',x=0,y=0,font="Helvetica 14 bold italic"):
        super().__init__(master=master,text=text,width=width,height=height,bg=bg)
        self['text']=text
        # self.width=width
        # self.height=height
        # self.bg=bg
        self.x=x
        self.y=y
        # self.active=False
        self.bind('<Button-1>', self.mouve)
    
    def mouve(self,*args):
        if (self.master.master.Turn):
            if self['text']==' ' and self.master.master.Status:
                self['text']=self.master.master.player
                self['bg']=self.master.master.color
                self['font']="Helvetica 10"
                #self.master.master.Turn=False
                if(self.master.master.player=="O"):
                    self.master.master.player="X"
                    self.master.master.color='orange'
                elif(self.master.master.player=="X"):
                    self.master.master.player="O"
                    self.master.master.color='blue'
            if self.master.master.check_game():
                """
                self.master.master.end=time.strftime('%c')
                f=open('score.txt','a')
                f.write(self.master.master.start+'\t'+self.master.master.end+'\n')
                self.master.master.start_new_game()
                """
                print('the player {} won the game'.format(self.master.master.player))
                tkinter.messagebox.showinfo(message='the player '+self.master.master.player+' won the game')
                
                #time.sleep(5)
                self.master.master.Status=False
                self.master.master.start_new_game()


main=Game(player="O")
main.Menu()
main.mainloop()