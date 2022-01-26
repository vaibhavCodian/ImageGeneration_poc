import datetime
import os
from dotenv import load_dotenv
from random import randrange
import yaml
import holidays
from pexels_api import API

load_dotenv()
api = API(os.getenv('pexel_api_key'))
in_holidays = holidays.IN()
holiday = in_holidays.get(datetime.datetime.now().strftime("%d-%m-%Y"))

time = datetime.datetime.now().hour
timed = 'Night'
if time < 12:
    timed = "Morning"

elif 12 < time < 16:
    timed = "Afternoon"

# print(datetime.datetime.now().strftime("%d-%m-%Y") in in_holidays)

with open("content.yml", 'r') as stream:
    data = yaml.safe_load(stream)

if holiday:
    search = holiday
    genre = 'HOLIDAY'
else:
    genre = data['genre'][randrange(len(data['genre']))]
    search = genre
    if genre == "TIMELY":
        search = timed


def getImage():
    api.search(search, page=randrange(1, 10), results_per_page=5)
    print(search)
    photos = api.get_entries()
    return photos[randrange(len(photos))].large


def getText():
    time = datetime.datetime.now().hour

    if genre == ['TIMELY']:
        texts = data['TEXT'][genre][timed]
    else:
        texts = data['TEXT']["QUOTES"]
    return texts[randrange(len(texts))]
