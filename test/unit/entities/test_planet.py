import pytest
from pydantic import ValidationError
from src.entities.planet import Planet


def test_successfully_planet_creation():
    planet = Planet(name="Tatooine", climate="arid", terrain="desert", count_films=5)

    assert planet.name == "Tatooine"
    assert planet.climate == "arid"
    assert planet.terrain == "desert"
    assert planet.count_films == 5


def test_error_planet_creation():
    with pytest.raises(ValidationError):
        Planet(name="Tatooine", climate="arid", terrain="desert", count_films="invalid")
