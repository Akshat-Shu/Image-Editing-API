import requests
from io import BytesIO
from PIL import Image

def resolve_image(url):
    with requests.get(url, stream=True) as r:
        return Image.open(BytesIO(r.content))