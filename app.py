from flask import Flask, request
import logging

logging.basicConfig(filename='client_data.log', level=logging.DEBUG)

app = Flask(__name__)

@app.route("/")
def hello_world():
    logging.info("Requester ip: " + request.remote_addr)
    return "<p>Hello, World!</p>"