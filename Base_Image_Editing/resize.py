from PIL import ImageFile


def width(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    image = image.resize((int(parameter_value), image.height))
    return image
    

def height(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    image = image.resize((image.width, int(parameter_value)))
    return image

def scale(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    image = image.sca