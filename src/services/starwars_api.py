import logging
import requests
from abc import ABC, abstractmethod

from src.config import URL_SWAPI


class StarWarsApi(ABC):
    @abstractmethod
    def get_planet_by_name(self):
        raise NotImplementedError


class SWAPI(StarWarsApi):
    planets = []

    async def get_all_planets(self):
        if self.planets:
            return

        try:
            logging.info("Requesting all planets from swapi")
            has_next = True
            page = 1
            while has_next:
                url = f"{URL_SWAPI}/?page={page}"
                response = requests.get(url)
                data = response.json()
                self.planets += data["results"]

                if data["next"] is None:
                    has_next = False
                    break

                page += 1

            logging.info("All planets requested from swapi")
        except Exception as e:
            logging.error(f"Error to request swapi: {str(e)}")
            raise e

    def get_planet_by_name(self, planet_name: str):
        for planet in self.planets:
            if planet["name"].lower() == planet_name.lower():
                return planet

        return None
