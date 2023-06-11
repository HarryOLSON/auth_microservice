import os

DEBUG = False

JWT_SECRET = os.environ.get('JWT_SECRET')

DBCreds = {
    'HOST': os.environ.get('HOST', 'localhost'),
    'USER': os.environ.get('USER', 'root'),
    'PORT': os.environ.get('PORT', '3306'),
    'PASSWORD': os.environ.get('PASSWORD', '123')
}

