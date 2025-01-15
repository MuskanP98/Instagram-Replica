import os

class Config:
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'secret-key'
    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
        'sqlite:///' + os.path.join(os.path.abspath(os.path.dirname(__file__)), 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    GOOGLE_APPLICATION_CREDENTIALS = os.environ.get('GOOGLE_APPLICATION_CREDENTIALS')
    GCS_BUCKET = os.environ.get('GCS_BUCKET')
    FIREBASE_CONFIG = {
        'apiKey': os.environ.get('AIzaSyCNKALyigYD8z1sMM7pPpaKvgkPlxWgzV8'),
        'authDomain': os.environ.get('cloudcomputingproject-378917.firebaseapp.com'),
        'databaseURL': os.environ.get('https://cloudcomputingproject-378917-default-rtdb.europe-west1.firebasedatabase.app'),
        'projectId': os.environ.get('cloudcomputingproject-378917'),
        'storageBucket': os.environ.get('cloudcomputingproject-378917.appspot.com'),
        'messagingSenderId': os.environ.get('168397816600'),
        'appId': os.environ.get('1:168397816600:web:1a6d8fecd023431d6a946d'),
        'measurementId': os.environ.get('FIREBASE_MEASUREMENT_ID')
    }
    POSTS_PER_PAGE = 10
    LANGUAGES = ['en', 'es']
    ELASTICSEARCH_URL = os.environ.get('ELASTICSEARCH_URL')
    LOG_TO_STDOUT = os.environ.get('LOG_TO_STDOUT')
    ADMINS = ['admin@example.com']
