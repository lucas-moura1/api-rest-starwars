import asyncio

from fastapi import APIRouter, status, Response
from pydantic import BaseModel
from pymongo import MongoClient

from src.config import DB_MONGODB_ENDPOINT, DB_MONGODB_NAME
from src.repositories.mongo_planet_repository import MongoPlanetRepository
from src.services.starwars_api import SWAPI
from src.usecases.create_planet import CreatePlanet
from src.usecases.delete_planet_by_name import DeletePlanetByName
from src.usecases.errors.invalid_planet_request import InvalidPlanetRequestError
from src.usecases.errors.not_found_planet_error import NotFoundPlanetError
from src.usecases.errors.planet_already_exists_error import PlanetAlreadyExistsError
from src.usecases.get_all_planets import GetAllPlanets
from src.usecases.get_planet_by_name import GetPlanetByName
from src.usecases.update_planet import UpdatePlanet


class CreatePlanetRequest(BaseModel):
    name: str
    climate: str
    terrain: str


class UpdatePlanetRequest(BaseModel):
    climate: str | None = None
    terrain: str | None = None
    count_films: int | None = None


router = APIRouter()

mongo_client = MongoClient(DB_MONGODB_ENDPOINT)
planet_repository = MongoPlanetRepository(mongo_client, DB_MONGODB_NAME)
swapi = SWAPI()
asyncio.gather(swapi.get_all_planets())


@router.get("/planets")
def get_planets():
    get_all_planets_usecase = GetAllPlanets(planet_repository)
    planets = get_all_planets_usecase.perform()
    return planets


@router.get("/planets/{planet_name}")
def get_planet_by_name(planet_name: str, response: Response):
    try:
        get_planet_by_name_usecase = GetPlanetByName(planet_repository)
        planet = get_planet_by_name_usecase.perform(planet_name)
        return planet
    except NotFoundPlanetError as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"{e}"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": f"{e}"}


@router.post("/planets", status_code=status.HTTP_201_CREATED)
def create_planet(body: CreatePlanetRequest, response: Response):
    try:
        create_planet_usecase = CreatePlanet(planet_repository, swapi)
        create_planet_usecase.perform(**body.model_dump())
        return
    except PlanetAlreadyExistsError as e:
        response.status_code = status.HTTP_409_CONFLICT
        return {"error": f"{e}"}
    except InvalidPlanetRequestError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": f"{e}"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": f"{e}"}


@router.put("/planets/{planet_name}")
def update_planet(planet_name: str, body: UpdatePlanetRequest, response: Response):
    try:
        update_planet_usecase = UpdatePlanet(planet_repository)
        update_planet_usecase.perform(planet_name, **body.model_dump())
        return
    except NotFoundPlanetError as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"{e}"}
    except InvalidPlanetRequestError as e:
        response.status_code = status.HTTP_400_BAD_REQUEST
        return {"error": f"{e}"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": f"{e}"}


@router.delete("/planets/{planet_name}")
def delete_planet(planet_name: str, response: Response):
    try:
        delete_planet_usecase = DeletePlanetByName(planet_repository)
        delete_planet_usecase.perform(planet_name)
        return
    except NotFoundPlanetError as e:
        response.status_code = status.HTTP_404_NOT_FOUND
        return {"error": f"{e}"}
    except Exception as e:
        response.status_code = status.HTTP_500_INTERNAL_SERVER_ERROR
        return {"error": f"{e}"}
