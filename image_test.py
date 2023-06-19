import cv2

from sms import SendSMS
from src.utils import compare
from preprocessor import PlateDetector

plateDetect = PlateDetector(0.25)

# cap = cv2.VideoCapture('./test_videos/vid3.mp4')
cap = cv2.imread("./test_videos/test_pic3.jpg")

thePlate = plateDetect.process_image(cap)
if thePlate is not None:
    theCar = compare(thePlate)
    if theCar is not None:
        if int(theCar.owed) > 5000:
            SendSMS().send(theCar.phoneNumber, theCar.owed)
        else:
            print(
                f"{theCar.carOwner}, owner of car ({theCar.plateNumber} {theCar.plateLetter}) is not owed.")
    else:
        print(f"{thePlate} couldn't be found in the Database.")

cap = cv2.resize(cap, (700, 700))
cv2.imshow('frame', cap)

# waits for user to press any key
# (this is necessary to avoid Python kernel form crashing)
cv2.waitKey(0)

# closing all open windows
cv2.destroyAllWindows()
