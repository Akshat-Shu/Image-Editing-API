from PIL import ImageFile
from Functions.resolve_image import resolve_image

def overlay_image_url(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    overlay_image = None
    overlay_image_y = int(request_args.get("overlay_image_y", default="0"))
    overlay_image_x = int(request_args.get("overlay_image_x", default="0"))

    # resolve overlay image
    try:
        overlay_image = resolve_image(parameter_value)

    except Exception as e:
        print(e)
        return "Unable to resolve your overlay image, you provided a bad URL"
    
    # paste overlay_image
    image.paste(overlay_image, (overlay_image_x, overlay_image_y), mask=overlay_image)
    
    return image