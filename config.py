class Config(object):
    ENVIRONMENT = 'Development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kitgiana@localhost/todo_app_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'

class Development(Config):
    ENVIRONMENT = 'Development'
    DEBUG = True
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kitgiana@localhost/todo_app_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'

class Testing (Config):
    ENVIRONMENT = 'Development'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kitgiana@localhost/todo_app_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'

class Production(Config):
    ENVIRONMENT = 'Development'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kitgiana@localhost/todo_app_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'
