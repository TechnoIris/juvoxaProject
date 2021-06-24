import os
basedir = os.path.abspath(os.path.dirname(__file__))


class Config(object):
    DEBUG = False
    TESTING = False
    CSRF_ENABLED = True
    SECRET_KEY = 'something'
    # os.getenv("SECRET_KEY", "this-is-the-default-key")
    SQLALCHEMY_DATABASE_URI = os.environ['DATABASE_URL']


    # @property
    # def DATABASE_URI(self):  # Note: all caps
    #     return f"postgresql:///hospital"
    #     # return f"mysql://user@{self.DB_SERVER}/foo"


class ProductionConfig(Config):
    DEBUG = False


class StagingConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class DevelopmentConfig(Config):
    DEVELOPMENT = True
    DEBUG = True


class TestingConfig(Config):
    TESTING = True
