from tkinter import *
from tkinter import ttk
import sqlite3

c = sqlite3.connect('time_track.db')
cursor = c.cursor()

'''
# Database init and table creation
cursor.execute("""CREATE TABLE time_track(
    subject text,
    date text,
    time_spent integer,
    week integer
    )
    """)
'''

def frame_track(root):
    #Track frame
    frame_track = LabelFrame(root, text= "Track current session", padx= 400, pady = 100)
    frame_track.grid(padx= 10, pady= 10, row= 1, column= 0, columnspan= 2, sticky= 'nsew')
    #Placeholder buttons
    my_button = Button(frame_track, text= "PlaceHolder")
    my_button.grid(row= 0, column= 0)

   