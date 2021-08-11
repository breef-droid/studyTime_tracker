from tkinter import *
import sqlite3
import time
import app_timer
import db_functions



def frame_track(root):
    #Track frame
    frame_track = LabelFrame(root, text= "Track current session", padx= 400, pady = 100)
    frame_track.grid(padx= 10, pady= 10, row= 1, column= 0, columnspan= 2, sticky= 'nsew')
    
    #Subject input box
    label_subject = Label(root, text="Subject: ")
    label_subject.grid(row= 1, column= 0, padx = 20, pady = 35, sticky= 'nw')
    editor_subject = Entry(root, width= 30)
    editor_subject.grid(row= 1, column= 0, padx = 70, pady = 35, sticky= 'nw')

    img_list = image_list()

    #Timer Control buttons - play
    timer_play = Button(root, image = img_list[0], borderwidth= 0, command= lambda : start_timer(label_time))
    timer_play.grid(row= 1, column= 0, padx= 20, pady= 110, sticky= 'nw')
    
    #Timer Control buttons - reset
    timer_reset = Button(root, image = img_list[1], borderwidth= 0, command= lambda : reset_timer(label_time))
    timer_reset.grid(row= 1, column= 0, padx= 80, pady= 110, sticky= 'nw')
    
    #Timer Control buttons - stop
    timer_stop = Button(root, image = img_list[2], borderwidth= 0, command= stop_timer)
    timer_stop.grid(row= 1, column= 0, padx= 50, pady= 110, sticky= 'nw')

    #Time Label
    label_time = Label(root, text="Click Play to Start", font=("Helvetica", 12), fg= "green", bg= "black")
    label_time.grid(row= 1, column= 0, padx = 150, pady = 110, sticky= 'nw')

    #Date Label
    # current date var formatted
    current_date = time.strftime('%Y/%m/%d', time.localtime()) 
    # subject = stringVar created for dropdown menu
    label_date = Label(root, text= current_date, font=("Helvetica", 12), fg= "green", bg= "black")
    label_date.grid(row= 1, column= 0, padx = 0, pady = 35, sticky= 'ne')
    
    #Week Label
    label_week = Label(root, text="Week: ")
    label_week.grid(row= 1, column= 0, padx = 20, pady = 70, sticky= 'nw')
    editor_week = Entry(root, width= 10)
    editor_week.grid(row= 1, column= 0, padx = 70, pady = 70, sticky= 'nw')
    
    # Add to db
    update_db = Button(root, 
                        text="Log session", 
                        command= lambda : db_functions.add_one(editor_subject.get(), current_date, counter, editor_week.get()) #clicked.get() is called when the button is pressed to .get() the data -> you can't assign it to a variable as the variable will hold the initial state of the StringVar and not the updated state
                        )
    update_db.grid(row= 1, column= 0, padx = 20, pady = 150, sticky= 'nw')

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
