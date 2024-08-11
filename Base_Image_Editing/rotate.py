from PIL import ImageFile, Image
from Functions.hex_to_float import hex_to_float


def rotate(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    rotate_angle = None
    rotate_color = None
    rotate_expand = None
    try:
        rotate_angle = float(parameter_value)
        rotate_color = hex_to_float(request_args.get("rotate_background_color", "0"))
        rotate_expand = request_args.get("rotate_expand", "") in [
            'True', 'true', 'Yes', 'yes'
            'T', 't', 'y', 'Y'
        ]
    except Exception as e:
        print(e)
        return "Values provided for rotate parameters could not be resolved"
    
    image = image.rotate(rotate_angle, expand=rotate_expand, fillcolor=rotate_color)
    return image
    