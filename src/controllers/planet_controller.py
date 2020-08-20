import logging
from bson.json_util import dumps, ObjectId

from src.validators import PlanetValidator
from src.settings.database import planet_collection
from src.errors import RequestError
from src.utils import RequestSWAPI


class PlanetController:

    def __init__(self):
        self.planet_validator = PlanetValidator()
        self.request_swapi = RequestSWAPI()

    def get_planets(self) -> dict:
        logging.info('Getting all planets')
        planets = dumps(planet_collection.find())

        return planets

    def get_planet_by_name(self, planet_name: str) -> dict:
        logging.info(f'Getting planet by name: {planet_name}')
        planet = dumps(planet_collection.find_one({'name': planet_name}))

        return planet

    def get_planet_by_id(self, planet_id: int) -> dict:
        logging.info(f'Getting planet by id: {planet_id}')
        planet = dumps(planet_collection.find_one({'_id': ObjectId(planet_id)}))

        return planet

    def create_planet(self, planet_json: dict) -> dict:
        logging.info(f'Creating a planet: {planet_json}')
        self.planet_validator.validate_planet_fields(planet_json)

        count_films = self.request_swapi.get_count_films(planet_json.get('name'))

        planet = {
            'name': planet_json.get('name'),
            'climate': planet_json.get('climate'),
            'terrain': planet_json.get('terrain'),
            'count_films': count_films
        }
        try:
            response = planet_collection.insert_one(planet)
            logging.info(f'Creating planet with success ')

            return dumps(response.inserted_id)
        except Exception as err:
            logging.error(f'Error => {err.details}')
            raise RequestError(err.details.get('errmsg'), 409)

    def update_planet(self, planet_name: str, planet_json: dict) -> dict:
        logging.info(f'Updating {planet_name} planet')
        try:
            response = planet_collection.update_one({
                'name': planet_name
            }, {'$set': planet_json})
            logging.info(f'Updating planet with success ')

            return {'updated_count': response.modified_count}
        except Exception as err:
            logging.error(f'Error => {err.details}')
            raise RequestError(err.details.get('errmsg'), 409)

    def delete_planet(self, planet_name: str) -> dict:
        logging.info(f'Deleting {planet_name} planet')
        response = planet_collection.delete_one({"name": planet_name})

        return {'delete_count': response.deleted_count}
