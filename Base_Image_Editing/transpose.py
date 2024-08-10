from PIL import ImageFile, Image


def transpose(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    transpose_options_dict = {
        'mirror': Image.Transpose.FLIP_LEFT_RIGHT,
        'bottom_mirror': Image.Transpose.FLIP_TOP_BOTTOM,
        'rotate_180': Image.Transpose.ROTATE_180,
        'rotate_90': Image.Transpose.ROTATE_90,
        'rotate_270': Image.Transpose.ROTATE_270,
        'transpose': Image.Transpose.TRANSPOSE,
        'transverse': Image.Transpose.TRANSVERSE
    }
    transpose_option = transpose_options_dict.get(parameter_value, None)
    if transpose_option != None:
        image = image.transpose(transpose_option)
        return image
    else:
        return "You did not provide a valid transpose option"