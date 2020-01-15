class Config(object):
    ENVIRONMENT = 'Development'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kitgiana@localhost/todo_app_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'

class Development(Config):
    ENVIRONMENT = 'Development'
    
    SQLALCHEMY_DATABASE_URI = 'postgresql://postgres:kitgiana@localhost/todo_app_db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'

class Testing (Config):
    SQLALCHEMY_ECHO = False
    ENVIRONMENT = 'Production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://gnizztaxawguhu:3c7948a0a0da69cbf1a80d78d098389990b81d3f3da843d86916409e6a757d2e@ec2-174-129-255-106.compute-1.amazonaws.com:5432/demjoc3740hcae'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'

class Production(Config):
    SQLALCHEMY_ECHO = False
    ENVIRONMENT = 'Production'
    DEBUG = False
    SQLALCHEMY_DATABASE_URI = 'postgres://gnizztaxawguhu:3c7948a0a0da69cbf1a80d78d098389990b81d3f3da843d86916409e6a757d2e@ec2-174-129-255-106.compute-1.amazonaws.com:5432/demjoc3740hcae'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    SECRET_KEY = 'su93r-su93r-s3cr3t-qu1t3-h@r6-t0-h@ck-k1tg1@n@l1k3chr1st96040001'
