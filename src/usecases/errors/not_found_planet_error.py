class NotFoundPlanetError(Exception):
    def __init__(self):
        super().__init__("Planet not found")
