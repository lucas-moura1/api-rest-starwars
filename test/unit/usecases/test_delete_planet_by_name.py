from unittest.mock import MagicMock

import pytest
from src.usecases.delete_planet_by_name import DeletePlanetByName


def test_successfully_delete_planet_by_name():
    planet_repository_mock = MagicMock()
    delete_planet = DeletePlanetByName(planet_repository_mock)
    name = "Alderaan"

    delete_planet.perform(name)

    planet_repository_mock.delete.assert_called_once_with(name)


def test_failed_delete_planet_by_name():
    planet_repository_mock = MagicMock()
    delete_planet = DeletePlanetByName(planet_repository_mock)
    name = "Alderaan"

    planet_repository_mock.delete.side_effect = Exception("Some error occurred")

    with pytest.raises(Exception):
        delete_planet.perform(name)
