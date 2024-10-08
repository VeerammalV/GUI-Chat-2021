import socket

import threading

from tkinter import *

PORT = 50000

SERVER = "129.18.0.1"

ADDRESS = (SERVER, PORT)

FORMAT="utf-8"

client = socket.socket(socket.AF_INET,

socket.SOCK_STREAM)

client.connect(ADDRESS)

class chatbox:...

#constructor method

def __init__(self):

# chat window which is currently hidden

self.Window = Tk()

self.Window.withdraw()

# Login window for user to add names and connect with server

self.login = Toplevel()

# set the title for login window

self.login.title("Login")

self.login.resizable(width=False,height=False)

self.login.configure(width=400,height=300)

# create a Label

self.label = Label (self.login,
                 text="Please login to continue",
                 
                 font="Arial 14 bold,
                 
                 justify=CENTER")

self.label.place(relheight=0.15,

                       relx=0.2,
                       
                       rely=0.07)
                       
# create a Label   

self.labelName = Label(self.login,
                                    text = "Name: ",
                                    
                                    font = "Arial 12")
                                    
self.labelName.place(relheight = 0.2,

                                relx = 0.1,
                                
                                rely = 0.2)
                    
self.labelName.place(relheight=0.2,

                                relx=0.1,
                                
                                rely=0.2)

# create a entry box for

self.entryName = Entry(self.login,

                                    Font="Arial 14")

self.entryName.place(relwidth=0.4, 

                                 relheight=0.12,
                                 
                                 relx=0.35,
                                 
                                 rely=0.2)

# set the focus of the curser

self.entryName.focus()

# create a Continue Button along with action

self.go = Button(self.login,

                         text="CONTINUE",

                         font="Arial 14 bold",     
                         
                         command=Lambda: self.toChatWindow(self.entryName.get()))

self.go.place(relx=0.4,

                    rely=0.55)

self.Window.mainloop()

def toChatWindow(self, name):

self.login.destroy()

self.layout (name) 

# thread created to receive messages

rcv = threading. Thread(target=self.receive)

rcv.start()

# The main layout of the chat

def layout (self, name):

self.name = name

# to show chat window

self.Window.deiconify()

self.Window.title("CHATROOM")

self.Window.resizable (width=False,

                                   height=False)
                                   
self.Window.configure(width = 470,

                                   height=550,

                                   bg="#17202A")

self.labelHead = Label(self. Window,

                                   bg="#17202A",

                                   fg="#EAECEE",

                                   text=self.name,

                                   font="Helvetica 13 bold",

                                   pady=5)
                                   
self.labelHead.place(relwidth=1)

self.line = Label(self. Window,

                        width=450,

                        bg="#ABB2B9")

self.line.place(relwidth=1,

                     rely=0.07,

                     relheight=0.012)

self.textCons= Text(self. Window,

                              width=20,

                              height=2,

                              bg="#17202A", 
                              
                              fg="#EAECEE",

                              font="Helvetica 14",

                              padx=5,

                              pady=5)
                              
self.textCons.place(relheight=0.745,

                              relwidth=1,

                              rely=0.08)

self.labelBottom= Label(self.Window,

                                     bg="#ABB289",

                                     height=80)

self.labelBottom.place(relwidth=1,

                                   relv=0.825)  

self.entryMsg = Entry(self.labelBottom,

                                 bg="#2C3E50",

                                 fg="#EAECEE",

                                 font="Helvetica 13")

# place the given widget

# into the chat window

self.entryMsg.place(relwidth=0.74,

                              relheight=0.06,

                              rely=0.008,

                              relx=0.011)   
                              
self.entryMsg.focus()

# create a Send Button

self.buttonMsg = Button(self.labelBottom,

                                      text="Send",

                                      font="Helvetica 10 bold",

                                      width=20,

                                      bg="#ABB2B9",

                                      command=Lambda: self.sendButton(self.entryMsg.get()))

self.buttonMsg.place(relx=0.77,

                                rely=0.008,

                                relheight=0.06,

                                relwidth=0.22)

self.textcons.config(cursor="arrow")      

 # create a scroll bar

scrollbar = Scrollbar(self.textCons)

#place the scroll bar

# into the gui window

scrollbar.place(relheight=1,

                       relx=0.974)

scrollbar.config(command=self.textcons.yview)

self.textcons.config(state=DISABLED)   

#function to basically start the thread for sending messages
                
def sendButton(send, msg):
	self.textCons.config(state=DISABLED)
	self.msg = msg
    self.entryMsg.delete(0, END)
    send = threading.Thread(target.sendMessage)
    send.start()
    
# function to receive messages

def receive(self):

while True:

try:

message client.recv(1024).decode (FORMAT)

# if the messages from the server is NAME send the client's name

if message == 'NAME':

client.send(self.name.encode (FORMAT))

else:

# insert messages to text box

self.textCons.config(state=NORMAL)

self.textCons.insert (END,
                                message + "\n\n")

self.textCons.config(state=DISABLED)

self.textCons.see (END)

except:

# an error will be printed on the command line or console if there's an error 

 print("An error occured!")

client.close()

break

# function to send messages

def sendMessage(self):

self.textcons.config(state=DISABLED)

while True:

message = (f"[self.name}: {self.msg}")

client.send(message.encode (FORMAT))

break

# create a chatwindow class object

g = chatbox()  	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            	                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                             