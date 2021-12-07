from datetime import datetime
import os

import cv2
import flask
from flask import request, jsonify
from flask_cors import CORS
import s3_management as s3m
import mongo_management as mdb

app = flask.Flask(__name__)
app.config["DEBUG"] = True
CORS(app)


@app.route('/api/file', methods=['POST'])
def post_file():
    if request.method == 'POST':
        f = request.files['file']
        f.save("audio.wav")
        f.flush()
        f.close()
        aws_name = s3m.aws_upload("audio.wav")
        link = s3m.aws_get_file_url(aws_name)
        base_data_list = {'Branch_code': 12345566,
                          'Branch': "karachi",
                          'CNIC': 6111111111111,
                          'Audio_file_link': link,
                          'title':str(datetime.now()),
                          'Date': str(datetime.date(datetime.now())),
                          'time':str(datetime.time(datetime.now())),
                          'file_size':round(os.path.getsize("audio.wav")/1024),
                          'type':"wav",
                          'status':"good"
                          }
        mdb.insert_into_db(base_data_list)
        return "Data Inserted"
    return "not a correct method"


@app.route('/api/get/all', methods=['GET'])
def get_all():
    # query to fetch data from mongodb
    return jsonify(mdb.get_all_data())


app.run()
