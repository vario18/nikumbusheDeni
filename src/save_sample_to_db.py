import json
from .model import Cars, engine

from sqlmodel import Session


def save_questions_to_database(json_file_path: str):
    with open(json_file_path, "r") as f:
        cars = json.load(f)

    print(cars[0])

    with Session(engine) as session:
        i = 1
        for car_data in cars:
            car = Cars(**car_data)
            print("Saved car: ", i)
            i += 1
            session.add(car)
        session.commit()
        print("Saved all cars")


json_file_path = "sampleCars.json"

save_questions_to_database(json_file_path)
