# p227_starter_one_button_shell.py
import os
import tkinter as tk
import tkinter.scrolledtext as tksc
from tkinter import filedialog
from tkinter.filedialog import asksaveasfilename

def do_command(command):
    global command_textbox, url_entry
    
    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"

    p = os.system("ping -c 4 localhost" "> command_textbox.txt")
    # Puts the output in the txt file
    file = open("command_textbox.txt")
    for line in file:
        command_textbox.insert(tk.END, line)

def do_command_two(command):
    global command_textbox, url_entry
    
    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        # url_val = "127.0.0.1"
        url_val = "::1"

    r = os.system("traceroute localhost > trace_route.txt")
    # Puts the output in the txt file
    file = open("trace_route.txt")
    for line in file:
        command_textbox.insert(tk.END, line)

def do_command_three(command):
    global command_textbox, url_entry
    
    # If url_entry is blank, use localhost IP address 
    url_val = url_entry.get()
    if (len(url_val) == 0):
        #url_val = "127.0.0.1"
        url_val = "::1"

    r = os.system("NSlookup localhost > nslookup.txt")
    # Puts the output in the txt file
    file = open("nslookup.txt")
    for line in file:
        command_textbox.insert(tk.END, line)

root = tk.Tk()
frame = tk.Frame(root)
frame.pack()
root.configure(background="lightblue")
url_val=()

# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame,text="Ping", command=lambda:do_command("ping"))
ping_btn.pack(side = "left")
# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame, text="Trace Route", command=lambda:do_command_two("tracert"))
ping_btn.pack(side = "left")
# Makes the command button pass it's name to a function using lambda
ping_btn = tk.Button(frame, text="NSlookup", command=lambda:do_command_three("nslookup"))
ping_btn.pack(side = "left")

# creates the frame with label for the text box
frame_URL = tk.Frame(root, pady=10,  bg="black") # change frame color
frame_URL.pack()

# decorative label
url_label = tk.Label(frame_URL, text="Enter a URL of interest: ", 
    compound="center",
    font=("comic sans", 14),
    bd=0, 
    relief=tk.FLAT, 
    cursor="heart",
    fg="mediumpurple3",
    bg="black")
url_label.pack(side=tk.LEFT)
url_entry= tk.Entry(frame_URL,  font=("comic sans", 14), textvariable=url_val) # change font
url_entry.pack(side=tk.LEFT)
frame = tk.Frame(root,  bg="black") # change frame color
frame.pack()

# Adds an output box to GUI.
command_textbox = tksc.ScrolledText(frame, height=10, width=100,background="lightgreen")
command_textbox.pack()

root.mainloop()