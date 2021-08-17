import sqlite3

# table creation & type allocation
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

def show_all():
    # open db & init cursor
    connect = sqlite3.connect('time_track.db')
    c = connect.cursor()
    #execute query
    c.execute('SELECT rowid, * from time_track')
    # init results 
    items = c.fetchall()
    for item in items:
        print(item)
    #close db
    connect.close()

def add_one(subject, date, time_spent, week):
    connect = sqlite3.connect('time_track.db')
    c = connect.cursor()
    c.execute('INSERT INTO time_track VALUES (?, ?, ?, ?)', (subject, date, time_spent, week))
    connect.commit()
    message = f'Successfully added: {subject} - {date} - {time_spent}s - {week} to db'
    print(message)
    connect.close()

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

show_all()

