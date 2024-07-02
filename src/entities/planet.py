from pydantic import BaseModel


class Planet(BaseModel):
    name: str
    climate: str
    terrain: str
    count_films: int
