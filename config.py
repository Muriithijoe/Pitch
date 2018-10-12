import os

class Config:
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://username:killshot18@joe/pitch'

class ProdConfig:
    pass

class DevConfig:
    DEBUG = True

config_options = {
'development':DevConfig,
'production':ProdConfig
}
