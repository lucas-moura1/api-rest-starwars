import unittest
from unittest.mock import patch, MagicMock

from src.utils import RequestSWAPI


class TestRequestSWAPI(unittest.TestCase):

    def setUp(self) -> None:
        self.request_swapi = RequestSWAPI()

    @patch('src.utils.request_SWAPI.requests')
    def test_should_get_all_planets(self, mock_requests) -> None:

        self.request_swapi.get_all_planets()

        mock_requests.get.assert_called()

    def test_should_get_count_films(self) -> None:
        planet_name = ''
        json_swapi = {'results': [{'name': '', 'films': ['film1', 'film2']}]}

        self.request_swapi.get_all_planets = MagicMock(return_value=json_swapi)

        response = self.request_swapi.get_count_films(planet_name)

        self.request_swapi.get_all_planets.assert_called_once()
        self.assertEqual(response, 2)


if __name__ == '__main__':
    unittest.main()
