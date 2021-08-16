import socket
from tkinter import *
import threading

def send():
    msg = e1.get()
    l = Label(root,text = "You: "+msg).pack()
    s.send(bytes(msg,'utf-8'))
    e1.delete(0,END)
    if msg == '!bye':
        s.close()
def listen():
    while True:
        msg = s.recv(1024).decode()
        print(msg)
        msg_l = Label(root,text ="Friend: "+ msg).pack()

root = Tk()

root.geometry("400x600")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

ip = socket.gethostname()
port = 4444

s.connect((ip,port))

e1 = Entry(root)
e1.pack()

b1 = Button(root,text = "send",command = send).pack()


t = threading.Thread(target=listen)
t.start()

root.mainloop()


