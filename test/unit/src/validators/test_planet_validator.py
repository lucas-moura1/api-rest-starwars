import unittest

from unittest.mock import patch
from src.validators import PlanetValidator
from src.errors import RequestError

planet_json = {
    "name": "Teste",
    "climate": "teste",
    "terrain": "teste"
}

empty_planet_json = {}


class TestPlanetValidator(unittest.TestCase):

    def setUp(self) -> None:
        self.planet_validator = PlanetValidator()

    @patch('src.validators.planet_validator.validate_body_existence')
    @patch('src.validators.planet_validator.validate_field_existence')
    def test_should_check_validate_planet_fields_with_success(self, mock_validate_body_existence, mock_validate_field_existence) -> None:
        response = self.planet_validator.validate_planet_fields(planet_json)

        self.assertTrue(mock_validate_body_existence.called)
        self.assertTrue(mock_validate_field_existence.called)
        self.assertIsNone(response)

    def test_should_check_validate_planet_fields_with_raise(self) -> None:
        self.assertRaises(RequestError, self.planet_validator.validate_planet_fields, empty_planet_json)


if __name__ == '__main__':
    unittest.main()
