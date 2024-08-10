from PIL import ImageFile


def width(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    image = image.resize((int(parameter_value), image.height))
    return image
    