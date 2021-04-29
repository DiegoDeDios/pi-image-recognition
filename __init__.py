#This script should initialize the service and set up the endpoints 

#Authors: Juan Damaso, Diego de Dios

import os
from flask import Flask, flash, request
import pytools.api_instanciator as api_container
from PIL import Image

def create_app(test_config=None):
    # create and configure the app
    api = api_container.CloudAPI()
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # load the instance config, if it exists, when not testing
        app.config.from_pyfile('config.py', silent=True)
    else:
        # load the test config if passed in
        app.config.from_mapping(test_config)

    # ensure the instance folder exists
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    @app.route('/pytools')
    def return_image_raw_data():
        return "Test"
    
    @app.route('/image', methods=["POST"])
    def get_image():
        #img = Image.open(request.files['file'])
        try:
            out, error, override = api.parse_image_from_request(request)
            return {"counter_text":out, "_error_probability": "{:.2%}".format(error), "_overriden_string": override }
        except Exception as e:
            return "The image could not be parsed: %s\n"%(str(e))


    return app