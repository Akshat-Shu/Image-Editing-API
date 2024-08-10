from PIL import ImageFile
from resolve_image import resolve_image

def overlay_image_url(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    overlay_image = None
    try:
        overlay_image = resolve_image(parameter_value)
    