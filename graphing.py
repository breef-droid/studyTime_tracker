import sqlite3
import matplotlib.pyplot as plt
import time
import pandas as pd

def db_to_df():
    # db connection
    con = sqlite3.connect('time_track.db')
    c = con.cursor()

    # Read db & export to csv
    df_time_track = pd.read_sql_query('SELECT rowid, * from time_track', con)
    # df_time_track.to_csv('data.csv')

    c.close()
    con.close()

    return df_time_track

def df_graphs():
    # Read csv to df
    df_time = db_to_df()
    # Converts df time to minutes
    df_time['time_spent'] = df_time['time_spent']/60

    # Style graph
    plt.style.use('seaborn')
    # Week series
    df_group_week = df_time.groupby(['week', 'subject'])['time_spent'].sum().fillna(0).unstack()
    # Weekly plot
    weekly_graph = df_group_week.plot(kind= 'bar', stacked= True, title= 'Minutes per week', ylabel= 'Minutes', xlabel = 'Weeks')
    # Day series
    df_group_daily = df_time.groupby(['date', 'subject'])['time_spent'].sum().fillna(0).unstack()
    # # Daily plot
    # daily_graph = df_group_daily.plot(kind= 'bar', stacked= True, title= 'Minutes per day', ylabel= 'Minutes', xlabel = 'Date')

    return weekly_graph
    



