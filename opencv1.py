import cv2
import time
from time import sleep


start_time = time.time()

cap = cv2.VideoCapture(0)
time.sleep(15)

ret, frame1 = cap.read()
time.sleep(0.1)
ret, frame2 = cap.read()
time.sleep(0.1)
ret, frame3 = cap.read()
time.sleep(0.1)
ret, frame4 = cap.read()
time.sleep(0.1)
ret, frame5 = cap.read()
time.sleep(0.1)
ret, frame6 = cap.read()
time.sleep(0.1)





print("--- %s seconds ---" % (time.time() - start_time))
#print ("shape",frame6.shape)
#print ("size",frame6.size)
#print ("dtype",frame6.dtype)


while (True):

    ret, img = cap.read()
    if ret == False:
        print("ret falso")
        break

    cv2.imshow('Image',img)

    key = cv2.waitKey(0)
    if key==27:
        break


cap.release()
cv2.destroyAllWindows()
print("--- %s seconds ---" % (time.time() - start_time))
