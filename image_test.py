import cv2
import time
from preprocessor import PlateDetector

plateDetect = PlateDetector(0.25)

# cap = cv2.VideoCapture('./test_videos/vid3.mp4')
cap = cv2.imread("./test_videos/test_pic3.jpg")

plateDetect.process_image(cap)

cap = cv2.resize(cap, (700, 700))
cv2.imshow('frame', cap)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
