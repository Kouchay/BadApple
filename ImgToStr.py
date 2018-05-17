import numpy as np
import cv2
from PIL import Image
import time
import os
def ImgToStr(img):
    im = img
    img = im.convert('L')
    pix = img.load()
    width , height = im.size
    pic_str = ''
    for h in range(height):
        for w in range(width):
            if(int(pix[w,h])<=50):
                pic_str += '#'
            elif(int(pix[w,h])>50 and int(pix[w,h])<=100):
                pic_str += '@'
            elif(int(pix[w,h])>100 and int(pix[w,h])<=150):
                pic_str += '$'
            elif(int(pix[w,h])>150 and int(pix[w,h])<=200):
                pic_str += '&'
            else:
                pic_str += ' '
        pic_str += '\n'
    time.sleep(0.033333333)
    print(pic_str)
    #os.system("cls")

def video():
    cap = cv2.VideoCapture('bad apple.MP4')
	#cap = cv2.VideoCapture('视频路径')
    while(cap.isOpened()):
        ret, frame = cap.read()
        new_im = Image.fromarray(frame)
        ImgToStr(new_im)


if __name__=="__main__":
    video()
