from PIL import  Image, ImageFont, ImageDraw

img = Image.open("images/nature1.jpg")
title_font = ImageFont.truetype('fonts/Laila/Laila-Bold.ttf', int(img.width/15.9), textwrap=True)
title_text = "शुभ दोपहर"

sub_title_font = ImageFont.truetype('fonts/Laila/Laila-Bold.ttf', int(img.width/25.5), textwrap=True)
sub_title_text = "बोहोत बोहोत गुड आफ्टरनून जी "
image_editable = ImageDraw.Draw(img)

w, h = image_editable.textsize(title_text, font=title_font)
image_editable.text(
    ((img.width-w)/4, (img.height-h)/2),
    title_text,
    (237, 230, 211),
    stroke_width=20,
    stroke_fill="#000",
    font=title_font,
    align='center',
    textwrap=True
);

w, h = image_editable.textsize(title_text, font=title_font)
image_editable.text(
    ((img.width-w)/4, (img.height-h)/1.34),
    sub_title_text,
    (237, 230, 211),
    stroke_width=20,
    stroke_fill="#000",
    font=sub_title_font,
    align='center'
);

img.save("result.jpg")
