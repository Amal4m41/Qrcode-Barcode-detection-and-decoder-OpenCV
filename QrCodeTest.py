from cv2 import cv2
import numpy as np 
from pyzbar.pyzbar import decode   #pyzbar helps in detection and decoding of the qrcode


#observing the image
img=cv2.imread('qr_sample1.png')
code=decode(img)
# print(code)
# [Decoded(data=b'Messi is the best', type='QRCODE', rect=Rect(left=16, top=16, width=168, height=168),
#  polygon=[Point(x=16, y=16), Point(x=16, y=184), Point(x=184, y=184), Point(x=184, y=16)])]

for i in code:
    # print(type(i))  #<class 'pyzbar.pyzbar.Decoded'>
    # print(i.rect)   #Rect(left=16, top=16, width=168, height=168)
    # print(i.data)  #b'Messi is the best'   (Data in bytes)
    # myData=i.data.decode("utf-8")   #converts bytes to string value
    # print(myData)
    print(i.rect.left)

    