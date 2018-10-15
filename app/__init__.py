from flask import Flask
from flask_bootstrap import Bootstrap
from config import config_options
from flask_sqlalchemy import SQLAlchemy
from flask_uploads import UploadSet,configure_uploads,IMAGES 

bootstrap = Bootstrap()
db = SQLAlchemy()
photos = UploadSet('photos',IMAGES)
def create_app(config_name):

    app = Flask(__name__)

    #creating the app configurations
    app.config.from_object(config_options[config_name])

    #initializing flask extensions
    bootstrap.init_app(app)

    #registering the blueprint
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    #will add views and forms

    return app
