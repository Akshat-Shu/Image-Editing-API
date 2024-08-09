from flask import Flask, request, jsonify, send_file
from PIL import Image
import requests
import urllib.request
from io import BytesIO

app = Flask(__name__)
no_base_image = "app.Flask." + __name__ + ".no_base_image"

@app.route("/")
def home():
    return "Home"

@app.route('/edit_image')
def get_image():
    base_image = request.args.get("base_image", default=no_base_image)
    print(base_image)
    try:
        r = requests.get(base_image, stream=True)
        aux_im = Image.open(BytesIO(r.content))
        aux_im.show()
    except Exception as e:
        print(e)
        return "You provided a bad URL or did not provide one for base_image, try uploading the base image on imgur"


if __name__ == '__main__':
    app.run(debug=True)