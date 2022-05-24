import requests
from PIL import Image
from io import BytesIO

def resize(image, canva, orientation):

    sizes = {
            "Stories": (1080, 1920),
            "Feed Square": (1080, 1080),
            "Feed Landscape": (1920, 1080),
            "Feed Portrait": (1080, 1920)
    }

    canva = sizes[canva]

    response = requests.get(image)
    image = Image.open(BytesIO(response.content))
    
    width_ratio = canva[0] / image.size[0]
    height_ratio = canva[1] / image.size[1]

    size = None

    if width_ratio >= height_ratio:
        size = {
                "width": int(width_ratio * image.size[0]),
                "height": int(height_ratio * image.size[1])
        }

    elif width_ratio < height_ratio:
        size = {
                "width": int(height_ratio * image.size[0]),
                "height": int(height_ratio * image.size[1])
        }

    image = image.resize((size["width"], size["height"]))

    if image.size[0] == canva[0]:
        if orientation == "Top":
            left = 0
            top = 0
            right = canva[0]
            botton = canva[1]
        elif orientation == "Center":
            left = 0
            top = (image.size[1] - canva[1]) / 2
            right = canva[0]
            botton = image.size[1]
        elif orientation == "Botton":
            left = 0
            top = image.size[1] - canva[1]
            right = canva[0]
            botton = image.size[1]
    elif image.size[1] == canva[1]:
        if orientation == "Left":
            left = 0
            top = 0
            right = canva[0]
            botton = canva[1]
        elif orientation == "Center":
            left = (image.size[0] - canva[0]) / 2
            top = 0
            right = canva[0] + ((image.size[0] - canva[0]) / 2)
            botton = canva[1]
        elif orientation == "Right":
            left = (image.size[0] - canva[0]) / 2
            top = 0
            right = image.size[0]
            botton = canva.size[1]

    return image.crop((left, top, right, botton))
