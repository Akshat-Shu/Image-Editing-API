from PIL import ImageFile


def crop_left(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    crop_left_parameter = int(request_args.get('crop_left', default="0"))

    if crop_left:
        image = image.crop((crop_left_parameter, 0, image.width, image.height))
    return image
    
def crop_top(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    crop_top_parameter = int(request_args.get('crop_top', default="0"))

    if crop_top:
        image = image.crop((0, crop_top_parameter, image.width, image.height))
    return image
    
def crop_right(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    crop_right_parameter = int(request_args.get('crop_right', default="0"))

    if crop_right:
        image = image.crop((0, 0, image.width - crop_right_parameter, image.height))
    return image
    
def crop_bottom(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    crop_bottom_parameter = int(request_args.get('crop_bottom', default="0"))

    if crop_left:
        image = image.crop((0, 0, image.width, image.height - crop_bottom_parameter))
    return image
    