# import tkinter module
from tkinter import *

# import Vigenère Cipher
import base64

# import other necessery modules
import random

# creating root object
root = Tk()

# defining size of window
root.geometry("1200x400")

# setting up background color
root.configure(background="powder blue")

# setting up the title of window
root.title("Message Encryption and Decryption")

Tops = Frame(root, width=1600, relief=SUNKEN, background="powder blue")
Tops.pack(side=TOP)

f1 = Frame(root, width=800, height=700,
    relief=SUNKEN, background="powder blue")
f1.pack(side=LEFT)

lblInfo = Label(Tops, font=('helvetica', 50, 'bold'),
    text="ENCRYPT AND DECRYPT YOUR MESSAGE",
    fg="Black", bd=10, anchor='w', background="powder blue")
lblInfo.grid(row=0, column=0)

rand = StringVar()
Msg = StringVar()
key = StringVar()
mode = StringVar()
Result = StringVar()

# Function to reset the window
def Reset():
    rand.set("")
    Msg.set("")
    key.set("")
    mode.set("")
    Result.set("")

# labels
lblMsg = Label(f1, font=('arial', 16, 'bold'),
    text="Message:", bd=16, anchor="w", background="powder blue")

lblMsg.grid(row=0, column=4)

txtMsg = Entry(f1, font=('arial', 16, 'bold'),
    textvariable=Msg, bd=1, insertwidth=4,
    bg="light green", justify='left')

txtMsg.grid(row=0, column=5)

lblkey = Label(f1, font=('arial', 16, 'bold'),
    text="Key(same length as the message):", bd=16, anchor="w", background="powder blue")

lblkey.grid(row=1, column=4)

txtkey = Entry(f1, font=('arial', 16, 'bold'),
    textvariable=key, bd=1, insertwidth=4,
    bg="light green", justify='left')

txtkey.grid(row=1, column=5)

lblmode = Label(f1, font=('arial', 16, 'bold'),
    text="Mode(e or d):",
    bd=16, anchor="w", background="powder blue")

lblmode.grid(row=2, column=4)

txtmode = Entry(f1, font=('arial', 16, 'bold'),
    textvariable=mode, bd=1, insertwidth=4,
    bg="light green", justify='left')

txtmode.grid(row=2, column=5)

lblService = Label(f1, font=('arial', 16, 'bold'),
    text="Final Message:", bd=1, anchor="w", background="powder blue")

lblService.grid(row=3, column=4)

txtService = Entry(f1, font=('arial', 16, 'bold'),
    textvariable=Result, bd=1, insertwidth=4,
    bg="light green", justify='left')

txtService.grid(row=3, column=5)

# Function to encode
def encode(key, clear):
    enc = []
    for i in range(len(clear)):
        key_c = key[i % len(key)]
        enc_c = chr((ord(clear[i]) + ord(key_c)) % 256)
        enc.append(enc_c)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()

# Function to decode
def decode(key, enc):
    dec = []
    enc = base64.urlsafe_b64decode(enc).decode()
    for i in range(len(enc)):
        key_c = key[i % len(key)]
        dec_c = chr((256 + ord(enc[i]) - ord(key_c)) % 256)
        dec.append(dec_c)
    return "".join(dec)

if Msg =="":
    Msg = "You Did Not Input a Message!"

def Brain():
    print("Message= ", (Msg.get()))
    clear = Msg.get()
    k = key.get()
    m = mode.get()
    if (m == 'e'):
        Result.set(encode(k, clear))
    else:
        Result.set(decode(k, clear))

# Show message button
Total_button = Button(f1, padx=16, pady=8, bd=16, fg="black", 
    font=('arial', 16, 'bold'), width=10, text="Convert",
     bg="blue", command=Brain).grid(row=7, column=1)
     
# Reset button
Reset_button = Button(f1, padx=16, pady=8, bd=16,fg="black", 
    font=('arial', 16, 'bold'), width=10, text="Reset", 
    background="green",command=Reset).grid(row=7, column=2)

# keeps window alive
root.mainloop()