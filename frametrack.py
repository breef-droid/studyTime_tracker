from tkinter import *
import sqlite3
import time
import app_timer

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
    
    #Drop down button creation
    subjects = ['PWD (CM2015)', 'CS (CM2025)', 'DNW (CM2040)'] # Subject list:-> TODO: update to global var from update frame module
    clicked = StringVar() #init a String object in tkinter
    clicked.set('Select Subject')
    drop_down = OptionMenu(root, clicked, *subjects)
    drop_down.grid(row= 1, column= 0, padx= 20, pady= 30, sticky= 'nw')

    img_list = image_list()

    #Timer Control buttons - play
    timer_play = Button(root, image = img_list[0], borderwidth= 0, command= lambda : start_timer(label_time))
    timer_play.grid(row= 1, column= 0, padx= 20, pady= 60, sticky= 'nw')
    
    #Timer Control buttons - reset
    timer_reset = Button(root, image = img_list[1], borderwidth= 0, command= lambda : reset_timer(label_time))
    timer_reset.grid(row= 1, column= 0, padx= 80, pady= 60, sticky= 'nw')
    
    #Timer Control buttons - stop
    timer_stop = Button(root, image = img_list[2], borderwidth= 0, command= stop_timer)
    timer_stop.grid(row= 1, column= 0, padx= 50, pady= 60, sticky= 'nw')

    #Time Label
    label_time = Label(root, text="Click Play to Start", font=("Helvetica", 12), fg= "green", bg= "black")
    label_time.grid(row= 1, column= 0, padx = 150, pady = 60, sticky= 'nw')


def image_list():
    global img_play, img_pause, img_stop
    img_play = PhotoImage(file="./assets/play.png")
    img_pause = PhotoImage(file="./assets/pause.png")
    img_stop = PhotoImage(file="./assets/stop.png")

    return [img_play, img_pause, img_stop]


#init timer global vars
counter = -1
running = False


def counter_label(lbl):
    def count():
        if running:
            global counter
            if counter == -1:
                display = "00"
            else:
                display = str(counter)

            lbl['text'] = display

            lbl.after(1000, count)
            counter += 1
        elif running == False:
            counter = counter
            

    count()

def start_timer(lbl):
    global running
    running = True
    counter_label(lbl)


def stop_timer():
    global running
    running = False

def reset_timer(lbl):
    global counter
    counter = -1
    if running == False:
        lbl['text'] = '00'