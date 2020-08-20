from pymongo import MongoClient
import logging

from src.settings.configuration import DB_MONGODB_ENDPOINT, define_db_name
from src.errors import RequestError

db_name = define_db_name()

try:
    mongo = MongoClient(DB_MONGODB_ENDPOINT)

    planet_db = mongo[db_name]

    planet_collection = planet_db[db_name]
    planet_collection.create_index("name", unique=True)
except Exception as err:
    logging.error(f'Error from database {err.msg}')
    raise
