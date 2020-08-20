class RequestError(Exception):
    def __init__(self, message: str, status_code: int) -> None:
        Exception.__init__(self)
        self.message = message
        self.status_code = status_code

    def to_dict(self) -> dict:
        return {
            'message': self.message,
            'status_code': self.status_code
        }
