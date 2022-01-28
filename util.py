import datetime
import os

from PIL import Image
from dotenv import load_dotenv
from random import randrange
import yaml
import holidays
from pexels_api import API

load_dotenv()
api = API(os.getenv('pexel_api_key'))
in_holidays = holidays.IN()
holiday = in_holidays.get(datetime.datetime.now().strftime("%d-%m-%Y"))

img_watermark = Image.open('../watermark1.png')

time = datetime.datetime.now().hour
timed = 'Night'
if time < 12:
    timed = "Morning"

elif 12 < time < 16:
    timed = "Afternoon"

# print(datetime.datetime.now().strftime("%d-%m-%Y") in in_holidays)

with open("../content.yml", 'r') as stream:
    data = yaml.safe_load(stream)

if holiday:
    search = "india "+holiday
    genre = 'HOLIDAY'
else:
    genre = data['genre'][randrange(len(data['genre']))]
    search = genre
    if genre == "TIMELY":
        search = timed

    # if genre == "HOLIDAY":
    #     search = holiday_name


def getImage():
    api.search(search, page=randrange(1, 10), results_per_page=10)
    print(search)
    photos = api.get_entries()
    return photos[randrange(len(photos))].large


def getText():
    print("genre: "+genre)
    if genre == 'TIMELY':
        texts = data['TEXT'][genre][timed]
    elif genre == 'HOLIDAY':
        texts = data['TEXT']['HOLIDAY']
        return texts[randrange(len(texts))] % holiday
    else:
        texts = data['TEXT']["QUOTES"]

    return texts[randrange(len(texts))]


def getTimedText():
    texts = data['TEXT']['TIMELY'][timed]
    return texts[randrange(len(texts))]


def addWatermark(img: Image):
    watermark_pos = img.width / 3.4
    img_watermark.thumbnail((watermark_pos, watermark_pos), Image.ANTIALIAS)
    img.paste(img_watermark, (int(img.width - watermark_pos * 0.8), int(img.height - watermark_pos * 0.5)), img_watermark)
    return img

def getTextStyle():
    return {
        "rand_color": data["CONF"]['Colors'][randrange(len(data["CONF"]['Colors']))],
        "stroke_width": randrange(1,5),
        "font_width": randrange(25, 55)
    }
