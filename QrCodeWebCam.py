from cv2 import cv2
import numpy as np 
from pyzbar.pyzbar import decode   #pyzbar helps in detection and decoding of the qrcode

cap=cv2.VideoCapture(0)
# cap.set(3,1280)  #3 is the id for width which is set as 1280
# cap.set(4,720)  #4 is the id for height


while(True):
    success,frame=cap.read()

    for i in decode(frame):
        myData=i.data.decode("utf-8")   #converts bytes to string value
        print(myData)
        
        #Drawing rectangle on frame (stays static w.r.t orientation.... cuz it's a rectangle(stays fixed))
        #  cv2.rectangle(frame,(i.rect.left,i.rect.top),(i.rect.left+i.rect.width,i.rect.top+i.rect.height),(0,0,0),2)

        #Drawing polygon on frame (tilts w.r.t orientation)
        pts=np.array([i.polygon],np.int32)
        # When using a -1, the dimension corresponding to the -1 will be the product of the dimensions 
        #of the original array divided by the product of the dimensions given to reshape so as to maintain the same number of elements.
        pts=pts.reshape((-1,1,2))  
        cv2.polylines(frame,[pts],True,(0,0,255),2)
        # print(pts)
     
        #Display text
        rect_pts=i.rect #using rect point as origin for text as we don't want the text to tilt with the qrcode
        fontScale=0.8
        thickness=1
        cv2.putText(frame,myData,(rect_pts[0],rect_pts[1]),cv2.FONT_HERSHEY_SIMPLEX,fontScale,(255,0,0),thickness)
        print(rect_pts)

    cv2.imshow('Result',frame)

    ch=cv2.waitKey(1) #delay of 1ms    
    if(ch==113):
        break
      