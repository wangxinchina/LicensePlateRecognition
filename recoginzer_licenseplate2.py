import cv2
import numpy as np
import copy
import os,sys
from PIL import Image
import time
from cv2 import imread


#蓝色的范围
lower_blue = np.array([130,60,0])
upper_blue = np.array([255,110,60])
#白色的范围
lower_whit= np.array([160,160,160])
upper_whit= np.array([255,255,255])

# 核大小 3*3
kernel = np.ones((5, 5), np.uint8)
kernel2 = np.ones((3, 3), np.uint8)

def cutPic(upper,lower,dila_times,ero_times):
    # 读取图片,修剪多余的边
    img = cv2.imread(os.path.dirname(__file__) + '/test_images/cut.png')
    x_y_chan = img.shape
    cropImgw = img[10:5 + x_y_chan[0] - 20, 10:5 + x_y_chan[1] - 10]
    makr = cv2.inRange(cropImgw, lower, upper)
    dilation = cv2.dilate(makr, kernel2, iterations=dila_times)
    erode = cv2.erode(dilation, kernel2, iterations=ero_times)

    # 轮廓检测
    image, contours, hier=cv2.findContours(erode, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
    #轮廓列表
    box_list =[]
    #x列表
    x_list = []
    #筛选掉面积过小的轮廓
    for c in contours:
        x,y,w,h= cv2.boundingRect(c)
        area=cv2.contourArea(c)
        # print(area,w/h,x_y_chan[0]/x_y_chan[1])
        print('11111',w/h,w,h,area)
        if  (w/h)<0.4 or (w/h)>0.6 :
            continue
        print(area,x,y,w/h)
        box_list.append([x,y,w,h])

    #把轮廓的x位置放入x列表
    for i in range(0,len(box_list)):
        x_list.append(box_list[i][0])

    #深度拷贝x列表
    x_listcopy =copy.deepcopy(x_list)
    #排序
    x_listcopy.sort()

    #从左到右取出各符号
    for i in range(0,len(x_listcopy)):
        listnum=x_list.index(x_listcopy[i])
        #x位置
        x=box_list[listnum][0]
        #y位置
        y=box_list[listnum][1]
        #宽度
        w=box_list[listnum][2]
        #高度
        h=box_list[listnum][3]

        cv2.rectangle(cropImgw, (x, y), (x + w, y + h), (0, 0, 0), 2)
        cropImg = cropImgw[y:y + h, x:x + w]
        im_gray = cv2.cvtColor(cropImg, cv2.COLOR_BGR2GRAY)
        ret, thresh=cv2.threshold(im_gray,127,255,cv2.THRESH_BINARY)
        cv2.imwrite(os.path.dirname(__file__) + '/test_images/' + str(i + 1) + '.bmp', thresh)
        filein = os.path.dirname(__file__) + '/test_images/'+str(i + 1) +'.bmp'
        fileout = os.path.dirname(__file__) + '/test_images/'+str(i + 1) +'.bmp'
        width = 32
        height = 40
        type = 'bmp'
        ResizeImage(filein, fileout, width, height, type)






#截取目标范围：从大图中截取出车牌的位置图片
def roughCutPic(imgnum,upper,lower,dila_times,ero_times):
    imgb = cv2.imread(imgnum)
    makr = cv2.inRange(imgb,lower,upper)

    # 膨胀
    dilation = cv2.dilate(makr, kernel2, iterations=dila_times)

    #腐蚀
    erode = cv2.erode(dilation,kernel2,iterations=ero_times)

    # 核大小 3*3
    global contours
    # 轮廓检测
    image, contours, hier = cv2.findContours(dilation, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)

    for c in contours:

        x, y, w, h = cv2.boundingRect(c)
        area = cv2.contourArea(c)
        if area <2000:
            continue

        cropImg = imgb[y:y + h, x:x + w]
        cv2.imwrite(os.path.dirname(__file__) + '/test_images/cut.png',cropImg)

#统一图片尺寸
def ResizeImage(filein, fileout, width, height, type):
    img = Image.open(filein)
    out = img.resize((width, height),Image.ANTIALIAS)
    out.save(fileout, type)

def change():
    num = 1
    # cutPic(upper_whit, lower_whit, 3, 1)
    DIR = '/Users/wangxin/PycharmProjects/ParkingPaymentSystem/test_images'  # 要统计的文件夹
    while True:
        count=len([name for name in os.listdir(DIR) if os.path.isfile(os.path.join(DIR, name))])
        print(count)
        if count <9:
            cutPic(upper_whit, lower_whit,num, 1)
            num =num+1
        else:
            break

if __name__=="__main__":
    change()
    print('ok')
