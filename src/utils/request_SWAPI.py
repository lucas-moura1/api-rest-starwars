import requests
import logging

from src.settings.configuration import URL_SWAPI
from src.errors.request_error import RequestError


class RequestSWAPI:

    def get_all_planets(self) -> dict:
        logging.info('Getting all planets from SWAPI')
        try:
            response = requests.get(URL_SWAPI)

            return response.json()
        except Exception as err:
            raise RequestError(err, 409)


    def get_count_films(self, planet_name) -> int:
        logging.info(f'Verifying  {planet_name} planet name exist and get amount films')
        planets = self.get_all_planets()

        for planet in planets.get('results'):
            if planet_name == planet.get('name'):
                count_films = len(planet.get('films'))
                break
            else:
                count_films = False

        if count_films is False:
            raise RequestError('Planet do not exist, insert a valid planet', 409)

        return count_films
