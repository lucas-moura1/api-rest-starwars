import logging
from src.repositories.repositories import PlanetRepository


class DeletePlanetByName:
    def __init__(self, planet_repository: PlanetRepository):
        self.planet_repository = planet_repository

    def perform(self, name: str) -> None:
        try:
            logging.info(f"Deleting planet by name: {name}")
            self.planet_repository.delete(name)
        except Exception as e:
            logging.error(f"An error occurred: {e}")
            raise e
