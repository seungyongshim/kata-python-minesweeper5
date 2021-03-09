from flask import Flask, request
from flask_injector import FlaskInjector
from injector import Injector
from dependencies import AppModule
from service.minesweeper import MineSweeperService

app = Flask(__name__)
app.debug = True
app.secret_key = "ABCDEFG"


@app.route("/")
def index(service: MineSweeperService):
    return str(service)


@app.route("/click")
def click(service: MineSweeperService):
    x = int(request.args.get("x"))
    y = int(request.args.get("y"))
    service.click(x, y)
    return str(service)


FlaskInjector(app, injector=Injector([AppModule(app)]))