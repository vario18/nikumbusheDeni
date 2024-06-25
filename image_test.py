import cv2
from sms import SMSNotifier
from preprocessor import PlateDetector
from src.utils import find_car_by_plate

# initialize constants
dept = 0

# Initialize the plate detector
plate_detector = PlateDetector(0.25)

# Load the image from file
image = cv2.imread("./test_images/test-pic4.jpg")

# Process the image to detect the license plate
detected_plate = plate_detector.process_image(image)

# Check if a plate is detected
if detected_plate is not None:
    print("Detected plate:", detected_plate)

    # Find the car details based on the detected plate
    car = find_car_by_plate(detected_plate)

    # Check if the car is found in the database
    if car is not None:
        # Check if the car is owed more than 0
        if int(car.owed) > dept:
            # Send an SMS to the car owner
            SMSNotifier().send_sms(
                car.phoneNumber,
                car.carOwner,
                car.owed,
                f"T{car.plateNumber} {car.plateLetter}",
            )
        else:
            print(
                f"{car.carOwner}, owner of car ({car.plateNumber} {car.plateLetter}) is not owed."
            )
    else:
        print(f"{detected_plate} couldn't be found in the Database.")

# Resize the image for display
resized_image = cv2.resize(image, (700, 700))

# Show the image
cv2.imshow("frame", resized_image)

# Wait for user to press any key (to avoid Python kernel from crashing)
cv2.waitKey(0)

# Close all open windows
cv2.destroyAllWindows()
