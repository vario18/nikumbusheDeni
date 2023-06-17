import cv2
import yolov5
import easyocr


class PlateDetector:
    MODEL_PATH = "./model.pt"

    def __init__(self, conf=0.5) -> None:
        self.model = yolov5.load(self.MODEL_PATH)
        # set model parameters
        self.model.conf = conf  # NMS confidence threshold
        self.model.iou = 0.45  # NMS IoU threshold
        self.model.agnostic = False  # NMS class-agnostic
        self.model.multi_label = False  # NMS multiple labels per box
        self.model.max_det = 1000  # maximum number of detections per image

        # Language(s) for text recognition
        self.reader = easyocr.Reader(["en"])

    @classmethod
    def load_img(self, path):
        # if isinstance(path, cv2.Mat):
        # return path
        # cv2.resize(the_img, (120, 120))
        # return cv2.imread(path)
        return path

    def extract_text_from_image(self, image) -> list[str]:
        result = self.reader.readtext(image)
        texts = [entry[1] for entry in result]  # Extract text from result
        return texts

    def process_image(self, img_path: str):
        original_img = self.load_img(img_path)
        if original_img is None:
            print("The image file could not be read.")
            return
        results = self.model(original_img, augment=True)
        predictions = results.pred[0]
        # Get bounding box information
        car_plate_results = predictions[:, :4].tolist()
        if len(car_plate_results) == 0:
            print("No Plate number detected.")
            return
        for i in range(len(car_plate_results)):
            xmin, ymin, xmax, ymax = map(int, car_plate_results[i])
            cropped_image = cv2.cvtColor(
                original_img[ymin:ymax, xmin:xmax], cv2.COLOR_BGR2RGB)
            return self.extract_text_from_image(cropped_image)
