import os
import datetime
downloaded_files = list()

def del_file():
    downloaded_files.extend(os.listdir('downloads'))
    for i in downloaded_files:
        os.remove(f"downloads/{i}")