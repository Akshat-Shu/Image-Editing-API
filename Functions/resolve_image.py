import requests
from io import BytesIO
from PIL import Image

def resolve_image(url: str):
    with requests.get(url, stream=True) as r:
        r.raise_for_status()
        return Image.open(BytesIO(r.content)).convert("RGBA") #Alpha channel required for transparency