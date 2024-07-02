from abc import ABC, abstractmethod
from typing import List
from src.entities.planet import Planet


class PlanetRepository(ABC):
    @abstractmethod
    def get_all(self) -> List[Planet]:
        raise NotImplementedError

    @abstractmethod
    def get_by_name(self, planet_name: int) -> Planet:
        raise NotImplementedError

    @abstractmethod
    def add(self, planet: Planet) -> None:
        raise NotImplementedError

    @abstractmethod
    def update(self, planet: Planet) -> None:
        raise NotImplementedError

    @abstractmethod
    def delete(self, planet_name: str) -> None:
        raise NotImplementedError
