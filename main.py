# import argparse

import sys
import math
from pathlib import Path
from PIL import Image
import tkinter
import tkinter.ttk
from tkinter import filedialog
import threading
import cProfile

from img_proc import _combine_image_
from img_proc import _list_img_


default_path = 'C:\\Users\\THUChenYusi\\Pictures\\anime'
if not Path(default_path).exists():
    print("Directory img not exists")
    Path(default_path).mkdir()
    print("Directory img created")

# parser = argparse.ArgumentParser()
# parser.add_argument("-p", "--path",  default=default_path, help="Path of posters directory")
# parser.add_argument("-W", "--Width", type=int, default=400, help="Width of a poster in the posterwall")
# parser.add_argument("-H", "--Height", type=int, default=592, help="Height of a poster in the posterwall")
# args = parser.parse_args()

root = tkinter.Tk()
root.title("Yuu")

mainframe = tkinter.ttk.Frame(root, padding="3 3 12 12")
mainframe.grid(column=0, row=0, sticky=(tkinter.N, tkinter.W, tkinter.E, tkinter.S))
root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)

path_show = tkinter.StringVar()
dir_path = default_path
path_show.set(dir_path)
tkinter.ttk.Label(mainframe, textvariable=path_show).grid(column=1,columnspan=2, row=0, sticky=(tkinter.W, tkinter.E))

def browsefunc():
    global dir_path
    dir_path = filedialog.askdirectory()
    path_show.set(dir_path)
tkinter.ttk.Button(mainframe, text="Browse", command=browsefunc).grid(column=2, row=1, sticky=tkinter.W)

tkinter.ttk.Label(mainframe, text="Columns:").grid(column=1, row=2, sticky=tkinter.W)

columns_num = tkinter.StringVar()
columns_num_entry = tkinter.ttk.Entry(mainframe, width=7, textvariable=columns_num)
columns_num_entry.grid(column=2, row=2, sticky=(tkinter.W, tkinter.E))

tkinter.ttk.Label(mainframe, text="Rows:").grid(column=1, row=3, sticky=tkinter.W)

rows_num_show = tkinter.StringVar()
tkinter.ttk.Label(mainframe, textvariable=rows_num_show).grid(column=2, row=3, sticky=(tkinter.W, tkinter.E))

def Generate(*args):
    global rows_num_show
    try:
        img_list = _list_img_(dir_path)
        columns = int(columns_num.get())
        row = math.ceil(len(img_list)/columns)
        rows_num_show.set(row)
        _combine_image_(img_list,columns)
    except ValueError:
        pass
tkinter.ttk.Button(mainframe, text="Generate", command=Generate).grid(column=2, row=4, sticky=tkinter.W)

for child in mainframe.winfo_children(): 
    child.grid_configure(padx=5, pady=5)

columns_num_entry.focus()
root.bind("<Return>", Generate)

root.mainloop()
