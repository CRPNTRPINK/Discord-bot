import yadisk
from config import SETTINGS
import random
from urllib.request import urlopen
import os
import time
import datetime

y = yadisk.YaDisk(id=SETTINGS['ID'], secret=SETTINGS['SECRET'], token=SETTINGS['TOKEN'])
random_box = list()


def get_files():
    x = y.get_files()
    for i in x:
        random_box.append(i['name'])
    return random_box


def get_random():
    file_random = random.choice(get_files())
    y.download(f'/webm/{file_random}', f'downloads/{file_random}')
    return f'downloads/{file_random}'
