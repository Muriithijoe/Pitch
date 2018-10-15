import os

class Config:

    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:killshot18@joe/pitch'
    MAIL_SERVER = 'smtp.googlemail.com'
    MAIL_PORT = 587
    MAIL_USE_TLS = True
    MAIL_USERNAME = os.environ.get("MAIL_USERNAME")
    MAIL_PASSWORD = os.environ.get("MAIL_PASSWORD")
    #simple mde configurations
    SIMPLEMDE_JS_IIFE = True
    SIMPLEMDE_JS_CDN = True

class ProdConfig:
    pass

class DevConfig:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:killshot18@joe/pitch'

    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
