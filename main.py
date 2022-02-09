import textwrap
from datetime import datetime
from io import BytesIO
from random import randrange,choices
import yaml
from PIL import Image, ImageFont, ImageDraw
import holidays
from templates.template_0 import callTemplate
from templates.template_1 import callTemplate1

with open("content.yml", 'r') as stream:
    data = yaml.safe_load(stream)

def generateImages(quantity=10):
    # Getting If Holiday
    in_holidays = holidays.IN()
    holiday = in_holidays.get(datetime.now().strftime("%d-%m-%Y"))

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
    choices_list = choices(population=data['genre'], weights=weights, k=2) # k=2 for testing

    # if holiday:
    #     print("holiday for "+holiday)
    print("its is " + " of time of " + timed)

    for i, c in enumerate(choices_list):
        print(c)
        print(i)
        if i % 2:
            if c == 'HOLIDAY':
                callTemplate(c, holiday)
            callTemplate(c)
        else:
            if c == 'HOLIDAY':
                callTemplate1(c, holiday)
            callTemplate1(c)

            print(False)


generateImages()

