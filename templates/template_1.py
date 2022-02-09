import datetime
import textwrap
from random import randrange

from PIL import Image, ImageDraw, ImageFont

from util import getText, getImage, getTextStyle, addWatermark, getTimedText, getData


def callTemplate1(genre, holiday=None):
    img = getImage(genre, holiday)
    data = getData()

    font = data["CONF"]['Fonts'][randrange(len(data["CONF"]['Fonts']))]
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
        h = h/0.8
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


    addWatermark(img)

    print((img.width, img.height))
    img.save("../generated/GI_%s.jpg"%datetime.datetime.now())
