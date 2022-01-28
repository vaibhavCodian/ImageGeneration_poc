import datetime
import textwrap
from io import BytesIO
from random import randrange

import yaml
from PIL import Image, ImageDraw, ImageFont

from util import getText, getImage, getTextStyle, addWatermark
import requests

with open("../content.yml", 'r') as stream:
    data = yaml.safe_load(stream)

img = Image.open(BytesIO(requests.get(getImage()).content))
font = data["CONF"]['Fonts'][randrange(len(data["CONF"]['Fonts']))]
print(font)
title_font = ImageFont.truetype('../fonts/'+font+'/'+font+'-Bold.ttf', int(img.width/25))

style = getTextStyle()

title_text = textwrap.wrap(getText(), width=style["font_width"])
print(title_text)
image_editable = ImageDraw.Draw(img)

for i,text in enumerate(title_text):
    w, h = image_editable.textsize(text, font=title_font)
    p_hor, p_ver = (img.width-w)/2, ((img.height-h)/3.5)+i*55
    # if i > 0:
    #     p_ver = (img.height-h)/i*i
    image_editable.text(
        (p_hor, p_ver),
        text,
        (237, 230, 211),
        stroke_width=style['stroke_width'],
        stroke_fill=style['rand_color'],
        font=title_font,
        align='center',
        textwrap=True
    );

print(img.width)
addWatermark(img)
# img.save("../generated/GI_Repulic_%s.jpg"%datetime.datetime.now())
img.save("result.png")