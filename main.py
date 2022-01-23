from PIL import  Image, ImageFont, ImageDraw

img = Image.open("images/nature11.jpg")
title_font = ImageFont.truetype('fonts/Laila/Laila-Bold.ttf', int(img.width/8.9))
title_text = "गुड मॉर्निंग"
image_editable = ImageDraw.Draw(img)

w, h = image_editable.textsize(title_text, font=title_font,)

image_editable.text(
    ((img.width-w)/2, (img.height-h)/2),
    title_text,
    (237, 230, 211),
    stroke_width=2,
    stroke_fill="#000",
    font=title_font,
    align='center'
);

print(img.width)
img.save("result.jpg")
