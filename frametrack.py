from tkinter import *
from tkinter import ttk

def frame_track(root):
    #Track frame
    frame_track = LabelFrame(root, text= "Track current session", padx= 400, pady = 100)
    frame_track.grid(padx= 10, pady= 10, row= 1, column= 0, columnspan= 2, sticky= 'nsew')
    #Placeholder buttons
    my_button = Button(frame_track, text= "PlaceHolder")
    my_button.grid(row= 0, column= 0)