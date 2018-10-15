import os

class Config:
    export MAIL_USERNAME=joeace2000@gmail.com
    export MAIL_PASSWORD=killshot18
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:killshot18@joe/pitch'

class ProdConfig:
    pass

class DevConfig:
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
