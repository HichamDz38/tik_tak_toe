import tkinter as tk
import tkinter.messagebox
from threading import Thread
import random
import time
import datetime
import socket


class Game(tk.Tk):
    def __init__(self, player=""):
        super().__init__()
        self.title("Tik Tak Toe")
        self.Turn = False
        # main.geometry("450x450")
        # if player=="X" or player=='x':
        #     self.player="X"
        #     self.color="orange"
        # elif player=="O" or player=='o':
        #     self.player="O"
        #     self.color='blue'
        # else:
        #     raise Exception('player must be x , X , o , O')
        self.Status = True
        self.configure(background="light green")
        self.fr = tk.Frame(master=self, width=450, height=450,)
        self.cells = [[square(self.fr, text=' ', width=10, height=5,
                              bg='white', x=j, y=i)
                       for i in range(3)] for j in range(3)]

    def start_new_game(self, *args):
        self.title("Tik Tak Toe: Player O")
        # th_server=Thread(target=self.tcp_server)
        # th_server.start()
        self.player = "O"
        self.color = 'blue'
        self.fr.destroy()
        self.fr = tk.Frame(self, width=450, height=450, bg='light green')
        self.cells = [[square(self.fr, text=' ', width=10, height=5,
                              bg='white', x=j, y=i)
                       for i in range(3)] for j in range(3)]
        for i in range(3):
            for j in range(3):
                self.cells[i][j].grid(row=i, column=j, padx=5, pady=5)
        self.fr.pack()
        self.fr.update()
        f = open("setting.txt", "r")
        data = f.read().split()[0]
        self.tcp = tcp_com(operation="server",host=data)
        self.tcp.create()
        self.Status = True
        self.Turn = True
        self.fr.update()

    def check_game(self, *args):
        print("check game called")
        for i in range(3):
            print(self.cells[i][0]['text'], self.cells[i][1]['text'],
                  self.cells[i][2]['text'])
            print(self.cells[0][i]['text'], self.cells[1][i]['text'],
                  self.cells[2][i]['text'])

            print(self.cells[i][0]['text'] == self.cells[i][1]['text'] ==
                  self.cells[i][2]['text'] and self.cells[i][0]['text'] != ' ')
            print(self.cells[0][i]['text'] == self.cells[1][i]['text'] ==
                  self.cells[2][i]['text'] and self.cells[0][i]['text'] != ' ')

            if (self.cells[i][0]['text'] == self.cells[i][1]['text'] ==
                    self.cells[i][2]['text'] and
                    self.cells[i][0]['text'] != ' '):
                print('horizental match')
                self.Status = False
                return True

            elif (self.cells[0][i]['text'] == self.cells[1][i]['text'] ==
                    self.cells[2][i]['text'] and
                    self.cells[0][i]['text'] != ' '):
                print('virtical match')
                self.Status = False
                return True
        print(self.cells[0][0]['text'] == self.cells[1][1]['text'] ==
              self.cells[2][2]['text'] and
              self.cells[0][0]['text'] != ' ')
        print(self.cells[0][2]['text'] == self.cells[1][1]['text'] ==
              self.cells[2][0]['text'] and
              self.cells[0][2]['text'] != ' ')
        if (self.cells[0][0]['text'] == self.cells[1][1]['text'] ==
            self.cells[2][2]['text'] and
                self.cells[0][0]['text'] != ' '):
            self.Status = False
            print('diagonal match')
            return True

        elif (self.cells[0][2]['text'] == self.cells[1][1]['text'] ==
                self.cells[2][0]['text'] and self.cells[0][2]['text'] != ' '):
            self.Status = False
            print('diagonal2 match')
            return True
        return False

    def profile(self, *args):
        try:
            f = open("setting.txt", "r")
            data = f.read()
            print(data)
            if not(data):
                data = ' '
            f.close()
        except Exception as e:
            data = ' '
        self.fr.destroy()
        self.fr=tk.Frame(self,width=450,height=450,bg='light green')
        self.lbl1 = tk.Label(master=self.fr, text='Name', width=30,
                             height=1, bg='magenta')
        self.lbl1.pack(padx=5, pady=5)
        self.ent1 = tk.Entry(master=self.fr, width=30, bg='white')
        self.ent1.insert(0, data)
        self.ent1.pack(padx=5, pady=5)
        self.btn1 = tk.Button(master=self.fr, text='Save',
                              width=30, height=1, bg='magenta')
        self.btn1.pack(padx=5, pady=5)
        self.btn1.bind('<Button-1>', self.Save_profile)
        self.btn2 = tk.Button(master=self.fr, text='Return',
                              width=30, height=1, bg='magenta')
        self.btn2.pack(padx=5, pady=5)
        self.btn2.bind('<Button-1>', self.Menu)
        self.lbl1.pack()
        self.ent1.pack()
        self.btn1.pack()
        self.btn2.pack()
        self.fr.pack()

    def Save_profile(self, *args):
        f = open("setting.txt", "w")
        f.write(self.ent1.get())
        f.close()
        tkinter.messagebox.showinfo(message='profile name has been saved')

    def Menu(self, *args):
        self.fr.destroy()
        self.fr = tk.Frame(self, width=450, height=450, bg='light green')
        lbl1 = tk.Button(master=self.fr, text='Start New GAmE',
                         width=30, height=3, bg='magenta')
        lbl2 = tk.Button(master=self.fr, text='Join Another gAmE',
                         width=30, height=3, bg='magenta')
        lbl3 = tk.Button(master=self.fr, text='Watch GaME',
                         width=30, height=3, bg='magenta')
        lbl4 = tk.Button(master=self.fr, text='Profile',
                         width=30, height=3, bg='magenta')
        lbl5 = tk.Button(master=self.fr, text='Quit GaMe',
                         width=30, height=3, bg='magenta')
        lbl1.pack(padx=5, pady=5)
        lbl1.bind('<Button-1>', self.start_new_game)
        lbl2.pack(padx=5, pady=5)
        lbl2.bind('<Button-1>', self.join_game)
        lbl3.pack(padx=5, pady=5)
        lbl4.pack(padx=5, pady=5)
        lbl4.bind('<Button-1>', self.profile)
        lbl5.pack(padx=5, pady=5)
        lbl5.bind('<Button-1>', lambda x: self.destroy())
        self.fr.pack()
        # self.fr.tkraise()

    def join_game(self, *args):
        self.title("Tik Tak Toe: Player X")
        self.fr.destroy()
        self.fr = tk.Frame(self, width=450, height=450, bg='light green')
        self.cells = [[square(self.fr, text=' ', width=10, height=5,
                              bg='white', x=j, y=i)
                       for i in range(3)] for j in range(3)]

        for i in range(3):
            for j in range(3):
                self.cells[i][j].grid(row=i, column=j, padx=5, pady=5)
        print(self.cells)
        self.fr.pack()
        self.fr.update()
        self.Status = True
        self.player = "X"
        self.color = 'orange'
        f = open("setting.txt", "r")
        data = f.read().split()[0]
        print(data)
        self.tcp = tcp_com(operation="client",host=data)
        self.tcp.join()
        print('connected to server')
        new_mouve = self.tcp.opponent.recv(1024).decode('utf-8').split(',')
        print(new_mouve)
        x = int(new_mouve[0])
        y = int(new_mouve[1])
        self.cells[x][y]['text'] = "O"
        self.cells[x][y]['bg'] = 'blue'
        self.cells[x][y].update()
        self.Turn = True


class square(tk.Label):
    def __init__(self, master, text=' ', width=30, height=15,
                 bg='red', fg='black', x=0, y=0,
                 font="Helvetica 14 bold italic"):
        super().__init__(master=master, text=text, width=width,
                         height=height, bg=bg)
        self['text'] = text
        # self.width=width
        # self.height=height
        # self.bg=bg
        self.x = x
        self.y = y
        # self.active=False
        self.bind('<Button-1>', self.mouve)

    def mouve(self, *args):
        print('click happened', self.master.master.Turn)
        if (self.master.master.Turn):
            if self['text'] == ' ' and self.master.master.Status:
                self['text'] = self.master.master.player
                self['bg'] = self.master.master.color
                self['font'] = "Helvetica 10"
                self.master.master.Turn = False
                self.update()
                msg = str(self.x) + "," + str(self.y)
                self.master.master.tcp.opponent.sendall(msg.encode('utf-8'))
                if self.master.master.check_game():
                    """
                    self.master.master.end=time.strftime('%c')
                    f=open('score.txt','a')
                    f.write(self.master.master.start+'\t'+
                            self.master.master.end+'\n')
                    self.master.master.start_new_game()
                    """
                    print('You won the game '.
                          format(self.master.master.player))
                    tkinter.messagebox.showinfo(message='you Won the game')

                    # time.sleep(5)
                    self.master.master.Status = False
                    self.master.master.Menu()
                    # if self.master.master.tcp.operation == "server":
                    #     self.master.master.tcp.close_game()
                    #    print('server closed')
                    self.master.master.tcp.close_game()
                    print('server closed')
                    return
                else:
                    new_mouve = self.master.master.tcp.opponent.recv(1024)
                    new_mouve = new_mouve.decode('utf-8').split(',')
                    x = int(new_mouve[0])
                    y = int(new_mouve[1])

                    if(self.master.master.player == "O"):
                        self.master.master.cells[x][y]['text'] = "X"
                        self.master.master.cells[x][y]['bg'] = 'orange'
                    elif(self.master.master.player == "X"):
                        self.master.master.cells[x][y]['text'] = "O"
                        self.master.master.cells[x][y]['bg'] = 'blue'
                    self.update()
                    if self.master.master.check_game():
                        print('You Lost the game')
                        tkinter.messagebox.showinfo(message='you Lost the game')
                        # time.sleep(5)
                        self.master.master.Status = False
                        self.master.master.Menu()
                        self.master.master.tcp.close_game()
                        print('server closed')
                self.master.master.Turn = True


class tcp_com:
    def __init__(self, host='127.0.0.1', port=65432, server='',
                 clients=[], status=False, operation='client'):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.host = host  # Standard loopback interface address (localhost)
        self.port = port  # Port to listen on (non-privileged ports are > 1023)
        self.server = server
        self.clients = clients
        self.status = status
        self.operation = operation

    def create(self, *args):
        self.sock.bind((self.host, self.port))
        self.sock.listen(1)
        self.opponent, self.addr = self.sock.accept()
        self.clients.append((self.opponent, self.addr))
        self.status = True
        self.operation = "server"

    def join(self, *args):
        self.opponent = self.sock
        self.sock.connect((self.host, self.port))
        self.status = True
        self.operation = "client"

    def close_game(self, *args):
        if self.operation == "client":
            self.opponent.close()
        elif self.operation == "server":
            for client in self.clients:
                client[0].close()
            self.sock.close()


main = Game()
main.Menu()
main.mainloop()
