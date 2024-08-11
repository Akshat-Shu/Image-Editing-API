from flask import Flask, request, send_file
from Functions.resolve_image import resolve_image
from io import BytesIO
from Functions.resolve_functions import resolve_functions
from PIL import ImageFile, Image
import os

app = Flask(__name__)
no_base_image = "app.Flask." + __name__ + ".no_base_image"

@app.route("/")
def home():
    return "use the path /edit_image to start editing your images!"

@app.route('/edit_image')
def get_image():
    base_image_url: str = request.args.get("base_image", default=no_base_image)
    edited_image: ImageFile = None
    if(base_image_url == no_base_image):
        return "You did not provide a URL"


    #image resolution
    try:
        base_image = resolve_image(base_image_url)
        edited_image = base_image.copy()
        

    except Exception as e:
        print(e)
        return "You provided a bad URL for base_image. It could be that your Image Hosting Provider does not allow requests."

    # resolve image with all base image functions
    try:
        all_base_functions = resolve_functions(os.path.join(
            os.path.dirname(__file__), 'Base_Image_Editing'
        ))
        base_function_names = all_base_functions.keys()

        
        #TODO: Rather than looping all functions, use the keys for parameters
        # it would be quicker and would provide more functionality
        for name in base_function_names:
            parameter_value = request.args.get(name, default=None)
            if parameter_value:
                edited_image = all_base_functions[name](edited_image, parameter_value, request.args)
                if not isinstance(edited_image, Image.Image):
                    if isinstance(edited_image, str):
                        return edited_image 
                    else:
                        print(f"new type: {type(edited_image)}")
                        return "Please contact the developer regarding this issue"
                

    except Exception as e:
        print(e)
        return "You provided an invalid parameter or there was an Internal Error while editing your image"
    
    # return resolved image
    try:
        img_byte_arr = BytesIO()
        edited_image.save(img_byte_arr, format=base_image.format)
        img_byte_arr.seek(0)  # Move cursor back to the start of the buffer
        
        edited_image.close()
        print(base_image.filename)
        return send_file(img_byte_arr, as_attachment=False)
    except Exception as e:
        print(e)
        return "There was an error in presenting the image"






if __name__ == '__main__':
    app.run(debug=True)