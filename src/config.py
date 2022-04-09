from distutils.command.config import config


class Config:
    SECRET_KEY = 'llaveSecreta'


class DevelopmentConfig(Config):
    DEBUG = True
    MYSQL_HOST = 'localhost'
    MYSQL_USER = 'root'
    MYSQL_PASSWORD = ''
    MYSQL_DB = 'flask_login'
    
    
config = {
    'development': DevelopmentConfig
}