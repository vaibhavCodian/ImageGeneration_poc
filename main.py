import textwrap
from datetime import datetime
from io import BytesIO
from random import randrange,choices
import yaml
from PIL import Image, ImageFont, ImageDraw
import holidays
from util import getText, getImage
import requests

# img = Image.open(BytesIO(requests.get(getImage()).content))
# title_font = ImageFont.truetype('fonts/Laila/Laila-Bold.ttf', int(img.width/25))
# title_text = textwrap.wrap(getText(), width=20)
# print(title_text)
# image_editable = ImageDraw.Draw(img)

with open("content.yml", 'r') as stream:
    data = yaml.safe_load(stream)

def generateImages(quantity=10):
    # Getting If Holiday
    in_holidays = holidays.IN()
    holiday = in_holidays.get(datetime.now().strftime("26-%m-%Y"))

    # Getting Time of the day
    time = datetime.now().hour
    timed = 'Night'
    if time < 12:
        timed = "Morning"
    elif 12 < time < 18:
        timed = "Afternoon"

    weights = [0.2]*(len(data["genre"])-1)+[0]
    if holiday:
        weights = [0.2]*(len(data["genre"])-1)+[2]

    print(weights)
    c = choices(population=data['genre'], weights=weights, k=10)


    print(c)
    # if holiday:
    #     print("holiday for "+holiday)
    print("its is " + " of time of "+ timed)
    #
    # with open("content.yml", 'r') as stream:
    #     data = yaml.safe_load(stream)
    #
    # if holiday:
    #     search = holiday
    #     genre = 'HOLIDAY'
    # else:
    #     genre = data['genre'][randrange(len(data['genre']))]
    #     search = genre
    #     if genre == "TIMELY":
    #         search = timed

generateImages()

