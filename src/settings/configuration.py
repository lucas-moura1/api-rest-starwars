import os

env = os.environ.get('ENV')

DB_MONGODB_NAME_TEST = os.environ.get('DB_MONGODB_NAME_TEST')
DB_MONGODB_NAME = os.environ.get('DB_MONGODB_NAME')
DB_MONGODB_ENDPOINT = os.environ.get('DB_MONGODB_ENDPOINT')
URL_SWAPI = os.environ.get('URL_SWAPI')


def define_db_name() -> str:
    if env == 'test':
        return DB_MONGODB_NAME_TEST
    else:
        return DB_MONGODB_NAME
