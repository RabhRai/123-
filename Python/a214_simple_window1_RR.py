##############################################################################
#   a113_TR_simple_window1.py
#   Example soulution: Change its size to 200 by 100 pixels.
##############################################################################
import tkinter as tk

# main window
root = tk.Tk()
root.wm_geometry("200x100")
root.title("Authentication")
root.mainloop()
frame_login = tk.Frame(root)
frame_login.grid
lbl_username = tk.Label(frame_login, text='Username:')
lbl_username.pack()