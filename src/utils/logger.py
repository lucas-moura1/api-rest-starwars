import logging
import sys
from flask import request


class LogFormatter(logging.Formatter):

    def format(self, record):
        record.request_id = request.request_id
        record.request_method = request.request_method
        return super(LogFormatter, self).format(record)


handler = logging.StreamHandler(sys.stdout)

handler.setFormatter(
    LogFormatter("[%(asctime)s] [%(request_method)s] [%(filename)s] [%(levelname)s] [%(request_id)s] - "
                 "%(message)s")
)

logging.getLogger().setLevel(logging.INFO)
logging.getLogger().addHandler(handler)
