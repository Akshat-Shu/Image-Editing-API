from flask import Flask, request
from resolve_image import resolve_image
import Base_Image_Editing as BIE

app = Flask(__name__)
no_base_image = "app.Flask." + __name__ + ".no_base_image"

@app.route("/")
def home():
    return "Home"

@app.route('/edit_image')
def get_image():
    base_image_url = request.args.get("base_image", default=no_base_image)
    if(base_image_url == no_base_image):
        return "You did not provide a URL"

    try:
        base_image = resolve_image(base_image_url)

        # return send_file(base_image)


        
    except Exception as e:
        print(e)
        return "You provided a bad URL for base_image. It could be that your Image Hosting Provider does not allow requests."


if __name__ == '__main__':
    app.run(debug=True)