from flask import Flask
from os import urandom

app = Flask(__name__)
app.config["SECRET_KEY"] = urandom(32).hex() #hex code with 256bits

from views import *

if __name__ == '__main__':
    app.run(debug = True)