import os, sys, inspect

# cmd_subfolder = os.path.realpath(os.path.abspath(os.path.join(os.path.split(inspect.getfile( inspect.currentframe() ))[0],"telapi-python-master")))
# if cmd_subfolder not in sys.path:
# 	sys.path.insert(0, cmd_subfolder)

from flask import Flask
from telapi import rest

print 'hello'

app = Flask(__name__)

@app.route('/')
def hello():
    return 'This shud hopefully work!!!!!'



if __name__ == '__main__':
    app.run()