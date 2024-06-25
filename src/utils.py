from .model import Cars


def find_car_by_plate(plate: list[str]):
    # Fetch all cars from the database
    all_cars = Cars.get_all()

    # Iterate through each car
    for car in all_cars:
        # Check if both plate letter and plate number are present in the given plate list
        if is_plate_present(car.plateLetter, plate) and is_plate_present(
            car.plateNumber, plate
        ):
            # Print the found car details and return the car object
            print(
                f"Found car with plate: {car.plateLetter} {car.plateNumber} (ID: {car.id})"
            )
            return Cars.get_by_id(car.id)

    # If no car is found, return None
    return None


def is_plate_present(item, plate_list):
    # Iterate through each item in the plate list
    for plate_item in plate_list:
        # Check if the item (plate letter or plate number) is present in the plate item
        if item.lower() in plate_item.lower():
            return True

    # If the item is not present in any of the plate items, return False
    return False
