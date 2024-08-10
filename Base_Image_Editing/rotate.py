from PIL import ImageFile, Image


def rotate(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    rotate_angle = float(parameter_value)