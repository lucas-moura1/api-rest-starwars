import pytest
from unittest.mock import MagicMock
from src.usecases.errors.invalid_planet_request import InvalidPlanetRequestError
from src.usecases.errors.not_found_planet_error import NotFoundPlanetError
from src.repositories.repositories import PlanetRepository
from src.usecases.update_planet import UpdatePlanet


@pytest.fixture
def update_planet():
    planet_repository = MagicMock(spec=PlanetRepository)
    return UpdatePlanet(planet_repository)


def test_successfully_update_planet():
    planet_repository_mock = MagicMock()
    planet_repository_mock.get_by_name.return_value = {
        "name": "Tatooine",
        "climate": "arid",
        "terrain": "desert",
        "count_films": 5,
    }

    update_planet = UpdatePlanet(planet_repository_mock)

    update_planet.perform("Tatooine", "temperate", "desert", 5)

    planet_repository_mock.get_by_name.assert_called_once()
    assert planet_repository_mock.update.called_once()


def test_not_found_update_planet():
    planet_repository_mock = MagicMock()
    planet_repository_mock.get_by_name.return_value = None

    update_planet = UpdatePlanet(planet_repository_mock)

    with pytest.raises(NotFoundPlanetError):
        update_planet.perform("Alderaan", "temperate", "grasslands", 2)
        planet_repository_mock.get_by_name.assert_called_once()


def test_invalid_request_update_planet():
    planet_repository_mock = MagicMock()
    planet_repository_mock.get_by_name.return_value = {
        "name": "Hoth",
        "climate": "frozen",
        "terrain": "tundra",
        "count_films": 3,
    }

    update_planet = UpdatePlanet(planet_repository_mock)

    with pytest.raises(InvalidPlanetRequestError):
        update_planet.perform("Hoth", "frozen", "tundra", "three")
        planet_repository_mock.get_by_name.assert_called_once()


def test_failed_update_planet():
    planet_repository_mock = MagicMock()
    planet_repository_mock.get_by_name.return_value = {
        "name": "Endor",
        "climate": "temperate",
        "terrain": "forests",
        "count_films": 1,
    }
    planet_repository_mock.update.side_effect = Exception("Some error occurred")

    update_planet = UpdatePlanet(planet_repository_mock)

    with pytest.raises(Exception):
        update_planet.perform("Endor", "temperate", "forests", 1)
        planet_repository_mock.get_by_name.assert_called_once()
        planet_repository_mock.update.assert_called_once()
