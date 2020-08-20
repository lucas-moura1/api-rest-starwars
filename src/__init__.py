from flask import Flask
from src.utils import logger


app = Flask(__name__)


from src.routes import routes
