#Color Picker Code
#Ref: https://docs.opencv.org/4.x/d7/d4d/tutorial_py_thresholding.html
#Ref: https://ckyrkou.medium.com/color-thresholding-in-opencv-91049607b06d

import numpy as np
import cv2
from matplotlib import pyplot as plt
cap = cv2.VideoCapture(0)

while(True):
    # Capture frame-by-frame
    ret, frame = cap.read()
    edges = cv2.Canny(frame,100,200)
    lower_color_bounds = (0, 0, 80)
    upper_color_bounds = (50,50,250)
    # Our operations on the frame come here
    #gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
   # gray = cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
    mask = cv2.inRange(frame,lower_color_bounds,upper_color_bounds )
    mask_rgb = cv2.cvtColor(mask,cv2.COLOR_GRAY2BGR)
    frame = frame & mask_rgb
    # Display the resulting frame
    cv2.imshow('frame',mask)
   # plt.subplot(122),plt.imshow(edges,cmap = 'gray')
   # plt.title('Edge Image'), plt.xticks([]), plt.yticks([])
   # plt.show()
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()