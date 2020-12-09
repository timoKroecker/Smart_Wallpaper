import ctypes
import os
import time

def save_img(img, img_name):
    img.save(img_name)
    #time.sleep(1)

def change_wallpaper(absolute_path, osys):
    if(osys.lower() == "windows"):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path , 2)
        #time.sleep(0.5)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path , 2)
        time.sleep(0.5)
    if(osys.lower() == "linux"):
        os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + absolute_path)