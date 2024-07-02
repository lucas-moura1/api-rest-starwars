import pytest
from unittest.mock import patch
from src.services.starwars_api import SWAPI


@pytest.fixture
def swapi():
    return SWAPI()


@pytest.mark.asyncio
@patch("requests.get")
async def test_successfully_get_all_planets(mock_request, swapi):
    mock_request.return_value.json.return_value = {
        "results": [{"name": "Tatooine"}, {"name": "Coruscant"}, {"name": "Hoth"}],
        "next": None,
    }
    await swapi.get_all_planets()
    assert len(swapi.planets) == 3


@pytest.mark.asyncio
@patch("requests.get")
async def test_error_get_all_planets(mock_request, swapi):
    swapi.planets = []
    mock_request.side_effect = Exception("Some error occurred")
    with pytest.raises(Exception):
        await swapi.get_all_planets()


@pytest.mark.asyncio
async def test_planets_filled_get_all_planets(swapi):
    swapi.planets = [{"name": "Tatooine"}, {"name": "Coruscant"}, {"name": "Hoth"}]
    await swapi.get_all_planets()
    assert len(swapi.planets) == 3


def test_successfully_get_planet_by_name(swapi):
    swapi.planets = [{"name": "Tatooine"}, {"name": "Coruscant"}, {"name": "Hoth"}]

    planet = swapi.get_planet_by_name("Coruscant")
    assert planet["name"] == "Coruscant"


def test_return_none_get_planet_by_name(swapi):
    swapi.planets = [{"name": "Tatooine"}]

    planet = swapi.get_planet_by_name("Coruscant")
    assert planet is None
