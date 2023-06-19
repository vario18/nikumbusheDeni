from .model import Cars


def compare(plate: list[str]):
    fetched_all_plates = Cars.get_all()
    for item in fetched_all_plates:
        if present(item.plateLetter, plate):
            # print(f"{item['letters']} is present in {item['id']}")
            if present(item.plateNumber, plate):
                print(
                    f"Found {item.plateLetter} {item.plateNumber} in {item.id}")
                return Cars.get_by_id(item.id)


def present(item, thelst):
    for i in thelst:
        if item.lower() in i.lower():
            return True
    return False
