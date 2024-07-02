import logging
from src.entities.planet import Planet
from src.usecases.errors.not_found_planet_error import NotFoundPlanetError
from src.usecases.errors.invalid_planet_request import InvalidPlanetRequestError
from src.repositories.repositories import PlanetRepository


class UpdatePlanet:
    def __init__(self, planet_repository: PlanetRepository):
        self.planet_repository = planet_repository

    def perform(
        self, planet_name: str, climate: str, terrain: str, count_films: int
    ) -> None:
        logging.info(f"Updating planet {planet_name}")
        planet = self.planet_repository.get_by_name(planet_name)
        if not planet:
            raise NotFoundPlanetError()
        planet = Planet(**planet)
        try:
            update_planet = Planet(
                name=planet.name,
                climate=climate or planet.climate,
                terrain=terrain or planet.terrain,
                count_films=count_films or planet.count_films,
            )
        except Exception as e:
            raise InvalidPlanetRequestError([str(e)])

        self.planet_repository.update(update_planet)
