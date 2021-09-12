from tkinter import messagebox
from tkinter import filedialog

def _ok_box_(t,m):
    return messagebox.askyesno(title=t, message=m)

def _ask_dir_(default_dir = None):
    get_dir = filedialog.askdirectory()
    if get_dir == '' and default_dir != None:
        return default_dir
    else:
        return get_dir

def _ask_save_(title=None,
            fileName=None,
            dirName=None,
            fileExt=".*",
            fileTypes=None):
    if fileTypes is None:
            fileTypes = [('all files', '.*')]
    options = {}
    options['defaultextension'] = fileExt
    options['filetypes'] = fileTypes
    options['initialdir'] = dirName
    options['initialfile'] = fileName
    options['title'] = title
    return filedialog.asksaveasfilename(**options)
