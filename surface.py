import tkinter as tk
from tkinter.filedialog import *
from tkinter import ttk
import predict
import cv2
import os
import numpy as np
from PIL import Image, ImageTk
from recoginzer_licenseplate import *
import threading
import time

class Surface(ttk.Frame):
    pic_path = ""
    viewhigh = 600
    viewwide = 600
    update_time = 0

    def __init__(self, win):
        ttk.Frame.__init__(self, win)
        frame_left = ttk.Frame(self)
        frame_right1 = ttk.Frame(self)
        frame_right2 = ttk.Frame(self)
        win.title("车牌识别")
        win.state("zoomed")
        self.pack(fill=tk.BOTH, expand=tk.YES, padx="5", pady="5")
        frame_left.pack(side=LEFT, expand=1, fill=BOTH)
        frame_right1.pack(side=TOP, expand=1, fill=tk.Y)
        frame_right2.pack(side=RIGHT, expand=0)
        ttk.Label(frame_left, text='原图：').pack(anchor="nw")
        ttk.Label(frame_right1, text='车牌位置：').grid(column=0, row=0, sticky=tk.W)

        from_pic_ctl = ttk.Button(frame_right2, text="来自图片", width=20, command=self.from_pic)
        cutCarPic = ttk.Button(frame_right2, text="截取车牌", width=20,command=self.cutlicen)
        cutCarNum = ttk.Button(frame_right2, text="分割字符", width=20, command=self.cutlicennum)
        reCarPic = ttk.Button(frame_right2, text="识别车牌", width=20,command=self.reconlicen)
        exitfram =ttk.Button(frame_right2, text="清除", width=20,command=self.clean_window)

        self.image_ctl = ttk.Label(frame_left)
        self.image_ctl.pack(anchor="nw")

        self.roi_ctl = ttk.Label(frame_right1)
        self.roi_ctl.grid(column=0, row=1, sticky=tk.W)

        ttk.Label(frame_right1, text='识别结果：').grid(column=0, row=2, sticky=tk.W)
        self.r_ctl = ttk.Label(frame_right1, text="")
        self.r_ctl.grid(column=0, row=3, sticky=tk.W)

        from_pic_ctl.pack(anchor="se", pady="5")
        cutCarPic.pack(anchor="se", pady="5")
        cutCarNum.pack(anchor="se", pady="5")
        reCarPic.pack(anchor="se", pady="5")


        exitfram.pack(anchor="se", pady="5")


    def get_imgtk(self, img_bgr):
        img = cv2.cvtColor(img_bgr, cv2.COLOR_BGR2RGB)
        im = Image.fromarray(img)
        imgtk = ImageTk.PhotoImage(image=im)
        wide = imgtk.width()
        high = imgtk.height()
        if wide > self.viewwide or high > self.viewhigh:
            wide_factor = self.viewwide / wide
            high_factor = self.viewhigh / high
            factor = min(wide_factor, high_factor)
            wide = int(wide * factor)
            if wide <= 0: wide = 1
            high = int(high * factor)
            if high <= 0: high = 1
            im = im.resize((wide, high), Image.ANTIALIAS)
            imgtk = ImageTk.PhotoImage(image=im)
        return imgtk

    def from_pic(self):
        self.thread_run = False
        self.pic_path = askopenfilename(title="选择识别图片", filetypes=[("jpg图片", "*.jpg")])
        if self.pic_path:
            with open('pathpic.txt','w') as f:
                f.write(str(self.pic_path))
            img_bgr = predict.imreadex(self.pic_path)
            self.imgtk1 = self.get_imgtk(img_bgr)
            self.image_ctl.configure(image=self.imgtk1)

    def cutlicen(self):
        print(self.pic_path)
        os.system('python /Users/wangxin/PycharmProjects/ParkingPaymentSystem/recoginzer_licenseplate.py')
        time.sleep(2)
        picpath='/Users/wangxin/PycharmProjects/ParkingPaymentSystem/test_images/cut.png'
        if os.path.exists(picpath):
            img_bgr = predict.imreadex(picpath)
            self.imgtk2 = self.get_imgtk(img_bgr)
            self.roi_ctl.configure(image=self.imgtk2)

    def cutlicennum(self):
        os.system("python /Users/wangxin/PycharmProjects/ParkingPaymentSystem/recoginzer_licenseplate2.py")
        time.sleep(2)



    def reconlicen(self):
        PP = os.popen('python train_recoginzer_P.py recoginzer', 'r', 1)
        LL = os.popen('python train_recoginzer_L.py recoginzer', 'r', 1)
        DD = os.popen('python train_recoginzer_D.py recoginzer', 'r', 1)
        carnum=PP.read()+LL.read()+DD.read()
        self.r_ctl.configure(text=carnum)


    # 读取图片文件
    def imreadex(filename,x):
        return cv2.imdecode(np.fromfile(filename, dtype=np.uint8), cv2.IMREAD_COLOR)

    def clean_window(self):
        filurl = '/Users/wangxin/PycharmProjects/ParkingPaymentSystem/test_images'
        if os.path.exists(filurl + '/cut.png'):
            os.remove(filurl + '/cut.png')
        for i in range(1, 9):
            if os.path.exists(filurl + '/' + str(i) + '.bmp'):
                os.remove(filurl + '/' + str(i) + '.bmp')


def close_window():
    print("destroy")
    win.destroy()


if __name__ == '__main__':
    win = tk.Tk()
    surface = Surface(win)
    win.protocol('WM_DELETE_WINDOW', close_window)
    win.mainloop()

