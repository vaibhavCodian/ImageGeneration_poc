import datetime
import textwrap
from io import BytesIO
from random import randrange

import yaml
from PIL import Image, ImageDraw, ImageFont

from util import getText, getImage, getTextStyle, addWatermark, getTimedText
import requests

with open("../content.yml", 'r') as stream:
    data = yaml.safe_load(stream)

img = Image.open(BytesIO(requests.get(getImage()).content))
img_size = randrange(min(img.width, img.height),700)
img.thumbnail((img_size, img_size), Image.ANTIALIAS)

font = data["CONF"]['Fonts'][randrange(len(data["CONF"]['Fonts']))]
print(font)
title_font = ImageFont.truetype('../fonts/'+font+'/'+font+'-Bold.ttf', int(img.width/25))
sub_title_font = ImageFont.truetype('../fonts/'+font+'/'+font+'-Bold.ttf', int(img.width/20))

style = getTextStyle()
style2 = getTextStyle()

title_texts = textwrap.wrap(getText(), width=style["font_width"])
sub_title_text = getTimedText()
print(title_texts)
image_editable = ImageDraw.Draw(img)

# adding title and sub title
for i, text in enumerate(title_texts):
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

    if i == len(title_texts)-1:
        print("HERE")
        # adding subtitle
        image_editable.text(
            (p_hor, p_ver+50),
            sub_title_text,
            (237, 230, 211),
            stroke_width=style2['stroke_width'],
            stroke_fill=style2['rand_color'],
            font=sub_title_font,
            align='center',
            textwrap=True
        );



# watermark_pos = img.width/3.4
# img_w = Image.open('../watermark1.png')
# img_w.thumbnail((watermark_pos, watermark_pos), Image.ANTIALIAS)
# img.paste(img_w, (int(img.width-watermark_pos*0.8), int(img.height-watermark_pos*0.5)), img_w)
addWatermark(img)

print((img.width, img.height))
# img.save("../generated/GI_Repulic_%s.jpg"%datetime.datetime.now())

img.save("result.png")
