import socket
from tkinter import *
from tkinter import ttk
import time
import sys

PROG_NAME = "TesMart KVM Utility"
VERSION = "1.0"

ip = "10.1.30.37"
port = 5000


def sendkvm(ip, port, src):
    so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    so.connect((ip, port))
    print(src)
    so.send(bytes.fromhex('AA BB 03 01 0' + str(src) + ' EE'))
    data = so.recv(1024)
    so.close()
    return


root = Tk()
root.title("{} - Version {}".format(PROG_NAME, VERSION))

topFrame = Frame(root)
topFrame.pack()
bottomFrame = Frame(root)
bottomFrame.pack()
statusFrame = Frame(root)
statusFrame.pack(side=BOTTOM)

btn1 = ttk.Button(topFrame, text="1", command=lambda: sendkvm(ip, port, 1))
btn1.grid(row=0, column=1)
btn2 = ttk.Button(topFrame, text="2", command=lambda: sendkvm(ip, port, 2))
btn2.grid(row=0, column=2)
btn3 = ttk.Button(topFrame, text="3", command=lambda: sendkvm(ip, port, 3))
btn3.grid(row=0, column=3)
btn4 = ttk.Button(topFrame, text="4", command=lambda: sendkvm(ip, port, 4))
btn4.grid(row=0, column=4)
btn5 = ttk.Button(topFrame, text="5", command=lambda: sendkvm(ip, port, 5))
btn5.grid(row=0, column=5)
btn6 = ttk.Button(topFrame, text="6", command=lambda: sendkvm(ip, port, 6))
btn6.grid(row=0, column=6)
btn7 = ttk.Button(topFrame, text="7", command=lambda: sendkvm(ip, port, 7))
btn7.grid(row=0, column=7)
btn8 = ttk.Button(topFrame, text="8", command=lambda: sendkvm(ip, port, 8))
btn8.grid(row=0, column=8)

btnExit = ttk.Button(bottomFrame,  text="Exit/Quit", command=lambda: sys.exit(0))
btnExit.grid(row=4, column=0, columnspan=8)

statusbar = ttk.Label(root, text="(c) 2023, Darryl Quinn", border=1, relief=SUNKEN, anchor=W)
statusbar.pack(side=BOTTOM, fill=X)

root.mainloop()