import os
from flask import Flask, jsonify
from flask_restx import Resource, Api
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

db = SQLAlchemy()


def create_app(script_info=None):
    app = Flask(__name__)
    CORS(app)
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    db.init_app(app)

    # from project.api.ping import ping_blueprint
    # app.register_blueprint(ping_blueprint)

    from project.api import api
    api.init_app(app)

    # from project.api.athletes.views import athletes_blueprint
    # app.register_blueprint(athletes_blueprint)

    # shell conext for cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app


# S.NO,Name,Nationality,Current Rank,Previous Year Rank,Sport,Year,earnings ($ million)