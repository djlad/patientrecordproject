import os
import flask
from routes.routes import mainroutes

app_name = "Patient Records"

app = flask.Flask(app_name)
app.config.update({
    'DATABASE':os.path.join(app.root_path, app_name+".db"),
    'SECRET_KEY':'development key',
    'USERNAME':'admin',
    'PASSWORD':'default'
})

app.register_blueprint(mainroutes)