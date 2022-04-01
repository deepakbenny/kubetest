from flask import Flask
import os
app = Flask(__name__)
region_name = os.environ['REGION']

# configure default region
if region_name is None:
    region_name = "World"

@app.route('/')
def hello_world():
    return 'Bye, ' + region_name