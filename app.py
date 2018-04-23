import os
import flask
from routes.routes import mainroutes
from models.dbconnect import Dbconnect

app_name = "Patient Records"
app = flask.Flask(app_name)
app.config.from_object('config.Config')
app.register_blueprint(mainroutes)