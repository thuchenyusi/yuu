import math
import threading
from pathlib import Path
from PIL import Image

def _list_img_(dir_path):
    if not Path(dir_path).exists():
        print("Directory not exists!")
        return
    img_list = [x for x in (Path(dir_path)).iterdir() if (x.is_file())]
    if not img_list:
        print("No image detected")
        exit()
    return img_list

def _combine_image_(img_list,column,size=(400,592)):
    imgs = [Image.open(i) for i in img_list]
    row = math.ceil(len(imgs)/column)
    target = Image.new('RGB', (size[0]*column, size[1]*row))
    pasteImage(column,row,size,target,imgs).start()

class pasteImage(threading.Thread):
   def __init__(self,column,row,size,target,imgs):
        threading.Thread.__init__(self)
        self.column = column
        self.row = row
        self.size = size
        self.target = target
        self.imgs = imgs
   def run(self):
      _paste_(self.column,self.row,self.size,self.target,self.imgs)

def _paste_(column,row,poster_size,target,imgs):
    row_paste_threads = []
    threadLock = threading.Lock()
    for i in range(row):
        t = threading.Thread(target=_row_paste_,args=(i,column,poster_size,target,imgs,threadLock))
        t.start()
        row_paste_threads.append(t)
    for r_p_t in row_paste_threads:
        r_p_t.join()
    target.show()
    image_file = 'C:\\Users\\THUChenYusi\\Pictures\\poster.jpg'
    _image_save_(target,image_file)

def _row_paste_(row_pos,cols,poster_size,target,source_imgs,threadLock):
    width = poster_size[0]
    height = poster_size[1]
    row_size = (poster_size[0]*cols,poster_size[1])
    row_target = Image.new('RGB',row_size)
    pos = row_pos * cols
    for col, image in enumerate(source_imgs[pos:pos+cols]):
        box = (width*col, 0, width*(col + 1), height)
        row_target.paste(image.resize(poster_size), box)
    threadLock.acquire()
    target.paste(row_target, (0,height*row_pos))
    threadLock.release()

def _image_save_(img,save_pos):
    img.save(save_pos)