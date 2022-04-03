from logging import DEBUG
from flask import config


OPENAI_API_KEY = "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"

class Config(object):
    DEBUG = True
    TESTING = False

class DevelopmentConfig(Config):
    SECRET_KEY = 'this-is-a-secret-key'


config = {
    'development': DevelopmentConfig,
    'testing': DevelopmentConfig,
    'production': DevelopmentConfig
}
