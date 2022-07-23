class Configuration(object):
    DEBUG = True
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SQLALCHEMY_DATABASE_URI = "mysql+mysqlconnector://root:admin@localhost/test2"
    SECRET_KEY = "something very secret"
