from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk
import helpers, frametrack

#root init
root = Tk()

helpers.themes(root)

helpers.frame_semmester(root)
helpers.frame_weekly(root)
helpers.frame_update(root)
frametrack.frame_track(root)

# loop init
root.mainloop()
