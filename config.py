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
