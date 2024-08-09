import requests
from io import BytesIO
from PIL import Image

async def get_image(url):
    async with requests.get(url, stream=True) as r:
        base_image = await Image.open(BytesIO(r.content))