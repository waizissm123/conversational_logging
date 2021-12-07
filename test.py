import os
from datetime import datetime
import random

import requests
import mongo_management


# files = {'file': open(r"C:\Users\hamma\OneDrive\Documents\Sound recordings\Recording.wav", 'rb')}
# values = {"name": "hello", "format": ".wav"}
# r = requests.post("http://127.0.0.1:5000/api/file", files=files, data=values)
# print(r.text)

# r = requests.get("http://127.0.0.1:5000/api/get/all")
# print(r.te)
print(str(datetime.time(datetime.now())))
# print(str(datetime.date(datetime.now())))
# print(round(os.path.getsize("audio.wav")/1024))
list_city=["islamabad","dubai","peshawar","karachi"]
status=["good","offline"]
branch_code=12221111
CNIC=6110100000000
for x in range(151):
    base_data_list = {'Branch_code': branch_code+1,
                      'Branch': list_city[random.randint(0,3)],
                      'CNIC': CNIC+x,
                      'Audio_file_link': "https://coversational-logging.s3.amazonaws.com/2021-12-07%2005%3A01%3A22.609945.wav?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Credential=AKIAVDCNNPJRA7CCMZHF%2F20211207%2Feu-central-1%2Fs3%2Faws4_request&X-Amz-Date=20211207T000140Z&X-Amz-Expires=3600&X-Amz-SignedHeaders=host&X-Amz-Signature=03a9f49d15c8823843f824eb9d79cb8b0b2001f2106a5187c9863d7b121ef594",
                      'title': str(datetime.now()),
                      'Date': str(datetime.date(datetime.now())),
                      'time': str(datetime.time(datetime.now())),
                      'file_size': round(os.path.getsize("audio.wav") / 1024) + x,
                      'type': "wav",
                      'status': status[random.randint(0,1)]
                      }
    mongo_management.insert_into_db(base_data_list)


