import cv2
import random
import time
startTime = time.time()
def TakeSnap():
    number = random.randint(0,100)
    videoCaptureObject=cv2.VideoCapture(0) 
    result = True
    while(result):
        ret,frame = videoCaptureObject.read()
        imageName = "img" + str(number) + ".png"
        cv2.imwrite(imageName,frame)
        startTime = time.time
       # result = False
    videoCaptureObject.release() 
    cv2.destroyAllWindows()
    return imageName 
TakeSnap()
