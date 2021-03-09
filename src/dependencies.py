from flask import session
from flask import Flask
from flask_injector import Module, request
from injector import Binder

from service.minesweeper import MineSweeperService, Session


class AppModule(Module):
    def __init__(self, app: Flask):
        super().__init__()
        self.app = app

    def configure(self, binder: Binder):
        binder.bind(MineSweeperService, to=MineSweeperService, scope=request)
        binder.bind(Session, to=lambda: session, scope=request)
