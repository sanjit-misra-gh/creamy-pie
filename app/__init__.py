from flask import Flask
from .extensions import bootstrap
from .routes.controller import controller

def create_app():
    app = Flask(__name__)
    bootstrap.init_app(app)

    app.register_blueprint(controller)

    return app
