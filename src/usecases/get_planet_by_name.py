import logging
from src.repositories.repositories import PlanetRepository
from src.usecases.errors.not_found_planet_error import NotFoundPlanetError
from src.usecases.errors.invalid_planet_request import InvalidPlanetRequestError


class GetPlanetByName:
    def __init__(self, planet_repository: PlanetRepository):
        self.planet_repository = planet_repository

    def perform(self, planet_name: str):
        try:
            logging.info(f"Getting planet by name: {planet_name}")
            if not planet_name:
                raise InvalidPlanetRequestError("Planet name is required")

            planet = self.planet_repository.get_by_name(planet_name)

            if not planet:
                raise NotFoundPlanetError()
            return planet
        except Exception as e:
            logging.error(f"An error occurred: {str(e)}")
            raise e
