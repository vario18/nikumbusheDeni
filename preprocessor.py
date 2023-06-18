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

    # def is_number_or_letters(self, string):
    #     if string.isdigit():
    #         return "Number"
    #     elif string.isalpha():
    #         return "Letters"
    #     else:
    #         return "Mixed"

    # def good_plate_number(self, plate: list[str]):
    #     number = 0
    #     letters = ""
    #     if len(plate) == 1:
    #         newplate = plate[0].split(" ")
    #         self.good_plate_number(newplate)
    #     elif len(plate) == 2:
    #         for i in plate:
    #             print(i)
    #             if self.is_number_or_letters(i) == "Number":
    #                 number = i[-3:]
    #             elif self.is_number_or_letters(i) == "Letters":
    #                 letters = i[-3:]
    #             elif self.is_number_or_letters(i) == "Mixed":
    #                 number = i[-3:]
    #     theplate = [str(number), str(letters)]
    #     if len(theplate[0]) == 3 and len(theplate[1]) == 3:
    #         return theplate
    #     else:
    #         return None, f"got: {theplate}"

    def compare(self, plate):
        fetched_all_plates = [
            {"id": 1, "letters": "ABC", "numbers": "123"},
            {"id": 2, "letters": "DTP", "numbers": "152"},
            {"id": 3, "letters": "BDB", "numbers": "602"},
            {"id": 4, "letters": "CUL", "numbers": "245"},
            {"id": 5, "letters": "DTS", "numbers": "945"},
            {"id": 6, "letters": "DFH", "numbers": "405"},
            {"id": 7, "letters": "ALM", "numbers": "517"},
            {"id": 8, "letters": "DRN", "numbers": "468"},
            {"id": 9, "letters": "DBU", "numbers": "405"},
            {"id": 10, "letters": "AKE", "numbers": "393"},
            {"id": 11, "letters": "CBY", "numbers": "865"},
            {"id": 12, "letters": "SU", "numbers": "41396"},
            {"id": 13, "letters": "CYR", "numbers": "572"},
            {"id": 14, "letters": "DWW", "numbers": "280"},
            {"id": 15, "letters": "DUB", "numbers": "866"},
            {"id": 16, "letters": "DSQ", "numbers": "311"},
            {"id": 17, "letters": "DGC", "numbers": "785"},
            {"id": 18, "letters": "DRM", "numbers": "373"},
            {"id": 19, "letters": "CGE", "numbers": "374"},
            {"id": 20, "letters": "DJM", "numbers": "713"}
        ]
        # test_plate = ["CUL", "21245"]
        for item in fetched_all_plates:
            if self.present(item['letters'], plate):
                # print(f"{item['letters']} is present in {item['id']}")
                if self.present(item['numbers'], plate):
                    print(
                        f"Found {item['letters']} {item['numbers']} in {item['id']}")

    def present(self, item, thelst):
        for i in thelst:
            if item.lower() in i.lower():
                return True
        return False

    def extract_text_from_image(self, image) -> list[str]:
        result = self.reader.readtext(image)
        texts = [entry[1] for entry in result]  # Extract text from result
        self.compare(texts)
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
