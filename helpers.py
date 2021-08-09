from tkinter import *
from tkinter import ttk

def themes(root):
    #set theme
    ttk.Style().theme_use('winnative')
    root.title('Study Tracker')
    root.geometry("800x900")
    #Grid config rows/columns
    Grid.rowconfigure(root, 0, weight= 1)
    Grid.rowconfigure(root, 1, weight= 1)
    Grid.rowconfigure(root, 2, weight= 1)

    Grid.columnconfigure(root, 0, weight= 1)
    Grid.columnconfigure(root, 1, weight= 1)

def open_window(root):
    #creates new window
    top = Toplevel(root)
    ow_button = Button(top, text= "Close Window", command= top.destroy).pack()
    
    # https://stackoverflow.com/questions/29233029/python-tkinter-show-only-one-copy-of-window
    # interaction limited to open window
    top.transient(root)
    top.grab_set()
    root.wait_window(top)

def place_button(root, text):
    button = Button(root, text=f"{text}", command= lambda: open_window(root))
    button.grid(padx= 10, pady= 10, row= 1, column= 1)

def frame_semmester(root):
    #All time frame
    frame_allTime = LabelFrame(root,text= "Semester to date", padx= 100, pady = 100)
    frame_allTime.grid(padx= 10, pady= 10, row= 0, column= 0)
    #Placeholder buttons
    my_button = Button(frame_allTime, text= "PlaceHolder")
    my_button.grid(row= 0, column= 0)

def frame_weekly(root):
    # Week to date frame
    frame_weekly = LabelFrame(root, text= "Week to date", padx= 100, pady = 100)
    frame_weekly.grid(padx= 10, pady= 10, row= 0, column= 1)
    #Placeholder buttons
    my_button = Button(frame_weekly, text= "PlaceHolder")
    my_button.grid(row= 0, column= 0)

def frame_update(root):
    #Update frame
    frame_update = LabelFrame(root, text= "Update", padx= 200, pady = 100)
    frame_update.grid(padx= 10, pady= 10, row= 2, column= 0, columnspan= 2, sticky= 'nsew')
    my_button = Button(frame_update, text= "PlaceHolder")
    my_button.grid(row= 0, column= 0)

def frame_track(root):
    #Track frame
    frame_track = LabelFrame(root, text= "Track current session", padx= 400, pady = 100)
    frame_track.grid(padx= 10, pady= 10, row= 1, column= 0, columnspan= 2, sticky= 'nsew')
    #Placeholder buttons
    my_button = Button(frame_track, text= "PlaceHolder")
    my_button.grid(row= 0, column= 0)



