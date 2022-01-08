from flask import Response
import sys
sys.path.append('..')
from application import app
from conf import conf


@app.route("/")
def hello_world():
    return f"<p>Hello, World!</p><p>{conf.output1}</p>", 201


@app.route("/home")
def home():
    return Response(f"Home Page<p>{conf.output2}</p>", status=202, mimetype="application/json")


@app.route(f"/{conf.url1}")
def custom_url():
    return f"<p>Given environment variables are expected to be seen</p><p>{conf.output1}</p><p>{conf.output2}</p>", 201

