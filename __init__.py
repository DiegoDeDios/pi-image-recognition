#This script should initialize the service and set up the endpoints 

#Authors: Juan Damaso, Diego de Dios

import os
from flask import Flask
import sys;sys.path.append(r"/home/diegoama/vision_counter")
import pytools.api_instanciator as api_container


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
        image_path = r"./vision_counter/pytools/counter_images/1.jpeg"
        out = api.parse_image(image_path)
        return {os.path.basename(image_path) : out}

    return app