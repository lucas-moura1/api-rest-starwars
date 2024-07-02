import pytest
from unittest.mock import MagicMock
from src.usecases.get_all_planets import GetAllPlanets


def test_successfully_get_all_planets():
    planet_repository_mock = MagicMock()
    planet_repository_mock.get_all.return_value = [
        {"name": "Tatooine", "climate": "arid", "terrain": "desert", "count_films": 5},
        {"name": "Hoth", "climate": "frozen", "terrain": "tundra", "count_films": 1},
    ]

    get_all_planets = GetAllPlanets(planet_repository_mock)

    result = get_all_planets.perform()

    planet_repository_mock.get_all.assert_called_once()
    assert result == [
        {"name": "Tatooine", "climate": "arid", "terrain": "desert", "count_films": 5},
        {"name": "Hoth", "climate": "frozen", "terrain": "tundra", "count_films": 1},
    ]


def test_error_get_all_planets():
    planet_repository_mock = MagicMock()
    planet_repository_mock.get_all.side_effect = Exception("Some error occurred")

    get_all_planets = GetAllPlanets(planet_repository_mock)

    with pytest.raises(Exception):
        get_all_planets.perform()
        planet_repository_mock.get_all.assert_called_once()
