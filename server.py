import cv2
import logging
from flask import Flask
# from sms import SendSMS
# from flask_apscheduler import APScheduler

from preprocessor import PlateDetector

from apscheduler.schedulers.background import BackgroundScheduler

# Setup logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)


app = Flask(__name__)
# app.config.from_object(Config())

# initialize scheduler
scheduler = BackgroundScheduler()
# scheduler.init_app(app)

# Initialize plate detector
plateDetect = PlateDetector(0.25)


# OpenCv video
capture = cv2.VideoCapture('./test_videos/vid3.mp4')


def detect_and_recognize_plate():
    # Add your plate detection and recognition code here
    # This function will be called every 5 seconds by the scheduler
    ret, frame = capture.read()
    # Process the frame to detect and recognize the plate
    # Print the plate number
    print(plateDetect.process_image(frame))

# @scheduler.task('interval', id='detect_plate', seconds=60, misfire_grace_time=900)
# def detect_plate():
#     success, frame = capture.read()
#     fps = capture.get(cv2.CAP_PROP_FPS)
#     logging.info(f"Taking a picture of video with, {fps} FPS")

#     if not success:
#         # Handle video capture error
#         logging.info("Error capturing video")
#         return
#         # return Response("Error capturing video", status=500)

#     # Perform any additional processing on the frame (e.g., add timestamp)
#     # Modify the frame variable here to add the current time or any other desired information
#     # if process_frame:
#     print(plateDetect.process_image(frame))

#     # Convert the frame to JPEG format
#     # ret, jpeg = cv2.imencode('.jpg', frame)


# def send_sms():
#     # Code to send SMS goes here
#     print("Sending SMS...")
#     # print env variables
#     # print_env()
#     # send sms
#     SendSMS().sending()


@app.route("/")
def index():
    return "Server is running"


if __name__ == '__main__':
    scheduler.add_job(detect_and_recognize_plate, 'interval', seconds=20)
    # start the main scheduler
    scheduler.start()
    app.run(debug=True)
