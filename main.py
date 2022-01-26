import textwrap
from io import BytesIO
from PIL import Image, ImageFont, ImageDraw
from util import getText, getImage
import requests

img = Image.open(BytesIO(requests.get(getImage()).content))
title_font = ImageFont.truetype('fonts/Laila/Laila-Bold.ttf', int(img.width/25))


title_text = textwrap.wrap(getText(), width=20)
print(title_text)
image_editable = ImageDraw.Draw(img)




for i,text in enumerate(title_text):
    w, h = image_editable.textsize(text, font=title_font)
    p_hor, p_ver = (img.width-w)/2, ((img.height-h)/3.5)+i*45
    # if i > 0:
    #     p_ver = (img.height-h)/i*i
    image_editable.text(
        (p_hor, p_ver),
        text,
        (237, 230, 211),
        stroke_width=10,
        stroke_fill="#000",
        font=title_font,
        align='center',
        textwrap=True
    );

print(img.width)
img.save("result.jpg")
