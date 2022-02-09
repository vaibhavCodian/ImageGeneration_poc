import datetime
import os
import random
from io import BytesIO

import PIL.ImageEnhance
import requests
from PIL import Image, ImageEnhance
from PIL.ImageFilter import EDGE_ENHANCE
from dotenv import load_dotenv
from random import randrange
import yaml
import holidays
from pexels_api import API

load_dotenv()
api = API(os.getenv('pexel_api_key'))

img_watermark = Image.open('watermark1.png')

time = datetime.datetime.now().hour
timed = 'Night'
if time < 12:
    timed = "Morning"

elif 12 < time < 16:
    timed = "Afternoon"

# print(datetime.datetime.now().strftime("%d-%m-%Y") in in_holidays)

with open("content.yml", 'r') as stream:
    data = yaml.safe_load(stream)


def getData():
    return data


#

def getImage(genre, holiday=None):
    if genre == "HOLIDAY" and holiday is not None:
        search = "india "+holiday
    else:
        genre = data['genre'][randrange(len(data['genre']))]
        search = genre
        if genre == "TIMELY":
            search = timed
        else:
            search = genre

    print("[D] search: "+search)

    api.search(search, page=randrange(1, 10), results_per_page=10)

    photos = api.get_entries()
    url = photos[randrange(len(photos))].large
    img = Image.open(BytesIO(requests.get(url).content))
    img_size = randrange(min(img.width, img.height), 700)

    # OPTIMIZING IMAGE
    img.thumbnail((img_size, img_size), Image.ANTIALIAS)
    img = img.filter(EDGE_ENHANCE)
    img = ImageEnhance.Contrast(img).enhance(random.uniform(0, 0.8))
    return img

def getText(genre, holiday=None):
    print("genre: ",genre)
    if genre == 'TIMELY':
        texts = data['TEXT'][genre][timed]
    elif genre == 'HOLIDAY' and holiday is not None:
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
