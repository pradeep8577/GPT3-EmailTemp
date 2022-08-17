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
