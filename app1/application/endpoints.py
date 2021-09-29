from flask import Response
import sys
sys.path.append('..')
from application import app


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>", 201


@app.route("/home")
def home():
    return Response("Home Page", status=202, mimetype="application/json")
