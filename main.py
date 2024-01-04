import cv2
import cvzone
import pickle
import numpy as np

cap = cv2.VideoCapture('parking.mp4')

width, height = 41, 23


with open('carpositions', 'rb') as f:
    poslist = pickle.load(f)


def checkspace(imgpro):
    spacecount = 0
    for pos in poslist:
        x, y = pos

        crop = imgpro[y:y+height, x:x+width]
        #cv2.imshow(str(x+y),crop)

        count = cv2.countNonZero(crop)
        cvzone.putTextRect(img, str(count), (x,y+height-10), scale = 0.5, thickness=1,offset=1,colorR=(0,0,255))

        if count <370:
            color = (0,255,0)
            thickness = 3
            spacecount +=1
        else:
            color = (0,0,255)
            thickness = 2

        cv2.rectangle(img, pos, (pos[0] + width, pos[1] + height), color, thickness=thickness)
    cvzone.putTextRect(img, f'free places are: {spacecount} from {len(poslist)} places ', (100,50), scale = 2, thickness=3,offset=10,colorR=(0,240,0))

while True:
    if cap.get(cv2.CAP_PROP_POS_FRAMES) == cap.get(cv2.CAP_PROP_FRAME_COUNT):
        cap.set(cv2.CAP_PROP_POS_FRAMES, 0)

    _, img = cap.read()
    imggray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
    imgblur = cv2.GaussianBlur(imggray, (3,3), 1)
    imgthresh = cv2.adaptiveThreshold(imgblur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY_INV, 25, 10)
    imgmedian = cv2.medianBlur(imgthresh,5)
    kernel = np.ones((3,3),np.uint8)
    imgdilate = cv2.dilate(imgmedian,kernel=kernel,iterations=2)
    checkspace(imgdilate)

    cv2.imshow("Parking Cam",img)
    #cv2.imshow("Videoblur", imgblur)
    #cv2.imshow("Videothresh", imgthresh)
    #cv2.imshow("Videomedian", imgmedian)
    #cv2.imshow("Videoodilate", imgdilate)

    key = cv2.waitKey(10)
    if key == ord('q'):  # Press 'q' to exit
        break