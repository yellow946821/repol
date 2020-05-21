# -*- coding: utf-8 -*-
"""
Created on Wed May 13 11:36:19 2020

@author: Lai Hao Wei
"""

#from tkinter import *
#from PIL import Image, ImageTk
#import time
#import threading
#import cv2
#global linewidth , first , rectxy, myrect , start
#linewidth = 3
#start = [0]
#myrect = [0]
#first = [True]
#rectxy = [20,20]
#root = Tk()
#root.resizable(True, True)
#root.title('You Draw I Guess')
#root.geometry('705x591')
#
#canvas_width = 705
#canvas_height = 591
#var = StringVar()
#var.set("red")
#
#def drag(event):
##    cvs.place(x=event.x_root, y=event.y_root,anchor=CENTER)
#    cvs.delete(myrect[0])
#    first[0] = True
#    
#    if(var.get() == "eraser"):
#        cvs.create_rectangle(event.x-s.get(), event.y-s.get(), 
#                           event.x+s.get(), event.y+s.get(), 
#                           fill = "white" , outline = "white")
#    else:
#        cvs.create_oval(event.x-s.get(), event.y-s.get(), 
#                           event.x+s.get(), event.y+s.get(), 
#                           fill = var.get() , outline = var.get())
#    
##    cvs.create_line(event.x-1, event.y-1, 
##                    event.x, event.y, 
##                    fill="red" , width = s.get())
#    
##    print("x = " , event.x , " y = " , event.y)
#    
#def motion(event):
#
#    if (first[0]):
#
#        if(var.get() == "eraser"):
#            width = 1
#            if s.get() > 10:
#                width = 5
#            myrect[0] = cvs.create_rectangle(event.x-s.get()-2 , event.y-s.get()-2,
#                              event.x+s.get()+2 , event.y+s.get()+2,
#                              fill = "white" , outline = "black" , width = width)
#        else:
#            myrect[0] = cvs.create_oval(event.x-s.get(), event.y-s.get(), 
#                           event.x+s.get(), event.y+s.get(), 
#                           fill = var.get() , outline = var.get())
#        rectxy[0] = event.x
#        rectxy[1] = event.y
#        first[0] = False
#        
##    print(rectxy[0] , " " , rectxy[1])
#    cvs.move(myrect[0], event.x-rectxy[0], event.y-rectxy[1])
#    rectxy[0] = event.x
#    rectxy[1] = event.y
#    
#    
#    
#    
#def print_scale(v):
#    print('you have selected ' , v)
#    linewidth = v
#    print(linewidth)
#
#    
#def print_selection():
#    print('you have selected ' , var.get())
#    
#def in_contrl_space(event):
##    print("in radio!!")
#    cvs.delete(myrect[0])
#    first[0] = True
#    
#def job():
#  while True:
#      timetext.set(str(int(time.time() - start[0])))
#      time.sleep(1)
#      
#      if int(time.time() - start[0])%11 == 0:
#          start[0] += 10
#      
#    
##s = Scale(root, label='Linewidth', from_=2, to=10, 
##             orient=HORIZONTAL, length=200, showvalue=1,
##             tickinterval=2, resolution=1, command=print_selection)
##s.pack()
##s.place(x=10,y=100)
#s = Scale(root, label='Linewidth', from_=2, to=20, 
#             orient=HORIZONTAL, length=300, showvalue=1,
#             tickinterval=2, resolution=1, command=print_scale)
#s.grid(row=0)
#r1 = Radiobutton(root, text='RED', variable=var, value='red', command=print_selection)
#r1.grid(row=0 , column = 1)
#r2 = Radiobutton(root, text='BLUE', variable=var, value='blue', command=print_selection)
#r2.grid(row=0 , column = 2)
#r3 = Radiobutton(root, text='GREEN', variable=var, value='green', command=print_selection)
#r3.grid(row=0 , column = 3)
#r4 = Radiobutton(root, text='ERASER', variable=var, value='eraser', command=print_selection)
#r4.grid(row=0 , column = 4)
#
#timetext = StringVar()
#timetext.set("Test")
#Time = Label(root, textvariable=timetext).grid(row = 0 , column = 5)
#timetext.set("I'm changed")
#t = threading.Thread(target = job)
#t.setDaemon(True)
#start[0] = time.time()-1
#t.start()
#
#
#
#r1.bind('<Motion>', in_contrl_space)
#r2.bind('<Motion>', in_contrl_space)
#r3.bind('<Motion>', in_contrl_space)
#r4.bind('<Motion>', in_contrl_space)
#s.bind('<Motion>', in_contrl_space)
#
#
#cvs = Canvas(root,
#             width=canvas_width,
#             height=canvas_height,
#             bg="white")
#cvs.grid(row = 2,columnspan=6)
##cvs.pack(expand = YES, fill = BOTH , side='bottom')
#cvs.bind("<B1-Motion>", drag)
#cvs.bind('<Motion>', motion)
#
#
#
#mainloop()
#t._stop()
from tkinter import *
from PIL import Image, ImageTk
import time
import threading
global linewidth , first , rectxy, myrect , start , mytime
mytime = [0]
linewidth = 3
start = [0]
myrect = [0]
first = [True]
rectxy = [20,20]
class YouDrawIGuess(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.attrib1 = "Attrib from Interface class"

        self.root = Tk()
        self.root.resizable(True, True)
        self.root.title('You Draw I Guess')
        self.root.geometry('850x600')
        
      
        self.canvas_width = 850
        self.canvas_height = 600
        self.var = StringVar()
        self.var.set("red")
        self.s = Scale(self.root, label='Linewidth', from_ = 2, to = 20, 
             orient=HORIZONTAL, length=300, showvalue=1,
             tickinterval=2, resolution=1, command=self.print_scale)
        self.s.grid(row=0 , column = 0)
        self.r1 = Radiobutton(self.root, text='RED', variable=self.var, value='red',width=10, indicatoron=0, command=self.print_selection)
        self.r1.grid(row=0 , column = 1)
        self.r2 = Radiobutton(self.root, text='BLUE', variable=self.var, value='blue',width=10, indicatoron=0, command=self.print_selection)
        self.r2.grid(row=0 , column = 2)
        self.r3 = Radiobutton(self.root, text='GREEN', variable=self.var, value='green',width=10, indicatoron=0, command=self.print_selection)
        self.r3.grid(row=0 , column = 3)
        self.r4 = Radiobutton(self.root, text='ERASER', variable=self.var, value='eraser',width=10, indicatoron=0, command=self.print_selection)
        self.r4.grid(row=0 , column = 4)
        
        global timetext
        timetext = [StringVar()]
        timetext[0].set("Test")
        self.Time = Label(self.root, textvariable=timetext , width = 10).grid(row = 0 , column = 5)
#        print(timetext[0])
#        self.timetext = StringVar()
#        self.timetext.set("Test")
#        self.Time = Label(self.root, textvariable=self.timetext , width = 10).grid(row = 0 , column = 5)
        
        
        self.cvs = Canvas(self.root,
             width=self.canvas_width,
             height=self.canvas_height,
             bg="white")
        self.cvs.grid(row = 2,columnspan=6)
        self.cvs.bind('<Motion>', self.motion)
        self.cvs.bind("<B1-Motion>", self.drag)
        self.r1.bind('<Motion>', self.in_contrl_space)
        self.r2.bind('<Motion>', self.in_contrl_space)
        self.r3.bind('<Motion>', self.in_contrl_space)
        self.r4.bind('<Motion>', self.in_contrl_space)
        self.s.bind('<Motion>', self.in_contrl_space)
        
        self.cvstime = Canvas(self.root,
             width=self.canvas_width,
             height=5,
             bg="pink")
        self.cvstime.grid(row = 1,columnspan=6)
        mytime[0] = self.cvstime.create_line(0,2,850,2,fill = "red",width = 10)
    
    def print_selection(self):
        self.var.set(self.var.get())
        print('you have selected ' , self.var.get())
        
    
    def print_scale(v):
        print('you have selected ' , v)
        linewidth = v
        print(linewidth)
    def in_contrl_space(self,event):
#    print("in radio!!")
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
#    def job(self):
#      while True:
#          self.timetext.set(str(int(time.time() - start[0])))
#          time.sleep(1)
#          
#          if int(time.time() - start[0])%11 == 0:
#              start[0] += 10
        
    def start(self): #Start
#        t = threading.Thread(target = self.job)
#        t.setDaemon(True)
#        start[0] = time.time()-1
#        t.start()
#        t.join(self.root.mainloop)
        
        self.root.mainloop()
#        self.root.destroy()
    
class Process(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.attrib2 = "Attrib from Process class"
        start[0] = time.time()

    def run(self):
        totaltime = 30
        movex = 0
#        ThirdThread.start()
        global finish
        while not finish:
#            print("Proceso infinito")
            #Inside the infinite process a method from Interface class is used.
#            GUI.method1()
#            Main.cvstime.delete(mytime[0])
#            mytime[0] = Main.cvstime.create_line(0,2,850-minus,2,fill = "red",width = 10)
#            minus += 10
            Main.cvstime.move(mytime[0] , movex , 0)
            movex = -28.3
            timetext[0].set(str(totaltime-int(time.time() - start[0])))
            if int(time.time() - start[0]) == totaltime:
                start[0] += totaltime+1
                movex = 850
            time.sleep(1)
            
            
            
finish = False
finish2 = False
#ThirdThread = Process2()
SecondThread = Process()
Main = YouDrawIGuess()
Main.root.after(50, SecondThread.start) 
Main.start()
finish = True
#print(Main.canvas_height)
#print(timetext[0])