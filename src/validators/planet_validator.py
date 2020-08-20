import logging

from .validator import validate_body_existence, validate_field_existence


class PlanetValidator:

    @staticmethod
    def validate_planet_fields(planet_json: dict) -> None:
        logging.info('Validating planet datas')
        validate_body_existence(planet_json)
        validate_field_existence(planet_json, 'name')
        validate_field_existence(planet_json, 'climate')
        validate_field_existence(planet_json, 'terrain')
