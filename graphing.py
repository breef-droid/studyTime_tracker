import sqlite3
import matplotlib.pyplot as plt
import time
from matplotlib import style
style.use('fivethirtyeight')


def graph_data_weekly():
    conn = sqlite3.connect('time_track.db')
    c = conn.cursor()

    #query
    c.execute('''SELECT week, subject, SUM(time_spent) 
                FROM time_track
                GROUP BY week, subject;''')
    weeks, subjects, total_time = [], [], []
    #loop through data & append to lists
    for row in c.fetchall():
        weeks.append(row[0])
        subjects.append(row[1])
        total_time.append(row[2])

    c.close()
    conn.close()
    
    return [weeks, subjects, total_time]

data = graph_data_weekly()

labels = data[0]
subjects = data[1]
total_time = data[2]
width = 0.35
fig, ax = plt.subplots()

ax.bar(labels, subjects, width)


