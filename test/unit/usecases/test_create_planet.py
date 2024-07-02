import pytest
from unittest.mock import MagicMock
from src.entities.planet import Planet
from src.usecases.create_planet import CreatePlanet
from src.repositories.repositories import PlanetRepository
from src.services.starwars_api import StarWarsApi
from src.usecases.errors.planet_already_exists_error import PlanetAlreadyExistsError
from src.usecases.errors.invalid_planet_request import InvalidPlanetRequestError


@pytest.fixture
def create_planet():
    planet_repository = MagicMock(spec=PlanetRepository)
    star_wars_api = MagicMock(spec=StarWarsApi)
    return CreatePlanet(planet_repository, star_wars_api)


def test_successfully_create_planet(create_planet):
    name = "Tatooine"
    climate = "Arid"
    terrain = "Desert"

    planet_repository = create_planet.planet_repository
    star_wars_api = create_planet.star_wars_api

    swapi_planet = {"name": "Tatooine", "films": ["A New Hope", "The Phantom Menace"]}
    star_wars_api.get_planet_by_name.return_value = swapi_planet
    planet_repository.get_by_name.return_value = None

    result = create_planet.perform(name, climate, terrain)

    assert result is not None
    assert planet_repository.add.called_once_with(
        name=name, climate=climate, terrain=terrain, count_films=2
    )


def test_already_exists_error_create_planet(create_planet):
    name = "Tatooine"
    climate = "Arid"
    terrain = "Desert"

    planet_repository = create_planet.planet_repository
    star_wars_api = create_planet.star_wars_api

    swapi_planet = {"name": "Tatooine", "films": ["A New Hope", "The Phantom Menace"]}
    star_wars_api.get_planet_by_name.return_value = swapi_planet
    mock_planet = Planet(name=name, climate=climate, terrain=terrain, count_films=2)
    planet_repository.get_by_name.return_value = mock_planet

    with pytest.raises(PlanetAlreadyExistsError):
        create_planet.perform(name, climate, terrain)


def test_invalid_request_create_planet(create_planet):
    name = "Nonexistent Planet"
    climate = "Unknown"
    terrain = "Unknown"

    planet_repository = create_planet.planet_repository
    star_wars_api = create_planet.star_wars_api

    star_wars_api.get_planet_by_name.return_value = None
    planet_repository.get_by_name.return_value = None

    with pytest.raises(InvalidPlanetRequestError):
        create_planet.perform(name, climate, terrain)


def test_invalid_planet_request_error_create_planet(create_planet):
    name = "Tatooine"
    climate = "Arid"
    terrain = 1

    planet_repository = create_planet.planet_repository
    star_wars_api = create_planet.star_wars_api

    swapi_planet = {"name": "Tatooine", "films": ["A New Hope", "The Phantom Menace"]}
    star_wars_api.get_planet_by_name.return_value = swapi_planet
    planet_repository.get_by_name.return_value = None

    with pytest.raises(InvalidPlanetRequestError):
        create_planet.perform(name, climate, terrain)
        planet_repository.add.assert_not_called()
