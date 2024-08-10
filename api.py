from flask import Flask, request, send_file
from resolve_image import resolve_image
import Base_Image_Editing as BIE
from io import BytesIO
from resolve_functions import resolve_functions

app = Flask(__name__)
no_base_image = "app.Flask." + __name__ + ".no_base_image"

@app.route("/")
def home():
    return "use the path /edit_image to start editing your images!"

@app.route('/edit_image')
def get_image():
    base_image_url = request.args.get("base_image", default=no_base_image)
    if(base_image_url == no_base_image):
        return "You did not provide a URL"

    try:
        base_image = resolve_image(base_image_url)
        #TODO: do whatever edits required

        all_base_functions = resolve_functions('./Base_Image_editing')
        base_function_names = all_base_functions.keys()

        for name in base_function_names:
            parameter_value = request.args.get(name, default=None)
            if parameter_value:
                all_base_functions[name](base_image, parameter_value, request.args)


        img_byte_arr = BytesIO()
        base_image.save(img_byte_arr, format='JPEG')
        img_byte_arr.seek(0)  # Move cursor back to the start of the buffer
        
        return send_file(img_byte_arr, mimetype='image/jpeg', as_attachment=False)



        
    except Exception as e:
        print(e)
        return "You provided a bad URL for base_image. It could be that your Image Hosting Provider does not allow requests."


if __name__ == '__main__':
    app.run(debug=True)