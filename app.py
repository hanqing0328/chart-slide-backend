from flask import Flask
from flask import Response
from flask import stream_with_context
import os
from flask import send_from_directory
from flask_cors import CORS, cross_origin
from flask_csv import send_csv


app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.realpath(__file__))
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

@app.route("/getData/r<r_id>c<c_id>", methods=['GET'])
@cross_origin()
def hello_world(r_id, c_id):
    FILE_DIR = 'r%sc%sdata.json' %(r_id, c_id)
    FINAL_DIR = os.path.join(BASE_DIR, FILE_DIR)
    try: 
        # return send_csv(FINAL_DIR, "test.csv")
        return send_from_directory(BASE_DIR,FILE_DIR , mimetype='text/json')
    except Exception as e:
        return str(e)
    