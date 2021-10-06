import tkinter as tk
from tkinter import ttk #CSS for tkinter
import time #time module
import sqlite3
import pandas as pd
from datetime import date
import matplotlib.pyplot as plt
import matplotlib.dates as mdates
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
        


class Study_App(tk.Tk):

    def __init__(self):
        tk.Tk.__init__(self) #initialising tkinter
        self.window = ttk.Frame(self) #container to hold tkinter frames
        self.window.pack(side= 'top', fill= 'both', expand= True) # packs container to frame

        FRAME_WIDTH = 400
        FRAME_HEIGHT = 300
        #icon & title
        tk.Tk.iconbitmap(self, default= "assets/favicon.ico")
        tk.Tk.wm_title(self, "StudyTrack")

        #row/column config
        # self.window.grid(row= 0, column= 0, sticky= 'nsew')
        # self.window.grid_rowconfigure(0, weight= 1)
        # self.window.grid_columnconfigure(0, weight= 1)
        self.window.pack()

        # Create MenuBar
        menubar = tk.Menu() #init and associate to container
        filemenu = tk.Menu(menubar, tearoff= False) #places filemenu in menubar
        filemenu.add_command(label= 'Exit', command= self.close_app)
        menubar.add_cascade(label= "File", menu= filemenu)
        tk.Tk.config(self, menu= menubar)

        #place canvas in window
        Grapher(self.window, FRAME_WIDTH, FRAME_HEIGHT, 0, 0, '#e63946', 'weekly')
        Grapher(self.window, FRAME_WIDTH, FRAME_HEIGHT, 1, 0, '#1d3557', 'daily')
        Logger(self.window, FRAME_WIDTH, FRAME_HEIGHT + 25, 0, 1, '#457b9d')
        FrameConstructor(self.window, FRAME_WIDTH, FRAME_HEIGHT + 25, 1, 1,'#a8dadc')

    def close_app(self):
        self.destroy() # destroy container
        self.quit() # stops mainloop

class FrameConstructor():
    def __init__(self, root, width, height, row, column, bg_color):
        # self.root = root
        self.width = width
        self.height = height
        self.row = row
        self.column = column
        self.bg_color = bg_color
        
        self.root = tk.Canvas(width= self.width, height= self.height, bg= self.bg_color)
        
        #row/column config
        self.root.place(x= int(self.row * self.width), y= int(self.column * self.height))

class Logger(FrameConstructor):

    def __init__(self, root, width, height, row, column, bg_color):
        #Inherit from FrameConstructor
        FrameConstructor.__init__(self, root, width, height, row, column, bg_color)
        
        # counter variables
        self.counter = -1
        self.running = False
        
        #aesthetics
        app_font= ('Calibri', 10)
        app_fg = 'silver'
        app_bg= 'black'

        # loads PhotoImages
        self.img_play = tk.PhotoImage(file="./assets/play.png")
        self.img_stop = tk.PhotoImage(file="./assets/pause.png")
        self.img_pause = tk.PhotoImage(file="./assets/stop.png")
        
        #Time Label
        self.label_time = tk.Label(self.root, text="Click Play to Start", font= app_font, fg= app_fg, bg= app_bg)
        self.label_time.place(x= 110, y = 10)

        #Timer Control buttons - play
        timer_play = tk.Button(self.root, image = self.img_play, borderwidth= 0, command= lambda: self.start_timer(), bg= self.bg_color)
        timer_play.image = self.img_play #keeps reference to image https://web.archive.org/web/20201111190625id_/http://effbot.org/pyfaq/why-do-my-tkinter-images-not-appear.htm
        timer_play.place(x= 10, y= 10)
        
        #Timer Control buttons - reset
        timer_reset = tk.Button(self.root, image = self.img_stop, borderwidth= 0, command= lambda: self.reset_timer(), bg= self.bg_color)
        timer_reset.image = self.img_stop
        timer_reset.place(x= 40, y= 10)
        
        #Timer Control buttons - stop
        timer_stop = tk.Button(self.root, image = self.img_pause, borderwidth= 0, command= lambda: self.stop_timer(), bg= self.bg_color)
        timer_stop.image = self.img_pause
        timer_stop.place(x= 70, y= 10)

        #Date Label
        current_date = time.strftime('%d/%m/%Y', time.localtime())
        date_label = tk.Label(self.root, text= current_date, font= app_font, fg= app_fg, bg= app_bg)
        date_label.place(x= self.width - 120, y = 10)

        #Week Label & DropDown
        OPTIONS = list(range(0, 23))
        week_label = tk.Label(self.root, text= 'Week: ', font= app_font, bg= self.bg_color)
        week_label.place(x= self.width - 120, y = 35)
        weeks_var = tk.StringVar(self.root)
        week_editor = ttk.Combobox(self.root, width= 3, values= OPTIONS)
        week_editor.place(x= self.width - 80, y = 35)

        #Subject Selector
        SUBJECTS = ['PWD (CM2015)', 'CSec(CM2025)', 'DNW(CM2015)', 'AppDev', 'Coding']
        subject_label = tk.Label(self.root, 
                                    text= 'Subject: ',
                                    font= app_font, 
                                    bg= self.bg_color)
        subject_label.place(x= 10, y = 35)
        subject_editor = ttk.Combobox(self.root, width= 10, values= SUBJECTS)
        subject_editor.place(x= 60, y = 35)

        #Upload Button
        upload_button = tk.Button(self.root, 
                                    text= "Log Session",
                                    command= lambda : self.add_one(
                                        subject_editor.get(),
                                        current_date, 
                                        self.counter, 
                                        week_editor.get()))
        upload_button.place(x = 10, y = 70, width= 380)
    
    def counter_init(self):
        if self.running:
            if self.counter == -1:
                display = '0'
            else:
                display = str(self.counter)

            self.label_time['text'] = display

            self.label_time.after(1000, self.counter_init)
            self.counter += 1
        
        elif self.running == False:
            self.counter = self.counter
    
    def start_timer(self):
        self.running = True
        self.counter_init()

    def stop_timer(self):
        self.running = False
        self.counter = self.counter

    def reset_timer(self):
        self.counter = -1
        if self.running == False:
            self.label_time['text'] = '0'

    #db functions
    def add_one(self, subject, date, time_spent, week):
        #db connection
        connect = sqlite3.connect('time_track.db')
        c = connect.cursor()
        
        # blank upload error handling
        if subject and week and (time_spent > 0):
            c.execute('INSERT INTO time_track VALUES (?, ?, ?, ?)', (subject, date, time_spent, week))
        else:
            raise RuntimeError('Blank values present')
        
        connect.commit()
        
        message = f'Successfully added: {subject} - {date} - {time_spent}s - {week} to db'
        
        print(message)

        #bd close connection
        connect.close()

class Grapher(FrameConstructor):
    def __init__(self, root, width, height, row, column, bg_color, period= None):
        #Inherit from FrameConstructor
        FrameConstructor.__init__(self, root, width, height, row, column, bg_color)
        
        self.period= period

        params = {
                    'font.size' : 6,
                    'axes.titlesize' : 6,
                    'axes.labelsize' : 6,
                    'legend.framealpha' : 0.2
        }
                
        plt.style.use('ggplot')

        plt.rcParams.update(params)

        fig = plt.Figure(figsize=(4, 3))
        fig.autofmt_xdate()

        axis_1 = fig.add_subplot(111)

        self.canvas = FigureCanvasTkAgg(fig, self.root)


        def redraw():
            axis_1.cla()

            graph_data = self.graph_data()

            if self.period == 'weekly':
                graph_data[0].plot(kind= 'bar', 
                                    stacked= True, 
                                    title= 'Minutes per week', 
                                    ylabel= 'Minutes', 
                                    xlabel = 'Weeks', 
                                    ax= axis_1)
                axis_1.legend(bbox_to_anchor= (1.1, 0.9))
                axis_1.axhline(y= 180 * 7, ls= '--')
                
            
            elif self.period == 'daily':
                graph_data[1].plot(kind= 'bar', 
                                    stacked= True, 
                                    title= 'Minutes per day', 
                                    ylabel= 'Minutes', 
                                    xlabel = 'Date', 
                                    ax= axis_1)
                axis_1.legend(bbox_to_anchor= (1.1, 0.9))
                axis_1.axhline(y= 180, ls= '--')
        
            for tick in axis_1.get_xticklabels():
                tick.set_rotation(0)
            
            self.canvas.draw()

            self.canvas.get_tk_widget().place(relheight= 1, relwidth= 1)
            

        update_button= ttk.Button(self.root, 
                                    text= 'Update', 
                                    command = lambda: redraw())
        update_button.place(x= 0, y= 0)

    @staticmethod
    def graph_data():
        con = sqlite3.connect('time_track.db')
        df_time = pd.read_sql_query('SELECT * FROM time_track', con)
        df_time['date'] = pd.to_datetime(df_time['date'], dayfirst= True).dt.strftime('%d-%m')
        df_time['time_spent'] = df_time['time_spent']/60
        con.close()

        df_group_week = df_time.groupby(['week', 'subject'])['time_spent'].sum().fillna(0).unstack()

        df_group_day = df_time.groupby(['date', 'subject'])['time_spent'].sum().fillna(0).unstack()

        return [df_group_week, df_group_day.tail(7)]



def delete_one(rowid):
    connect = sqlite3.connect('time_track.db')
    c = connect.cursor()
    #execute db delete, (rowid,) included because we pass in a sequence to make the parameters a tuple
    #https://stackoverflow.com/questions/16856647/sqlite3-programmingerror-incorrect-number-of-bindings-supplied-the-current-sta
    c.execute('DELETE FROM time_track WHERE rowid = (?)', (rowid,))
    connect.commit()
    message = f'Successfully deleted: id:{rowid} from db'
    print(message)
    connect.close()
    





app = Study_App()
app.geometry('850x720')
app.mainloop()
