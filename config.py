import os

class Config:
    DEBUG = os.environ.get('DEBUG')
    SECRET_KEY= os.environ.get('SECRET_KEY')
    
    
    


class TestConfig(Config):
    SQLALCHEMY_DATABASE_URI = 'postgresql+psycopg2://'

class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig,
'test':TestConfig
}