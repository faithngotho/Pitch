
import os
class Config:
    SQLALCHEMY_TRACK_MODIFICATIONS = True
    SECRET_KEY = os.environ.get('SECRET_KEY') 
    WTF_CSRF_SECRET_KEY="a csrf secret key"
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://faith:34816809@localhost/pitch'


class ProdConfig(Config):
  SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")


class DevConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://faith:34816809@localhost/pitch'
    DEBUG = True
class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://faith:34816809@localhost/pitch'
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}