import ctypes
import time

def save_img(img, img_name):
    img.save(img_name)
    #time.sleep(1)

def change_wallpaper(absolute_path):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path , 2)
    #time.sleep(0.5)
    ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path , 2)
    time.sleep(0.5)