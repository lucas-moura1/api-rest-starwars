import unittest
from unittest.mock import patch, MagicMock

from src.controllers import PlanetController
from src.validators import PlanetValidator
from src.utils import RequestSWAPI


class TestPlanetController(unittest.TestCase):

    def setUp(self) -> None:
        self.planet_controller = PlanetController()
        self.planet_validator = PlanetValidator()
        self.request_swapi = RequestSWAPI()

    @patch('src.controllers.planet_controller.planet_collection.find')
    def test_should_get_planets(self, mock_planet_collection) -> None:

        mock_planet_collection.return_value = [{},{}]

        response = self.planet_controller.get_planets()

        self.assertTrue(mock_planet_collection.called)
        self.assertIsNotNone(response)

    @patch('src.controllers.planet_controller.planet_collection.find_one')
    def test_should_get_planet_by_name_and_by_id(self, mock_planet_collection) -> None:
        planet_name = ''

        response = self.planet_controller.get_planet_by_name(planet_name)

        self.assertTrue(mock_planet_collection.called)
        self.assertIsNotNone(response)

    @patch('src.controllers.planet_controller.planet_collection.insert_one')
    def test_should_create_planet(self, mock_planet_collection) -> None:
        planet_json = {'name': 'teste', 'climate': 'teste', 'terrain': 'teste'}
        self.planet_controller.planet_validator.validate_planet_fields = MagicMock(return_value=None)
        self.planet_controller.request_swapi.get_count_films = MagicMock(return_value=1)

        response = self.planet_controller.create_planet(planet_json)

        self.planet_controller.planet_validator.validate_planet_fields.assert_called_with(planet_json)
        self.planet_controller.request_swapi.get_count_films.assert_called_with('teste')
        self.assertIsNotNone(response)

    @patch('src.controllers.planet_controller.planet_collection.update_one')
    def test_should_update_planet(self, mock_planet_collection) -> None:
        planet_name = 'teste'
        planet_json = {'name': 'teste', 'climate': 'teste', 'terrain': 'teste'}

        response = self.planet_controller.update_planet(planet_name, planet_json)

        self.assertTrue(mock_planet_collection.called)
        self.assertIsNotNone(response)

    @patch('src.controllers.planet_controller.planet_collection.delete_one')
    def test_should_delete_planet(self, mock_planet_collection) -> None:
        planet_name = 'teste'

        response = self.planet_controller.delete_planet(planet_name)

        self.assertTrue(mock_planet_collection.called)
        self.assertIsNotNone(response)


if __name__ == '__main__':
    unittest.main()
