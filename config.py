import os
from decouple import config


class Config(object):
    DEBUG = True

    basedir = os.path.abspath(os.path.dirname(__file__))

    SECRET_KEY = config('SECRET_KEY', default='Secrettt')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config('DB_ENGINE', default='mysql'),
        config('DB_USERNAME', default='root'),
        config('DB_PASS', default='root'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=3306),
        config('DB_NAME', default='flask-face')
    )


class ProductionConfig(Config):
    DEBUG = False

    # Security
    SESSION_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_HTTPONLY = True
    REMEMBER_COOKIE_DURATION = 3600

    # PostgreSQL database
    SQLALCHEMY_DATABASE_URI = '{}://{}:{}@{}:{}/{}'.format(
        config('DB_ENGINE', default='mysql'),
        config('DB_USERNAME', default='root'),
        config('DB_PASS', default='root'),
        config('DB_HOST', default='localhost'),
        config('DB_PORT', default=3306),
        config('DB_NAME', default='my_project')
    )
    SQLALCHEMY_TRACK_MODIFICATIONS = False


class DebugConfig(Config):
    DEBUG = True


# Load all possible configurations
config_dict = {
    'Production': ProductionConfig,
    'Debug': DebugConfig
}
