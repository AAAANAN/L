#1. 请写出对numpy、matplotlib、opencv导入库文件的编程语句?（4分）
import numpy as np
import matplotlib.pyplot as plt
import cv2
#2. 请用编程语句实现读入彩色图片bawei_zhoukao1并显示图像。（8分）
img=cv2.imread('bawei_zhoukao1.jpg')
#3. 请在图片bawei_zhoukao1上画出矩型框的编程语句（8分）
cv2.rectangle(img,(12,0),(1180,128),(0,255,0),3)
#4. 请在图片bawei_zhoukao1上打印如下文字“You are great, keep on trying”，并显示。（8分）
font=cv2.FONT_HERSHEY_SIMPLEX
cv2.putText(img,'You are great, keep on trying',(83,123),font,2,(12,152,250),4)
cv2.imshow('image',img)
cv2.waitKey(0)
#5. 请写出OpenCV中删除建立的全部窗口的库函数语句（8分）
cv2.destroyAllWindows()
#6. 请问在OpenCV中，能将图像上下翻转、左右翻转，以及同时均可的库函数是 ? （8分）cv2.filp()
#第三题
#请使用python编程对笔记本电脑摄像头视频进行捕获并保存在本地。（40分）
cap=cv2.VideoCapture(0)   #捕获视频
i=1
while(i):
    ret,frame=cap.read()  #读取视频
    # gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)   #摄像头灰色
    gray=cv2.cvtColor(frame,cv2.NORMAL_CLONE)   #摄像头彩色
    cv2.imshow('frame',gray)  #显示
    fourcc = cv2.VideoWriter_fourcc(*'XVID')
    out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))
    a = ["0", "cam01.jpg", "cam02.jpg", "cam03.jpg", "cam04.jpg", "cam05.jpg"]
    if (cv2.waitKey(1) & 0xFF == ord('s')):
        cv2.imwrite(a[i], frame)
        i += 1
    elif (cv2.waitKey(1) & 0xFF == ord('z')):#保存视频
        out.write(frame)
        cv2.imshow('frame', frame)
        break
    elif (cv2.waitKey(1) & 0xFF == ord('q')): #按q键退出
        break
cap.release()  #释放摄像头
cv2.destroyAllWindows()  #删除所有窗口