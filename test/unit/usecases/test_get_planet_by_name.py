import pytest
from unittest.mock import MagicMock

from src.usecases.get_planet_by_name import GetPlanetByName
from src.usecases.errors.not_found_planet_error import NotFoundPlanetError


def test_successfully_get_planet_by_name():
    planet_repository_mock = MagicMock()
    planet_repository_mock.get_by_name.return_value = {
        "name": "Tatooine",
        "climate": "arid",
        "terrain": "desert",
    }

    get_planet_by_name = GetPlanetByName(planet_repository_mock)
    planet_name = "Tatooine"

    result = get_planet_by_name.perform(planet_name)

    assert result == {"name": "Tatooine", "climate": "arid", "terrain": "desert"}
    planet_repository_mock.get_by_name.assert_called_once_with(planet_name)


def test_not_found_get_planet_by_name():
    planet_repository_mock = MagicMock()
    planet_repository_mock.get_by_name.return_value = None

    get_planet_by_name = GetPlanetByName(planet_repository_mock)
    planet_name = "Alderaan"

    with pytest.raises(NotFoundPlanetError):
        get_planet_by_name.perform(planet_name)
        planet_repository_mock.get_by_name.assert_called_once_with(planet_name)


def test_failed_get_planet_by_name():
    planet_repository_mock = MagicMock()
    planet_repository_mock.get_by_name.side_effect = Exception("An error occurred")

    get_planet_by_name = GetPlanetByName(planet_repository_mock)
    planet_name = "Tatooine"

    with pytest.raises(Exception):
        get_planet_by_name.perform(planet_name)
        planet_repository_mock.get_by_name.assert_called_once_with(planet_name)
