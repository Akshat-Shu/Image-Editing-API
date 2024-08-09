from flask import Flask, request, send_file

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
        base_image = get_image(base_image_url)



        return send_file(base_image)


        
    except Exception as e:
        print(e)
        return "You provided a bad URL or did not provide one for base_image, try uploading the base image on imgur"


if __name__ == '__main__':
    app.run(debug=True)