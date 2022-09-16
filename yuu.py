import sys
import math
import os
from pathlib import Path
from PIL import Image
import tkinter
from tkinter import N,S,E,W
from tkinter import ttk
import cProfile

from img_proc import _combine_image_
from img_proc import _list_img_

from message_box import _ask_dir_

default_path = os.environ['USERPROFILE'] + '\\Pictures'
if not Path(default_path).exists():
    print("Directory img not exists")
    Path(default_path).mkdir()
    print("Directory img created")

root = tkinter.Tk()
root.title("Yuu")
root.iconbitmap('yuu.ico')
root.resizable(0,0)

mainframe = ttk.Frame(root, padding="12 12 12 12")
mainframe.grid(column=0, row=0, sticky=(N,S,E,W))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

path_show = tkinter.StringVar()
dir_path = default_path
path_show.set(dir_path)
ttk.Label(mainframe, textvariable=path_show).grid(column=0,columnspan=2, row=0, sticky=(E,W))

# ttk.Checkbutton(mainframe, text="Iterate").grid(column=0, row=1, sticky=S+N)

def browsefunc():
    global dir_path
    dir_path = _ask_dir_(dir_path) 
    path_show.set(dir_path)
ttk.Button(mainframe, width=7,
 text="Browse", command=browsefunc).grid(column=1, row=1, sticky=(N+S), pady=3)

ttk.Label(mainframe, text="Columns").grid(column=0, row=2)

ttk.Label(mainframe, text="Rows").grid(column=1, row=2)

columns_num = tkinter.IntVar(value=10)
columns_num_entry = ttk.Entry(mainframe, width=7, textvariable=columns_num, justify='center')
columns_num_entry.grid(column=0, row=3)

def rows_num_update():
    row = math.ceil(len(_list_img_(dir_path))/columns_num.get())
    rows_num_show.set(row)
rows_num_show = tkinter.IntVar()
rows_num_update()
ttk.Label(mainframe, width=7, relief=tkinter.SUNKEN,
 textvariable=rows_num_show, anchor='c').grid(column=1, row=3)

def callback_rows_num_update(var, indx, mode): 
    rows_num_update()
columns_num.trace_add(mode='write',callback=callback_rows_num_update)
path_show.trace_add(mode='write',callback=callback_rows_num_update)

ttk.Label(mainframe, text="Height").grid(column=0, row=4)
ttk.Label(mainframe, text="Width").grid(column=1, row=4)

width_pixel = tkinter.IntVar(value=400)
width_pixel_entry = ttk.Entry(mainframe, width=7, textvariable=width_pixel, justify='center')
width_pixel_entry.grid(column=0, row=5)

height_pixel = tkinter.IntVar(value=592)
height_pixel_entry = ttk.Entry(mainframe, width=7, textvariable=height_pixel, justify='center')
height_pixel_entry.grid(column=1, row=5)

def Generate(*args):
    global rows_num_show
    try:
        img_list = _list_img_(dir_path)
        _combine_image_(img_list=img_list,
        column=columns_num.get(),
        size=(width_pixel.get(),height_pixel.get()))
    except ValueError:
        pass
ttk.Button(mainframe, width=7, text="Gen", command=Generate).grid(column=1, row=6, pady=3)

columns_num_entry.focus()
root.bind("<Return>", Generate)

mainframe.columnconfigure(0, weight=3)
mainframe.columnconfigure(1, weight=3)
mainframe.rowconfigure(0, weight=2)
mainframe.rowconfigure(1, weight=1)
mainframe.rowconfigure(2, weight=1)
mainframe.rowconfigure(3, weight=1)
mainframe.rowconfigure(4, weight=1)
mainframe.rowconfigure(5, weight=1)
mainframe.rowconfigure(6, weight=1)

root.mainloop()
