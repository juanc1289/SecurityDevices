import cv2
import time
from time import sleep


start_time = time.time()

cap = cv2.VideoCapture(0)

ret, frame1 = cap.read()

print("--- %s seconds ---" % (time.time() - start_time))
print ("shape",frame1.shape)
print ("size",frame1.size)
print ("dtype",frame1.dtype)


while (cap.isOpened()):

    ret, img = cap.read()
    if ret == False:
        break

    cv2.imshow('Image',img)

    cv2.imshow('Mask Red',mask_hsv_r)
    cv2.imshow('Mask Green',mask_hsv_g)
    
    key = cv2.waitKey(1)
    if key==27:
        break


cap.release()
cv2.destroyAllWindows()
print("--- %s seconds ---" % (time.time() - start_time))