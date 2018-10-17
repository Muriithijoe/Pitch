import os

class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS= False
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:killshot18@joe/pitch'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USE_SSL = False
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    print(MAIL_USERNAME)
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")

    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_JS_CDN = True
    SECRET_KEY=os.environ.get("SECRET_KEY")

class TestConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:killshot18@joe/pitch'

class ProdConfig:
    pass

class DevConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://joe:killshot18@localhost/pitch'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig,
'testconfig':TestConfig
}
