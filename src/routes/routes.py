import uuid
from flask import jsonify, request

from src import app
from src.controllers import PlanetController
from src.errors import RequestError

planet_controller = PlanetController()


@app.route('/planet', methods=['GET'])
def get_all_planets():
    response = planet_controller.get_planets()

    return response, 200


@app.route('/planet', methods=['POST'])
def create_planet():
    planet_json = request.json
    response = planet_controller.create_planet(planet_json)

    return response, 201


@app.route('/planet/name/<string:planet_name>', methods=['GET'])
def get_planet_by_name(planet_name):
    response = planet_controller.get_planet_by_name(planet_name)

    return response


@app.route('/planet/id/<planet_id>', methods=['GET'])
def get_planet_by_id(planet_id):
    response = planet_controller.get_planet_by_id(planet_id)

    return response


@app.route('/planet', methods=['PATCH'])
def update_planet():
    planet_name = request.args.get('name')
    planet_json = request.json
    response = planet_controller.update_planet(planet_name, planet_json)

    return response, 200


@app.route('/planet', methods=['DELETE'])
def delete_planet():
    planet_name = request.args.get('name')
    response = planet_controller.delete_planet(planet_name)

    return response, 200


@app.errorhandler(RequestError)
def handle_error_request_api(error):
    response = jsonify(error.to_dict())
    response.status_code = error.status_code
    return response


@app.before_request
def log_request_information():
    request.request_id = str(uuid.uuid4())
    request.request_method = request.method
