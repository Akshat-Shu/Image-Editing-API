from PIL import ImageFile
from Functions.resolve_image import resolve_image


def integer_if_exists(i: int, list_params: list[str], default_value: int|None):
    return int(list_params[i]) if i < len(list_params) else default_value

def overlay_image_url(image: ImageFile, parameter_value: str, request_args: dict[str, str]):
    overlay_image_urls = request_args.getlist("overlay_image_url")
    overlay_image_ys = request_args.getlist("overlay_image_y")
    overlay_image_xs = request_args.getlist("overlay_image_x")
    overlay_image_widths = request_args.getlist("overlay_image_width")
    overlay_image_heights = request_args.getlist("overlay_image_height")
    # overlay_image_width = int(request_args)

    for i in range(len(overlay_image_urls)):
        overlay_image = None
        overlay_image_url = overlay_image_urls[i]
        overlay_image_y = integer_if_exists(i, overlay_image_ys, 0)
        overlay_image_x = integer_if_exists(i, overlay_image_xs, 0)
        overlay_image_width = integer_if_exists(i, overlay_image_widths, None)
        overlay_image_height = integer_if_exists(i, overlay_image_heights, None)
        print(overlay_image_height, overlay_image_width)

        print()
        
        #resolve overlay images
        try:
            overlay_image = resolve_image(overlay_image_url)
        except Exception as e:
            print(e)
            return "Unable to resolve your overlay image, you provided a bad URL"
        

        if(overlay_image_height and overlay_image_width):
            overlay_image = overlay_image.resize((overlay_image_width, overlay_image_height))
        elif(overlay_image_width):
            overlay_image = overlay_image.resize((overlay_image_width, overlay_image.height))
        elif(overlay_image_height):
            overlay_image = overlay_image.resize((overlay_image.width, overlay_image_height))

        #paste overlay images
        image.paste(overlay_image, (overlay_image_x, overlay_image_y), overlay_image)

    

    # resolve overlay image

    
    # paste overlay_image
    
    
    return image