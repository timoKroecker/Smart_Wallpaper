import ctypes
import os
import time
import platform

def save_img(img, img_name):
    img.save(img_name)
    #time.sleep(1)

def change_wallpaper(absolute_path):
    osys = platform.system()
    if(osys == "Windows"):
        ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path , 2)
        #time.sleep(0.5)
        ctypes.windll.user32.SystemParametersInfoW(20, 0, absolute_path , 2)
        time.sleep(0.5)
    if(osys == "Linux"):
        command = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri " + absolute_path
        command_dark = "/usr/bin/gsettings set org.gnome.desktop.background picture-uri-dark " + absolute_path
        os.system(command)
        os.system(command_dark)