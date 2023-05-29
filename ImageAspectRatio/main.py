# Enunciado: Crea un programa que se encargue de calcular el aspect ratio de una imagen a partir de una url.
# - Url de ejemplo: https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png

import requests
from PIL import Image
from io import BytesIO

res = requests.get("https://raw.githubusercontent.com/mouredev/mouredev/master/mouredev_github_profile.png")
img = Image.open(BytesIO(res.content))
width, height = img.size
aspect_ratio = width / height

print("The aspect ratio of the image is: {}".format(aspect_ratio))