import os
from flask import Flask, request
from telapi import rest

app = Flask(__name__)

@app.route('/')
def hello():
    return 'This shud hopefully work!!!!!'



if __name__ == '__main__':
    app.run()