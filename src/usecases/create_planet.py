import logging
from src.repositories.repositories import PlanetRepository
from src.entities.planet import Planet
from src.services.starwars_api import StarWarsApi
from src.usecases.errors.planet_already_exists_error import PlanetAlreadyExistsError
from src.usecases.errors.invalid_planet_request import InvalidPlanetRequestError


class CreatePlanet:
    def __init__(self, planet_repository: PlanetRepository, star_wars_api: StarWarsApi):
        self.planet_repository = planet_repository
        self.star_wars_api = star_wars_api

    def perform(self, name: str, climate: str, terrain: str):
        logging.info("Creating planet")
        planet = self.planet_repository.get_by_name(name)
        if planet:
            raise PlanetAlreadyExistsError("Planet already exists")

        swapi_planet = self.star_wars_api.get_planet_by_name(name)
        if not swapi_planet:
            raise InvalidPlanetRequestError("Planet not exists in swapi")

        try:
            planet = Planet(
                name=name,
                climate=climate,
                terrain=terrain,
                count_films=len(swapi_planet["films"]),
            )
        except Exception as e:
            raise InvalidPlanetRequestError(str(e))

        return self.planet_repository.add(planet)
