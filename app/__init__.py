from flask import Flask
from flask_mongoengine import MongoEngine
from flask_cache import  Cache
import config

app = Flask(__name__)

app.config["MONGODB_SETTINGS"] = config.MONGODB_SETTINGS
db = MongoEngine(app)

MEMCACHED_SERVER = '{}:{}'.format(config.MEMCACHED_SETTINGS['SERVER'],config.MEMCACHED_SETTINGS['PORT'])
cache = Cache(app, config={'CACHE_TYPE': 'memcached','CACHE_MEMCACHED_SERVERS': [MEMCACHED_SERVER]})

from app import routes,db
