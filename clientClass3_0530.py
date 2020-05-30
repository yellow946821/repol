import socket
import errno
import sys
import tkinter as tk
import PIL
from PIL import Image, ImageTk
import time
import threading
from threading import *

global linewidth , first , rectxy, myrect , start , mytime
mytime = [0]
linewidth = 3
start = [0]
myrect = [0]
first = [True]
rectxy = [20,20]

IP = "127.0.0.1"
PORT = 8000
client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect((IP, PORT))


class YouDrawIGuess(threading.Thread):
    
    def __init__(self):
        threading.Thread.__init__(self)
        
        self.attrib1 = "Attrib from Interface class"
        self.root = tk.Tk()
        self.root.title('You Draw I Guess')
        self.root.geometry('1000x550')
        self.root.configure(background='#F8F8FF')
        
        self.namestr = tk.StringVar() 
        self.etyName = tk.Entry(self.root,textvariable=self.namestr,bd=3)
        self.etyName.grid(row=0 , column = 6,sticky=tk.W)
        self.btnSet = tk.Button(self.root, text='set',width=10, command=self.Set_name)
        self.btnSet.grid(row=0 , column = 6,padx=150,sticky=tk.W)
        
        self.scorebox = tk.Text(self.root, width=30 ,height=10, bd=5)
        self.scorebox.grid(row=2, column = 6,sticky=tk.N+tk.W)
        self.scorebox.insert('end',"this is a score box")

        self.txbox = tk.Text(self.root,width=30 ,height=20, bd=5)
        self.txbox.grid(row=2, column = 6,sticky=tk.S+tk.W)
        

        self.msgstr = tk.StringVar()
        self.etyMsg = tk.Entry(self.root,textvariable=self.msgstr,bd=3)
        self.etyMsg.grid(row=6 , column = 6,sticky=tk.W)
        self.btnEnter = tk.Button(self.root, text='enter',width=10, command=self.sendMessage)
        self.btnEnter.grid(row=6 , column = 6, padx=150, sticky=tk.W)
        
        self.canvas_width = 600
        self.canvas_height = 400
        self.var = tk.StringVar() 
        self.var.set("red")
        self.s = tk.Scale(self.root, label='Linewidth', from_ = 2, to = 20, 
             orient=tk.HORIZONTAL, length=300, showvalue=1,
             tickinterval=2, resolution=1, command=self.print_scale)
        self.s.grid(row=0 , column = 0)
        self.r1 = tk.Radiobutton(self.root, text='RED', variable=self.var, value='red',width=10, indicatoron=0, command=self.print_selection)
        self.r1.grid(row=0 , column = 1)
        self.r2 = tk.Radiobutton(self.root, text='BLUE', variable=self.var, value='blue',width=10, indicatoron=0, command=self.print_selection)
        self.r2.grid(row=0 , column = 2)
        self.r3 = tk.Radiobutton(self.root, text='GREEN', variable=self.var, value='green',width=10, indicatoron=0, command=self.print_selection)
        self.r3.grid(row=0 , column = 3)
        self.r4 = tk.Radiobutton(self.root, text='ERASER', variable=self.var, value='eraser',width=10, indicatoron=0, command=self.print_selection)
        self.r4.grid(row=0 , column = 4)
                
        self.cvs = tk.Canvas(self.root, width=self.canvas_width, height=self.canvas_height, bg="white",bd=3)
        self.cvs.grid(row = 2, column=0, columnspan=7,sticky=tk.W)
        self.cvs.bind('<Motion>', self.motion) #bind(event,handler)
        self.cvs.bind("<B1-Motion>", self.drag)
        self.r1.bind('<Motion>', self.in_contrl_space)
        self.r2.bind('<Motion>', self.in_contrl_space)
        self.r3.bind('<Motion>', self.in_contrl_space)
        self.r4.bind('<Motion>', self.in_contrl_space)
        self.s.bind('<Motion>', self.in_contrl_space)
        
        global timetext
        timetext = [tk.StringVar()]
        timetext[0].set("Test")
        self.Time = tk.Label(self.root, textvariable=timetext , width = 10)
        self.Time.grid(row = 0 , column = 5)

        self.cvstime = tk.Canvas(self.root, width=self.canvas_width, height=5, bg="pink")
        self.cvstime.grid(row = 1, columnspan=7, sticky=tk.W)
        mytime[0] = self.cvstime.create_line(0,2,self.canvas_width,2,fill = "red",width = 10)
        
        
    def Set_name(self):
        global my_username
        my_username = self.etyName.get()
       
        
    def print_selection(self): 
        self.var.set(self.var.get())
        print('you have selected ' , self.var.get())
    
    def print_scale(v): 
        print('you have selected ' , v)
        linewidth = v
        print(linewidth)
        
    def in_contrl_space(self,event): 
        self.cvs.delete(myrect[0])
        first[0] = True
        
    def motion(self,event): 

        if (first[0]):
    
            if(self.var.get() == "eraser"):
                width = 1
                if self.s.get() > 10:
                    width = 5
                myrect[0] = self.cvs.create_rectangle(event.x-self.s.get()-2 , event.y-self.s.get()-2,
                                  event.x+self.s.get()+2 , event.y+self.s.get()+2,
                                  fill = "white" , outline = "black" , width = width)
            else:
                myrect[0] = self.cvs.create_oval(event.x-self.s.get(), event.y-self.s.get(), 
                               event.x+self.s.get(), event.y+self.s.get(), 
                               fill = self.var.get() , outline = self.var.get())
            rectxy[0] = event.x
            rectxy[1] = event.y
            first[0] = False
            
            
        self.cvs.move(myrect[0], event.x-rectxy[0], event.y-rectxy[1])
        rectxy[0] = event.x
        rectxy[1] = event.y
    
    def drag(self,event): 
        self.cvs.delete(myrect[0])
        first[0] = True
        
        if(self.var.get() == "eraser"):
            self.cvs.create_rectangle(event.x-self.s.get(), event.y-self.s.get(), 
                               event.x+self.s.get(), event.y+self.s.get(), 
                               fill = "white" , outline = "white")
        else:
            self.cvs.create_oval(event.x-self.s.get(), event.y-self.s.get(), 
                               event.x+self.s.get(), event.y+self.s.get(), 
                               fill = self.var.get() , outline = self.var.get())
            
    def sendMessage(self):
        clientMessage = self.etyMsg.get()
        self.txbox.insert('end', "You: "+ clientMessage)
        self.txbox.insert('end', "\n")
        client_socket.send(clientMessage.encode('utf-8'))
        self.etyMsg.delete(0, 'end') 

    def Start(self):
        self.root.mainloop()



class RecvMsg(threading.Thread):
    def __init__(self):
        time.sleep(1)
        threading.Thread.__init__(self)
        threading.daemon = True    
        
    def run(self):
        global finish3
        while not finish3:
            print("in recv")
            serverMessage = client_socket.recv(1024).decode('utf-8')
            time.sleep(1)
            print(serverMessage)
            Main.txbox.insert('end', serverMessage) 
            Main.txbox.insert('end', "\n") 


        
class Process(threading.Thread):
    def __init__(self):
        time.sleep(1)
        threading.Thread.__init__(self)
        self.attrib2 = "Attrib from Process class"
        start[0] = time.time()

    def run(self):
        totaltime = 30
        movex = 0
        times = 0
        global finish2
        while not finish2:
            Main.cvstime.move(mytime[0] , movex , 0)
            movex = -20
            timetext[0].set(str(totaltime))
            totaltime -= 1 
            if times == 30:
                start[0] += totaltime+1
                movex = 600
                totaltime = 30
                times = -1
            times += 1
            time.sleep(1)
            
                      
            
finish2 = False
finish3 = False
SecondThread = Process() 
ThirdThread = RecvMsg()
Main = YouDrawIGuess()

Main.root.after(50, SecondThread.start)
Main.root.after(70, ThirdThread.start)
Main.Start()
finish2 = True
finish2 = True

