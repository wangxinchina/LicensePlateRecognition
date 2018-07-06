# import os
#
# os.system("python train_recoginzer_P.py")
# os.system('python train_recoginzer_L.py')
# os.system('python train_recoginzer_D.py')
import tkinter as tk
from tkinter.filedialog import askopenfilename

from PIL import Image, ImageTk

def choosepic():

    path_ = askopenfilename()
    path.set(path_)
    img_open = Image.open(path.get())
    img = ImageTk.PhotoImage(img_open)
    img
    chepaipic = tk.Label(window,image=img_open).grid(row=1, column=0)
    # chepaipic.configure(image=img)
    # chepaipic.image = img



def cutlicen():
    pass

def reconlicen():
    pass

window= tk.Tk()
window.title('车牌识别系统')
window.geometry('900x600+%d+%d'%((window.winfo_screenwidth()-900)/2,(window.winfo_screenheight()-600)/2))

path = tk.StringVar()
var=tk.StringVar()
imgpath=tk.StringVar()
# img= Image.open('timg.png')
# bm=ImageTk.PhotoImage(img)
img2=Image.open('test_images/cut.png')
bm2=ImageTk.PhotoImage(img2)




tk.Label(window,text='原图:').grid(row = 0, column = 0)

tk.Label(window,text = "图片路径:").grid(row = 2, column = 0)
filepath=tk.Entry(window,state='readonly', textvariable = path,width=30).grid(row = 3, column = 1)
tk.Button(window, text = "选择", command = choosepic).grid(row = 4, column = 2)

# tk.Button(frm_r, text = "截取车牌", command = cutlicen).grid(row = 0, column = 0)
# tk.Label(frm_r,text='车牌图:').grid(row = 1, column = 0)
# tk.Label(frm_r,bg='green',image=bm2,height=20,width=40).grid(row = 2, column = 0)
# tk.Button(frm_r, text = "识别车牌", command = reconlicen).grid(row = 3, column = 0)
# tk.Label(frm_r,text='识别结果:').grid(row = 4, column = 0)
# tk.Entry(frm_r,width=15).grid(row = 5, column = 0)

window.mainloop()






#
# class chepaiFrom(object):
#     def __init__(self):
#         self.window= tk.Tk()
#         self.window.title('车牌识别系统')
#         self.window.geometry('900x600+%d+%d' % ((self.window.winfo_screenwidth() - 900) / 2, (self.window.winfo_screenheight() - 600) / 2))
#         # # 主框架
#         # self.frm = tk.Frame(self.window)
#         # self.frm.grid()
#
#         self.path = tk.StringVar()
# #         # self.var = tk.StringVar()
# #         # self.imgpath = tk.StringVar()
# #         # self.img = Image.open('timg.png')
# #         # self.bm = ImageTk.PhotoImage(self.img)
# #         # self.img2 = Image.open('test_images/cut.png')
# #         # self.bm2 = ImageTk.PhotoImage(self.img2)
#         tk.Label(self.window, text='原图:').grid(row=0, column=0)
#         # self.piccar=tk.Label(self.window).grid(row=1, column=0)
#         tk.Label(self.window, text="图片路径:").grid(row=2, column=0)
#         self.picPath=tk.Entry(self.window, textvariable=self.path, width=30).grid(row=2, column=1)
#         tk.Button(self.window, text="选择", command=self.selectPath).grid(row=2, column=2)
#
#         tk.Label(self.window, text='车牌图:').grid(row=0, column=3)
#         self.chepaiPic=tk.Label(self.window, height=20, width=40).grid(row=1, column=3)
#         tk.Label(self.window, text='识别结果:').grid(row=2, column=3)
#         self.result=tk.Label(self.window).grid(row=3, column=3)
#         tk.Button(self.window, text="截取车牌", command=self.cutlicen).grid(row=4, column=3)
#         tk.Button(self.window, text="识别车牌", command=self.reconlicen).grid(row=5, column=3)
#
#     def selectPath(self):
#         path_ = askopenfilename()
#         self.path.set(path_)
#         # print(self.path.get())
#         # print(dir(self.piccar))
#         img_open = Image.open(self.path.get())
#         img = ImageTk.PhotoImage(img_open)
#         self.piccar = tk.Label(self.window,image=img).grid(row=1, column=0)
#
#
#     def cutlicen(self):
#         pass
#
#     def reconlicen(self):
#         pass
#
#
# def main():
#     chepai=chepaiFrom()
#     chepai.window.mainloop()
#
# if __name__=='__main__':
#     main()