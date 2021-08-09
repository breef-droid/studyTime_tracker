from tkinter import *
from tkinter import ttk
import helpers

#root init
root = Tk()

helpers.themes(root)

helpers.frame_semmester(root)
helpers.frame_weekly(root)
helpers.frame_update(root)
helpers.frame_track(root)

# loop init
root.mainloop()
