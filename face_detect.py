# -*- coding: utf-8 -*-
"""
Created on Fri Feb 18 14:34:44 2022

@author: admin
"""

import cv2

# 待检测的图片路径
imagepath="T.jpg"

image = cv2.imread(imagepath)
gray = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)


'''
# 获取人脸识别训练数据

对于人脸特征的一些描述，opencv在读取完数据后很据训练中的样品数据，
就可以感知读取到的图片上的特征，进而对图片进行人脸识别。
xml数据下载，
参考：https://github.com/opencv/opencv/tree/master/data/haarcascades
'''
face_cascade = cv2.CascadeClassifier(r'C:\\Python38\\Lib\\site-packages\\cv2\\data\\haarcascade_frontalface_default.xml')

# 探测人脸
# 根据训练的数据来对新图片进行识别的过程。
faces = face_cascade.detectMultiScale(
  gray,
  scaleFactor = 1.15,
  minNeighbors = 5,
  minSize = (20,20),
  #flags = cv2.HAAR_SCALE_IMAGE
)

# 我们可以随意的指定里面参数的值，来达到不同精度下的识别。返回值就是opencv对图片的探测结果的体现。

# 处理人脸探测的结果
print ("发现{0}个人脸!".format(len(faces)))
for(x,y,w,h) in faces:
    cv2.rectangle(image,(x,y),(x+w,y+w),(0,255,0),2)
    # cv2.circle(image,((x+x+w)/2,(y+y+h)/2),w/2,(0,255,0),2)

cv2.imshow("image",image)
cv2.imwrite("123.jpg", image)
cv2.waitKey(0)
cv2.destroyAllWindows()