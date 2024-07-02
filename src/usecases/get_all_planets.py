import logging
from src.repositories.repositories import PlanetRepository


class GetAllPlanets:
    def __init__(self, planet_repository: PlanetRepository):
        self.planet_repository = planet_repository

    def perform(self):
        try:
            logging.info("Getting all planets")
            planets = self.planet_repository.get_all()
            return planets
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            raise Exception({"error": str(e)})
