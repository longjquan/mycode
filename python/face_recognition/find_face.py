import cv2

save_path = 'G:\\'

cascade = cv2.CascadeClassifier(r'C:\Users\quan\Desktop\pythonlianxi\cv2\data\haarcascade_frontalface_default.xml')
#上述的训练数据*.xml是需要下载
cap = cv2.VideoCapture(0)

i = 0

while True:

    ret,frame = cap.read()

    gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)

    rect = cascade.detectMultiScale(gray,scaleFactor=1.3,minNeighbors=9,minSize=(50,50),flags = 0)
    #print ("rect",rect)

    if not rect is (): 

        for x,y,z,w in rect:

            roiImg = frame[y:y+w,x:x+z]

            cv2.imwrite(save_path+str(i)+'.jpg',roiImg)

            cv2.rectangle(frame,(x,y),(x+z,y+w),(0,0,255),2)

            i +=1

    #cv2.imshow('frame',frame)       

    if cv2.waitKey(1) &0xFF == ord('q'):

        break

cap.release()

cv2.destroyAllWindows()
