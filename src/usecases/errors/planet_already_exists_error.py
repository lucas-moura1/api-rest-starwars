from typing import List


class PlanetAlreadyExistsError(Exception):
    def __init__(self, message: List[str]):
        super().__init__(message)
