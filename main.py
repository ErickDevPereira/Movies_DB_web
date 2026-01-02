from flask import Flask
from os import urandom
import db.DDL as ddl
import utils.IOops as IO

app = Flask(__name__)
app.config["SECRET_KEY"] = urandom(32).hex() #hex code with 256bits

from views import *

if __name__ == '__main__':
    try: #Catch username and password for the database. If the DB doesn't exist, a new one is created, otherwise, nothing special happen.
        username: str = input('Username for mySQL account on the server (write "root" if you didn\'t define it on the server) >>  ')
        password: str = input('Password for mySQL account on the server >>  ')
        ddl.run_database(username = username, password = password)
        IO.load_src_db(username, password)
    except Exception as err: #If the username or password don't match the expectation, the server won't run.
        print(err)
    else:
        #use_reloader as False won't let this code runs twice, but we loose the real time visibility for changes on the server.
        app.run(debug = True, use_reloader = False) #If everything is ok, the server will run.
    finally:
        IO.del_src_db()