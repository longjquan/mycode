
#coding:utf-8
import cv2
# 引入人像识别训练库“haarcascade_frontalface_default.xml
face_patterns = cv2.CascadeClassifier(r'C:\Users\quan\Desktop\pythonlianxi\cv2\data\haarcascade_frontalface_default.xml')
#读取图片
image=cv2.imread(r'C:\Users\quan\Desktop\pythonlianxi\liming.jpg')
#获取识别到到人脸
faces = face_patterns.detectMultiScale(image, scaleFactor=1.1, minNeighbors=4, minSize=(40, 40))
#cv2.namedWindow('Image')
#cv2.imshow('Image', faces)
#将识别到到人脸框出来
for (x, y, w, h) in faces:
    cv2.rectangle(image, (x, y), (x+w, y+h), (0, 255, 0), 2)
cv2.imwrite('qq.jpg', image)

print ('监控到%s张脸' % len(faces))

