import cv2
import time

from sms import SendSMS
from preprocessor import PlateDetector
from src.utils import compare

plateDetect = PlateDetector(0.25)

cap = cv2.VideoCapture('./test_videos/vid3.mp4')

# interval = 5 * 60  # Interval in seconds (5 minutes)
interval = 5
last_capture_time = time.time()

while cap.isOpened():
    success, frame = cap.read()
    # cap.set(cv2.CAP_PROP_FPS, 30)

    if success:
        frame = cv2.resize(frame, (840, 540))
        current_time = time.time()

        # Capture an image at the specified interval
        if current_time - last_capture_time >= interval:
            cv2.imshow('frame', frame)
            cv2.imwrite('captured_frame.jpg', frame)  # Save the captured frame
            last_capture_time = current_time
            thePlate = plateDetect.process_image(frame)
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

        # Display the resulting frame
        # cv2.imshow('frame', frame)

        # the 'q' button is set as the
        # quitting button you may use any
        # desired button of your choice
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break
    else:
        break

# After the loop release the cap object
cap.release()
# Destroy all the windows
cv2.destroyAllWindows()
