# Import the necessary libraries
import cv2  # OpenCV for video processing
import time  # For time-related operations
from sms import SMSNotifier  # Custom module for sending SMS notifications
from preprocessor import PlateDetector  # Custom module for license plate detection
from src.utils import find_car_by_plate  # Custom module for comparing license plates

# Initialize the plate detector
plate_detector = PlateDetector(0.25)

# Open the video file
cap = cv2.VideoCapture("./test_videos/vid5.mp4")

# Set the capture interval in seconds
interval = 4
dept = 0

# Initialize the last capture time
last_capture_time = time.time()

# Loop through the frames of the video
while cap.isOpened():
    # Read the next frame
    success, frame = cap.read()

    if success:
        # Resize the frame
        frame = cv2.resize(frame, (1080, 1920))
        current_time = time.time()

        # Capture an image at the specified interval
        if current_time - last_capture_time >= interval:
            cv2.imshow("frame", frame)
            cv2.imwrite("captured_frame.jpg", frame)  # Save the captured frame
            last_capture_time = current_time

            # Process the frame to detect the license plate
            detected_plate = plate_detector.process_image(frame)

            if detected_plate is not None:
                print(detected_plate)

                # Compare the detected plate with the database
                matched_car = find_car_by_plate(detected_plate)

                if matched_car is not None:
                    if int(matched_car.owed) > dept:
                        # Send SMS notification if the car owner is owed more than 5000 tshs
                        SMSNotifier().send_sms(
                            matched_car.phoneNumber,
                            matched_car.carOwner,
                            matched_car.owed,
                            f"T{matched_car.plateNumber} {matched_car.plateLetter}",
                        )
                    else:
                        print(
                            f"{matched_car.carOwner}, owner of car ({matched_car.plateNumber} {matched_car.plateLetter}) is not owed."
                        )
                else:
                    print(f"{detected_plate} couldn't be found in the Database.")

        # Exit the loop if 'q' is pressed
        if cv2.waitKey(1) & 0xFF == ord("q"):
            break
    else:
        break

# Release the video capture object
cap.release()

# Close all the windows
cv2.destroyAllWindows()
